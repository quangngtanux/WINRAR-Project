import random
from pathlib import Path

from otree.api import *

from whistleblowing_commons.functions import trans

doc = """
Questionnaires
"""
app_name = Path(__file__).parent.name


def relevant_likert(lang="en"):
    return [
        (0, trans(dict(
            en="not at all relevant (this consideration has nothing to do with my judgments of right or wrong)",
            fr="pas du tout pertinent (cette considération n'a rien à voir avec mes jugements de bien ou de mal)",
            vi="không liên quan gì cả (cân nhắc này không liên quan gì đến đánh giá đúng hay sai của tôi)"
        ), lang)),
        (1, trans(dict(en="not very relevant", fr="pas très pertinent", vi="không quá liên quan"), lang)),
        (2, trans(dict(en="slightly relevant", fr="légèrement pertinent", vi="hơi liên quan"), lang)),
        (3, trans(dict(en="somewhat relevant", fr="assez pertinent", vi="khá liên quan"), lang)),
        (4, trans(dict(en="very relevant", fr="très pertinent", vi="rất liên quan"), lang)),
        (5, trans(dict(en="extremely relevant", fr="extrêmement pertinent", vi="cực kỳ liên quan"), lang)),
    ]


def agreement_likert(lang="en"):
    return [
        (0, trans(dict(en="Strongly disagree", fr="Fortement en désaccord", vi="Hoàn toàn không đồng ý"), lang)),
        (1,
         trans(dict(en="Moderately disagree", fr="Modérément en désaccord", vi="Không đồng ý mức độ vừa phải"), lang)),
        (2, trans(dict(en="Slightly disagree", fr="Légèrement en désaccord", vi="Không đồng ý một chút"), lang)),
        (3, trans(dict(en="Slightly agree", fr="Légèrement d'accord", vi="Đồng ý một chút"), lang)),
        (4, trans(dict(en="Moderately agree", fr="Modérément d'accord", vi="Đồng ý mức độ vừa phải"), lang)),
        (5, trans(dict(en="Strongly agree", fr="Fortement d'accord", vi="Hoàn toàn đồng ý"), lang)),
    ]


class C(BaseConstants):
    NAME_IN_URL = "whquest"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


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


def fairness_1_choices(player):
    return relevant_likert(player.session.vars["lang"])


def fairness_2_choices(player):
    return relevant_likert(player.session.vars["lang"])


def fairness_3_choices(player):
    return agreement_likert(player.session.vars["lang"])


def loyalty_1_choices(player):
    return relevant_likert(player.session.vars["lang"])


def loyalty_2_choices(player):
    return relevant_likert(player.session.vars["lang"])


def loyalty_3_choices(player):
    return agreement_likert(player.session.vars["lang"])


def morally_good_person_choices(player):
    lang = player.session.vars["lang"]
    return [
        (1, trans(dict(
            en="Someone who is fair and just, impartial and unprejudiced",
            fr="Quelqu'un qui est juste et équitable, impartial et sans préjugés",
            vi="Ai đó công bằng và chính trực, không thiên vị và không định kiến"
        ), lang)),
        (0, trans(dict(
            en="Someone who is loyal and faithful, devoted and dependable",
            fr="Quelqu'un qui est loyal et fidèle, dévoué et fiable",
            vi="Ai đó trung thành và đáng tin cậy"
        ), lang)),
    ]


def friend_choice_choices(player):
    lang = player.session.vars["lang"]
    return [
        (1, trans(dict(
            en="Someone who is fair and just to others, who is impartial and unprejudiced regardless of "
               "how it affects their family and friends",
            fr="Quelqu'un qui est juste et équitable envers les autres, impartial et sans préjugés, même "
               "si cela affecte sa famille et ses amis",
            vi="Ai đó công bằng và chính trực với người khác, không thiên vị và không định kiến bất kể "
               "nó ảnh hưởng như thế nào đến gia đình và bạn bè của họ"
        ), lang)),
        (0, trans(dict(
            en="Someone who is loyal and faithful to their family and friends, who is devoted and "
               "dependable regardless of how it affects outsiders",
            fr="Quelqu'un qui est loyal et fidèle à sa famille et à ses amis, dévoué et fiable même si "
               "cela affecte des personnes extérieures",
            vi="Ai đó trung thành và đáng tin cậy với gia đình và bạn bè của họ, tận tâm và đáng tin cậy "
               "bất kể nó ảnh hưởng như thế nào đến người ngoài"
        ), lang))]


def gender_choices(player):
    lang = player.session.vars["lang"]
    return [
        ("F", trans(dict(en="Female", fr="Femme", vi="Nữ"), lang)),
        ("M", trans(dict(en="Male", fr="Male", vi="Nam"), lang)),
        ("NB", trans(dict(en="Non-binary", fr="Non binaire", vi="Không nhị phân"), lang)),
        ("NSP", trans(dict(en="Prefer no to say", fr="Ne souhaite pas répondre", vi="Không muốn nói"), lang)),
    ]


