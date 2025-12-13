import random
from collections import Counter
from pathlib import Path

from otree.api import *

from . import understanding
from .fields_labels_choices import *

doc = """
Stealing / Taking game
"""

app_name = Path(__file__).parent.name


class C(BaseConstants):
    NAME_IN_URL = "whgame"
    PLAYERS_PER_GROUP = Config.PLAYERS_PER_GROUP
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    reward = models.BooleanField()
    num_of_takers = models.IntegerField()
    num_of_reporters = models.IntegerField()
    society_opinion_majority = models.IntegerField()

    def creating_session(self):
        self.reward = self.session.config.get("reward", False)

        if "groups" not in self.session.vars:
            self.group_randomly()
            self.session.vars["groups"] = self.get_group_matrix()
        self.set_group_matrix(self.session.vars["groups"])

        inactive_group = random.choice(self.get_groups())
        for g in self.get_groups():
            g.active = g != inactive_group

        active_groups = [g for g in self.get_groups() if g.active]
        for g in active_groups:
            players = g.get_players()
            taker = random.choice(players)
            for p in players:
                p.taker = p == taker

    def compute_payoffs(self):
        active_groups = [g for g in self.get_groups() if g.active]
        for g in active_groups:
            players = g.get_players()
            reporters = [p for p in players if not p.taker]
            selected_reporter = random.choice(reporters)
            g.selected_reporter = selected_reporter.id_in_group
            g.reporter_has_reported = selected_reporter.reporting_decision

            if g.taker_has_taken and g.reporter_has_reported:
                g.audit_draw = random.uniform(0, 1)
                g.taker_audited = g.audit_draw < Config.AUDIT_PROBABILITY

        self.num_of_takers = sum([g.taker_has_taken for g in active_groups])
        self.num_of_reporters = sum(
            [p.reporting_decision for p in self.get_players() if p.group.active and not p.taker])

        soc_op_maj = [p.society_opinion for p in self.get_players()]
        soc_op_maj_count = Counter(soc_op_maj)
        self.society_opinion_majority = int(soc_op_maj_count.most_common(1)[0][0])

        for p in self.get_players():
            p.compute_payoffs()


def creating_session(subsession: Subsession):
    subsession.creating_session()


class Group(BaseGroup):
    active = models.BooleanField()
    taker_has_taken = models.BooleanField(initial=False)
    selected_reporter = models.IntegerField()
    reporter_has_reported = models.BooleanField(initial=False)
    audit_draw = models.FloatField()
    taker_audited = models.BooleanField(initial=False)


