from otree.api import *

doc = """
Welcome App
"""


class C(BaseConstants):
    NAME_IN_URL = 'whwel'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1

    ENDOWMENT = 75


class Subsession(BaseSubsession):
    country = models.StringField()
    language = models.StringField()
    treatment = models.StringField()


def creating_session(subsession: Subsession):
    subsession.country = subsession.session.config.get("country", "France")
    # language
    lang_code = subsession.session.config.get("language", "en")
    subsession.language = lang_code
    subsession.session.vars["lang"] = lang_code
    lang_dict = dict(en=lang_code == "en", fr=lang_code == "fr", vi=lang_code == "vi")
    subsession.session.vars["lang_dict"] = lang_dict
    # treatment
    treat_code = subsession.session.config.get("treatment", "cooperation")
    subsession.treatment = treat_code
    subsession.session.vars["treatment"] = treat_code
    treat_dict = dict(cooperation=treat_code == "cooperation", individual=treat_code == "individual")
    subsession.session.vars["treatment_dict"] = treat_dict
    # groups
    subsession.group_randomly()
    subsession.session.vars["groups"] = subsession.get_group_matrix()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# =======================================================================================================================
#
# PAGES
#
# =======================================================================================================================
class MyPage(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(**player.session.vars["lang_dict"], **player.session.vars["treatment_dict"])

    @staticmethod
    def js_vars(player: Player):
        return dict(
            fill_auto=player.session.config.get("fill_auto", False),
        )


class Welcome(MyPage):
    pass


class Presentation(MyPage):
    pass


class Part1(MyPage):
    pass


page_sequence = [Welcome, Presentation, Part1]