def highest_diploma_choices(player):
    lang = player.session.vars["lang"]
    return [
        (0,
         trans(dict(en="No formal education", fr="Aucune éducation formelle", vi="Không có giáo dục chính quy"), lang)),
        (1, trans(dict(en="Primary education", fr="Enseignement primaire", vi="Giáo dục tiểu học"), lang)),
        (2, trans(dict(en="Secondary education", fr="Enseignement secondaire", vi="Giáo dục trung học"), lang)),
        (3, trans(dict(en="Bachelor’s degree", fr="Licence", vi="Cử nhân"), lang)),
        (4, trans(dict(en="Master’s degree", fr="Master", vi="Thạc sĩ"), lang)),
        (5, trans(dict(en="Doctorate or higher", fr="Doctorat ou supérieur", vi="Tiến sĩ hoặc cao hơn"), lang)),
    ]


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
        lang = player.session.vars["lang"]
        fairness_1_label = trans(dict(
            en="... whether or not someone acted unfairly",
            fr="... si oui ou non quelqu'un a agi de manière injuste",
            vi="... liệu ai đó có hành xử không công bằng hay không"
        ), lang)
        fairness_2_label = trans(dict(
            en="... whether or not someone was denied his or her rights",
            fr="... si oui ou non quelqu'un a renié à ses droits",
            vi="... liệu ai đó có bị từ chối quyền lợi của mình hay không"
        ), lang)
        fairness_3_label = trans(dict(
            en="Justice is the most important requirement for a society",
            fr="La justice est primordiale pour une société",
            vi="Công lý là yêu cầu quan trọng nhất đối với một xã hội"
        ), lang)
        loyalty_1_label = trans(dict(
            en="... whether or not someone did something to betray his or her group",
            fr="... si oui ou non quelqu'un a fait quelque chose pour trahir son groupe",
            vi="... liệu ai đó có làm điều gì đó để phản bội nhóm của mình hay không"
        ), lang)
        loyalty_2_label = trans(dict(
            en="... whether or not someone showed a lack of loyalty",
            fr="... si oui ou non quelqu'un a fait preuve d'un manque de loyauté",
            vi="... liệu ai đó có thể hiện sự thiếu trung thành hay không"
        ), lang)
        loyalty_3_label = trans(dict(
            en="People should be loyal to their family members, even when they have done something wrong",
            fr="Les gens doivent être loyaux avec les membres de leur famille, même lorsqu'ils ont fait quelque "
               "chose de mal",
            vi="Mọi người nên trung thành với các thành viên trong gia đình, ngay cả khi họ đã làm điều gì đó sai trái"
        ), lang)
        morally_good_person_label = trans(dict(
            en="Objectively speaking, who do you think is the more morally good person?",
            fr="Objectivement parlant, qui est la personne la plus morale selon toi ?",
            vi="Nói một cách khách quan, bạn nghĩ ai là người có đạo đức hơn?"
        ), lang)
        friend_choice = trans(dict(
            en="Who would you rather be friends with?",
            fr="Avec qui préféreriez-vous être ami(e) ?",
            vi="Bạn muốn làm bạn với ai hơn?"
        ), lang)
        fields_labels = dict(
            fairness_1=fairness_1_label,
            fairness_2=fairness_2_label,
            fairness_3=fairness_3_label,
            loyalty_1=loyalty_1_label,
            loyalty_2=loyalty_2_label,
            loyalty_3=loyalty_3_label,
            morally_good_person=morally_good_person_label,
            friend_choice=friend_choice,
        )
        existing.update(fields_labels=fields_labels)
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
        share_friend_stranger_label = trans(dict(
            en=f"How much of your {cu(1000)} would you give to your friend, if the rest goes to a "
               "random stranger from your country?",
            fr=f"Sur vos {cu(1000)}, combien donneriez-vous à votre ami(e), si le reste allait à un(e) "
               f"inconnu(e) pris(e) au hasard dans votre pays ?",
            vi=f"Bạn sẽ cho bạn của mình bao nhiêu trong số {cu(1000)} của bạn, nếu phần còn lại sẽ "
               "đi đến một người lạ ngẫu nhiên từ đất nước của bạn?"
        ), lang)
        fields_labels = dict(
            share_friend_stranger=share_friend_stranger_label,
        )
        existing.update(fields_labels=fields_labels)
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
        lang = player.session.vars["lang"]
        gender_label = trans(dict(
            en="What is your gender?",
            fr="Quel est votre genre ?",
            vi="Giới tính của bạn là gì?"
        ), lang)
        age_label = trans(dict(
            en="What is your age?",
            fr="Quel est votre âge ?",
            vi="Tuổi của bạn là bao nhiêu?"
        ), lang)
        highest_diploma_label = trans(dict(
            en="What is the highest level of education you have completed?",
            fr="Quel est le niveau d'études le plus élevé que vous ayez terminé ?",
            vi="Trình độ học vấn cao nhất bạn đã hoàn thành là gì?"
        ), lang)
        fields_labels = dict(
            gender=gender_label,
            age=age_label,
            highest_diploma=highest_diploma_label,
        )
        existing.update(fields_labels=fields_labels)
        return existing

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.participant._is_bot = True
            player.gender = random.choice(["M", "F", "NB", "NSP"])
            player.age = random.randint(16, 120)
            player.highest_diploma = random.randint(0, 5)


page_sequence = [Questionnaire1, Questionnaire2, Demographics]