class Player(BasePlayer):
    # understanding questionnaire
    game_q1_faults = models.IntegerField()
    game_q2_faults = models.IntegerField()
    game_q3_faults = models.IntegerField()
    game_q4_faults = models.IntegerField()
    game_total_faults = models.IntegerField()

    taker = models.BooleanField()
    taking_decision = models.BooleanField(choices=[], widget=widgets.RadioSelectHorizontal)
    estimation_reporting = models.IntegerField(min=0, max=100)
    reporting_decision = models.BooleanField(widget=widgets.RadioSelectHorizontal)
    audit_draw = models.FloatField()
    audit = models.BooleanField()
    payoff_ecu = models.FloatField()

    # Questions
    taker_motivation = models.LongStringField()
    reporter_motivation = models.LongStringField()
    personal_opinion = models.IntegerField(choices=[], widget=widgets.RadioSelect)
    society_opinion = models.IntegerField(choices=[], widget=widgets.RadioSelect)

    def compute_payoffs(self):
        lang = self.session.vars["lang"]
        # --- Active group ---
        if self.group.active:
            txt_final = trans(dict(
                en=f"Your group has been randomly selected to be an Active group. "
                   f"Inside your group you had the role of a {'Red' if self.taker else 'Blue'} Player. ",
                fr=f"Votre groupe a été tiré au sort pour être un groupe Actif. "
                   f"Dans votre groupe, vous avez eu le rôle de joueur "
                   f"{'Rouge' if self.taker else 'Bleu'}. ",
                vi=f"Nhóm của bạn đã được chọn ngẫu nhiên để trở thành nhóm Chủ động. "
                   f"Trong nhóm của bạn, bạn có vai trò là người chơi {'Đỏ' if self.taker else 'Xanh'}. "
            ), lang)

            if self.taker:  # Red Player
                if self.taking_decision:  # Taker
                    txt_final += trans(dict(
                        en=f"You decided to steal ECU from the Passive group. ",
                        fr=f"Vous avez décidé de voler des ECU au groupe Passif. ",
                        vi=f"Bạn đã quyết định lấy cắp ECU từ nhóm Bị động. "
                    ), lang)

                    if self.group.reporter_has_reported:  # Reported
                        txt_final += trans(dict(
                            en=f"The selected Blue Player has decided to report you. ",
                            fr=f"Le joueur Bleu sélectionné a décidé de vous signalez. ",
                            vi=f"Người chơi Xanh được chọn đã quyết định báo cáo bạn. "
                        ), lang)

                        if self.group.taker_audited:  # Audited
                            txt_final += trans(dict(
                                en=f"You were audited and fined {Config.STEALING_PENALTY} ECU. ",
                                fr=f"Vous avez été pénalisé d'un montant de {Config.STEALING_PENALTY} ECU. ",
                                vi=f"Bạn đã bị kiểm toán và bị phạt {Config.STEALING_PENALTY} ECU. "
                            ), lang)
                            self.payoff_ecu = Config.STEALING_AMOUNT - Config.STEALING_PENALTY

                        else:  # Not Audited
                            txt_final += trans(dict(
                                en=f"You were not audited. ",
                                fr=f"Vous n'avez pas été pénalisé. ",
                                vi=f"Bạn đã không bị kiểm toán. "
                            ), lang)
                            self.payoff_ecu = Config.STEALING_AMOUNT

                    else:  # Not Reported
                        txt_final += trans(dict(
                            en=f"You were not reported. ",
                            fr=f"Vous n'avez pas été signalé. ",
                            vi=f"Bạn đã không bị báo cáo. "
                        ), lang)
                        self.payoff_ecu = Config.STEALING_AMOUNT

                else:  # Not Taker
                    txt_final += trans(dict(
                        en=f"You decided not to steal some ECU from the Passive group. ",
                        fr=f"Vous avez décidé de ne pas voler d'ECU au groupe Passif. ",
                        vi=f"Bạn đã quyết định không lấy cắp ECU từ nhóm Bị động. "
                    ), lang)
                    self.payoff_ecu = 0

            else:  # Blue Player
                # Initialisation par sécurité (couvre le cas "Not Reporter" et "Reporter non sélectionné")
                self.payoff_ecu = 0

                if self.reporting_decision:  # Reporter
                    txt_final += trans(dict(
                        en=f"You decided to report the Red Player. ",
                        fr=f"Vous avez décidé de signaler le joueur Rouge. ",
                        vi=f"Bạn đã quyết định báo cáo người chơi Đỏ. "), lang)

                    # Case 1 : Blue Player is selected
                    if self.group.selected_reporter == self.id_in_group:
                        txt_final += trans(dict(
                            en=f"You were selected to be the reporter. ",
                            fr=f"Votre décision de signalement a été sélectionnée. ",
                            vi=f"Quyết định báo cáo của bạn đã được chọn. "
                        ), lang)

                        if self.group.taker_has_taken:  # Taker stole
                            txt_final += trans(dict(
                                en="The Red Player has stolen some ECU from the Passive group. ",
                                fr="Le joueur Rouge a volé des ECU au groupe Passif. ",
                                vi="Người chơi Đỏ đã lấy cắp một số ECU từ nhóm Bị động. "
                            ), lang)
                            self.payoff_ecu = -Config.REPORTING_COST  # Paye le coût de reporting

                            if self.group.taker_audited:  # Audited
                                txt_final += trans(dict(
                                    en="The Red Player was audited and fined. ",
                                    fr="Le joueur Rouge a été pénalisé. ",
                                    vi="Người chơi Đỏ đã bị kiểm toán và bị phạt. "
                                ), lang)

                                if self.subsession.reward:  # With reward
                                    txt_final += trans(dict(
                                        en=f"You received a reward of {Config.REPORTING_REWARD} ECU. ",
                                        fr=f"Vous avez reçu une récompense de {Config.REPORTING_REWARD} ECU. ",
                                        vi=f"Bạn đã nhận được phần thưởng {Config.REPORTING_REWARD} ECU. "
                                    ), lang)
                                    self.payoff_ecu += Config.REPORTING_REWARD

                            else:  # Not audited
                                txt_final += trans(dict(
                                    en="The Red Player was not audited. ",
                                    fr="Le joueur Rouge n'a pas été pénalisé. ",
                                    vi="Người chơi Đỏ đã không bị kiểm toán. "
                                ), lang)

                        else:  # Taker did not steal
                            txt_final += trans(dict(
                                en="The Red Player did not steal some ECU from the Passive group. ",
                                fr="Le joueur Rouge n'a pas volé d'ECU au groupe Passif. "
                                , vi="Người chơi Đỏ đã không lấy cắp ECU từ nhóm Bị động. "
                            ), lang)
                            # Pas de changement de payoff_ecu (reste à 0)

                    # Case 2 : Blue Player is not selected
                    else:
                        txt_final += trans(dict(
                            en="You were not selected to be the reporter. ",
                            fr="Votre décision de signalement n'a pas été sélectionnée. ",
                            vi="Quyết định báo cáo của bạn đã không được chọn. "
                        ), lang)

                        # Payoff reste à 0, mais on informe quand même de ce qu'a fait le Rouge
                        if self.group.taker_has_taken:
                            txt_final += trans(dict(
                                en="The Red Player has stolen some ECU from the Passive group. ",
                                fr="Le joueur Rouge a volé des ECU au groupe Passif. ",
                                vi="Người chơi Đỏ đã lấy cắp một số ECU từ nhóm Bị động. "
                            ), lang)

                        else:
                            txt_final += trans(dict(
                                en="The Red Player did not steal some ECU from the Passive group. ",
                                fr="Le joueur Rouge n'a pas volé d'ECU au groupe Passif. ",
                                vi="Người chơi Đỏ đã không lấy cắp ECU từ nhóm Bị động. "
                            ), lang)

                else:  # Not Reporter
                    txt_final += trans(dict(
                        en=f"You decided not to report the Red Player. ",
                        fr=f"Vous avez décidé de ne pas signaler le joueur Rouge. ",
                        vi=f"Bạn đã quyết định không báo cáo người chơi Đỏ. "
                    ), lang)
                    # self.payoff_ecu est déjà à 0

        # --- Passive group ---
        else:
            txt_final = trans(dict(
                en=f"Your group has been randomly selected to be a Passive group. ",
                fr=f"Votre groupe a été tiré au sort pour être un groupe Passif. ",
                vi=f"Nhóm của bạn đã được chọn ngẫu nhiên để trở thành nhóm Bị động. "
            ), lang)

            if self.subsession.num_of_takers > 0:  # At least one taker
                if self.subsession.num_of_takers == 1:
                    txt_final += trans(dict(
                        en=f"{self.subsession.num_of_takers} Red Player has decided to steal some ECU from your group. ",
                        fr=f"{self.subsession.num_of_takers} joueur Rouge a décidé de voler des ECU à votre groupe. ",
                        vi=f"{self.subsession.num_of_takers} người chơi Đỏ đã quyết định lấy cắp một số ECU từ nhóm của bạn. "
                    ), lang)
                else:
                    txt_final += trans(dict(
                        en=f"{self.subsession.num_of_takers} Red Players have decided to steal some ECU from your group. ",
                        fr=f"{self.subsession.num_of_takers} joueurs Rouges ont décidé de voler des ECU à votre groupe. ",
                        vi=f"{self.subsession.num_of_takers} người chơi Đỏ đã quyết định lấy cắp một số ECU từ nhóm của bạn. "
                    ), lang)
            else:
                txt_final += trans(dict(
                    en="No Red Player has decided to steal ECU from your group. ",
                    fr="Aucun joueur Rouge n'a décidé de voler des ECU à votre groupe. ",
                    vi="Không có người chơi Đỏ nào quyết định lấy cắp ECU từ nhóm của bạn. "
                ), lang)
            self.payoff_ecu = -self.subsession.num_of_takers * Config.STEALING_LOSS_INDIV

        game_payoff = self.payoff_ecu

        # -- payoff for norm (question society_opinion) ---
        txt_final += "<br>" + trans(dict(
            fr=f"A la question sur votre évaluation de l'opinion de la société, vous avez répondu "
               f"<i>{get_appropriate(lang)[self.society_opinion][1]}</i>. La majorité des participants a répondu "
               f"<i>{get_appropriate(lang)[self.subsession.society_opinion_majority][1]}</i>.",
            en=f"In the question on your assessment of the society's opinion, you have responded "
               f"<i>{get_appropriate(lang)[self.society_opinion][1]}</i>. The majority of participants have responded "
               f"<i>{get_appropriate(lang)[self.subsession.society_opinion_majority][1]}</i>.",
            vi=f"Trong câu hỏi về đánh giá của bạn về ý kiến của xã hội, bạn đã trả lời "
               f"<i>{get_appropriate(lang)[self.society_opinion][1]}</i>. Phần lớn người tham gia đã trả lời "
               f"<i>{get_appropriate(lang)[self.subsession.society_opinion_majority][1]}</i>."
        ), lang)

        norm_payoff = 0
        if self.society_opinion == self.subsession.society_opinion_majority:
            norm_payoff = Config.SOCIETY_OPTION_PAYOFF
            self.payoff_ecu += norm_payoff
            txt_final += " " + trans(dict(
                fr=f"Vous gagnez donc {Config.SOCIETY_OPTION_PAYOFF} ECU pour votre réponse.",
                en=f"You earn {Config.SOCIETY_OPTION_PAYOFF} ECU for your answer.",
                vi=f"Bạn kiếm được {Config.SOCIETY_OPTION_PAYOFF} ECU cho câu trả lời của mình.",
            ), lang)

        txt_final += "<br>" + trans(
            dict(
                en=f"Your payoff for part 2 of the experiment is {self.payoff_ecu} ECU "
                   f"(Game: {game_payoff} ECU + Opinion: {norm_payoff} ECU).",
                fr=f"Votre gain pour la partie 2 de l'expérience est de {self.payoff_ecu} ECU "
                   f"(Jeu : {game_payoff} ECU + Opinion : {norm_payoff} ECU).",
                vi=f"Khoản thanh toán của bạn cho phần 2 của thí nghiệm là {self.payoff_ecu} ECU "
                   f"(Trò chơi: {game_payoff} ECU + Ý kiến: {norm_payoff} ECU).",
            ), lang)

        self.participant.vars[app_name] = dict(
            txt_final=txt_final,
            payoff_ecu=self.payoff_ecu,
            payoff=self.payoff_ecu * self.session.config["real_world_currency_per_point"]
        )


