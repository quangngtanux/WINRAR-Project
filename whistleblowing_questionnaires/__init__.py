import random
from pathlib import Path

from otree.api import *

from .fields_labels_choices import *

doc = """
Questionnaires
"""
app_name = Path(__file__).parent.name


class C(BaseConstants):
    NAME_IN_URL = "whquest"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    if "lang" not in subsession.session.vars:
        lang = subsession.session.config.get("language", "en")
        subsession.session.vars["lang"] = lang
        subsession.session.vars["lang_dict"] = dict(en=lang == "en", fr=lang == "fr", vi=lang == "vi")


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # ----- questionnaire 1 -----
    fairness_1 = models.IntegerField(choices=relevant_likert(), widget=widgets.RadioSelect())
    fairness_2 = models.IntegerField(choices=relevant_likert(), widget=widgets.RadioSelect())
    fairness_3 = models.IntegerField(choices=agreement_likert(), widget=widgets.RadioSelect())
    loyalty_1 = models.IntegerField(choices=relevant_likert(), widget=widgets.RadioSelect())
    loyalty_2 = models.IntegerField(choices=relevant_likert(), widget=widgets.RadioSelect())
    loyalty_3 = models.IntegerField(choices=agreement_likert(), widget=widgets.RadioSelect())
    morally_good_person = models.IntegerField(choices=[], widget=widgets.RadioSelect())
    friend_choice = models.IntegerField(choices=[], widget=widgets.RadioSelect())
    # ----- questionnaire 2 -----
    share_friend_stranger = models.IntegerField(min=0, max=1000)
    # ----- demographics -----
    age = models.IntegerField(choices=range(16, 121))
    gender = models.StringField(choices=[], widget=widgets.RadioSelect())
    highest_diploma = models.IntegerField(choices=[], widget=widgets.RadioSelect())


# ======================================================================================================================
#
# -- PAGES --
#
# ======================================================================================================================


class MyPage(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(**player.session.vars["lang_dict"])

    @staticmethod
    def js_vars(player: Player):
        return dict(fill_auto=player.session.config.get("fill_auto", False))


class Questionnaire1(MyPage):
    form_model = "player"
    form_fields = ["fairness_1", "fairness_2", "loyalty_1", "loyalty_2", "fairness_3", "loyalty_3",
                   "morally_good_person", "friend_choice"]

    @staticmethod
    def vars_for_template(player: Player):
        existing = MyPage.vars_for_template(player)
        existing.update(fields_labels=Lexicon.get_fields_labels(
            ["fairness_1", "fairness_2", "loyalty_1", "loyalty_2", "fairness_3", "loyalty_3",
             "morally_good_person", "friend_choice"], player.session.vars["lang"]
        ))
        return existing

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.participant._is_bot = True
            fields = [field for field in Questionnaire1.form_fields
                      if "fairness" in field or "loyalty" in field]
            for field in fields:
                setattr(player, field, random.randint(0, 5))
            player.morally_good_person = random.randint(0, 1)
            player.friend_choice = random.randint(0, 1)


class Questionnaire2(MyPage):
    form_model = "player"
    form_fields = ["share_friend_stranger"]

    @staticmethod
    def vars_for_template(player: Player):
        existing = MyPage.vars_for_template(player)
        lang = player.session.vars["lang"]
        existing.update(fields_labels=Lexicon.get_fields_labels(["share_friend_stranger"], lang),
                        )
        return existing

    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            player.participant._is_bot = True
            player.share_friend_stranger = random.randint(0, 1000)


class Demographics(MyPage):
    form_model = "player"
    form_fields = ["gender", "age", "highest_diploma"]

    @staticmethod
    def vars_for_template(player: Player):
        existing = MyPage.vars_for_template(player)
        existing.update(fields_labels=Lexicon.get_fields_labels(
            ["gender", "age", "highest_diploma"], player.session.vars["lang"]))
        return existing

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.participant._is_bot = True
            player.gender = random.choice(["M", "F", "NB", "NSP"])
            player.age = random.randint(16, 120)
            player.highest_diploma = random.randint(0, 5)


page_sequence = [Questionnaire1, Questionnaire2, Demographics]