# ======================================================================================================================
#
# -- PAGES --
#
# ======================================================================================================================

class MyPage(Page):
    @staticmethod
    def vars_for_template(player: Player):
        lang = player.session.vars["lang"]
        return dict(
            instructions_template_path="whistleblowing_game/InstructionsTemplate.html",
            instructions_template_title=trans(dict(
                en="Part 2 - Instructions",
                fr="Partie 2 - Instructions",
                vi="Phần 2 - Hướng dẫn"
            ), lang),
            instructions_wait_text=trans(dict(
                en="Waiting for the other participants.",
                fr="En attente des autres participants.",
                vi="Đang chờ các người tham gia khác."
            ), lang),
            **player.session.vars["lang_dict"],
            **Config.get_parameters()
        )

    @staticmethod
    def js_vars(player: Player):
        return dict(
            fill_auto=player.session.config.get("fill_auto", False),
            **Config.get_parameters(),
            **player.session.vars["lang_dict"],
        )


class Instructions(MyPage):
    template_name = "whistleblowing_commons/templates/Instructions.html"


class InstructionsWaitMonitor(MyPage):
    template_name = "global/InstructionsWaitMonitor.html"

    @staticmethod
    def is_displayed(player):
        return Instructions.is_displayed(player)


class InstructionsWaitForAll(WaitPage):
    wait_for_all_groups = True
    template_name = "global/InstructionsWaitPage.html"

    @staticmethod
    def vars_for_template(player):
        existing = MyPage.vars_for_template(player)
        existing.update(
            body_text=trans(dict(
                en="Waiting for the other participants.",
                fr="En attente des autres participants.",
                vi="Đang chờ những người tham gia khác."
            ), player.session.vars["lang"])
        )
        return existing


class Understanding(MyPage):
    form_model = "player"
    form_fields = [f"game_q{i}_faults" for i in range(1, 5)]
    template_name = "whistleblowing_commons/templates/Understanding.html"

    @staticmethod
    def vars_for_template(player: Player):
        existing = MyPage.vars_for_template(player)
        parameters = Config.get_parameters()
        parameters.update(reward=player.subsession.reward)
        existing.update(understanding=understanding.get_understanding(parameters, player.session.vars["lang"]))
        return existing

    @staticmethod
    def js_vars(player: Player):
        existing = MyPage.js_vars(player)
        existing["understanding"] = Understanding.vars_for_template(player)["understanding"]
        return existing

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.participant._is_bot = True
            for i in range(1, 5):
                setattr(player, f"game_q{i}_faults", random.randint(0, 2))
        player.game_total_faults = sum(
            getattr(player, f"game_q{i}_faults") for i in range(1, 5)
        )


class UnderstandingWaitForAll(WaitPage):
    wait_for_all_groups = True


class GroupRole(MyPage):
    pass


class DecisionTaking(MyPage):
    form_model = "player"
    form_fields = ["taking_decision"]

    @staticmethod
    def is_displayed(player):
        return player.group.active and player.taker

    @staticmethod
    def vars_for_template(player: Player):
        existing = MyPage.vars_for_template(player)
        existing.update(fields_labels=Lexicon.get_fields_labels(["taking_decision"], player.session.vars["lang"]))
        return existing

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.participant._is_bot = True
            player.taking_decision = random.choice([True, False])
        player.group.taker_has_taken = player.taking_decision


class EstimationReportingByTaker(MyPage):
    form_model = "player"
    form_fields = ["estimation_reporting"]

    @staticmethod
    def is_displayed(player: Player):
        return player.group.active and player.taker

    @staticmethod
    def vars_for_template(player: Player):
        existing = MyPage.vars_for_template(player)
        existing.update(fields_labels=Lexicon.get_fields_labels(["estimation_reporting"], player.session.vars["lang"]))
        return existing

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.participant._is_bot = True
            player.estimation_reporting = random.randint(0, 100)


class DecisionReporting(MyPage):
    form_model = "player"
    form_fields = ["reporting_decision"]

    @staticmethod
    def is_displayed(player):
        return player.group.active and not player.taker

    @staticmethod
    def vars_for_template(player: Player):
        existing = MyPage.vars_for_template(player)
        existing.update(fields_labels=Lexicon.get_fields_labels(["reporting_decision"], player.session.vars["lang"]))
        return existing

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.participant._is_bot = True
            player.reporting_decision = random.choice([True, False])


class Questionnaire(MyPage):
    form_model = "player"

    @staticmethod
    def get_form_fields(player: Player):
        fields = []
        if player.group.active:
            if player.taker:
                fields.append("taker_motivation")
            else:
                fields.append("reporter_motivation")
        fields.extend(["personal_opinion", "society_opinion"])
        return fields

    @staticmethod
    def vars_for_template(player: Player):
        existing = MyPage.vars_for_template(player)
        fields = Questionnaire.get_form_fields(player)
        existing.update(fields_labels=Lexicon.get_fields_labels(fields, player.session.vars["lang"]))
        return existing

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.participant._is_bot = True
            fields = Questionnaire.get_form_fields(player)
            if "taker_motivation" in fields:
                player.taker_motivation = "Explanation for stealing decision"
            if "reporter_motivation" in fields:
                player.reporter_motivation = "Explanation for reporting decision"
            player.personal_opinion = random.randint(0, 5)
            player.society_opinion = random.randint(0, 5)


class BeforeFinalWaitForAll(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession: Subsession):
        subsession.compute_payoffs()


class Final(MyPage):
    pass


page_sequence = [
    Instructions, InstructionsWaitForAll,
    # InstructionsWaitMonitor,
    Understanding, UnderstandingWaitForAll,
    GroupRole,
    DecisionTaking, EstimationReportingByTaker,
    DecisionReporting,
    Questionnaire,
    BeforeFinalWaitForAll, Final,
]
