from os import environ

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
USE_POINTS = False
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
DEMO_PAGE_INTRO_HTML = """ """
SECRET_KEY = '5249757042491'
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=5.00,
    fill_auto=False,
    test=False
)
DEBUG = False

LANGUAGE_CODE = 'EN'
REAL_WORLD_CURRENCY_CODE = 'VND'
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 2

SESSION_CONFIGS = [
    dict(
        name='whistleblowing_no_reward',
        display_name='Whistleblowing - No Reward',
        app_sequence=[
            'whistleblowing_welcome',
            'whistleblowing_counting', 'whistleblowing_maths', 'whistleblowing_sliders', 'whistleblowing_ios',
            'whistleblowing_transition', 'whistleblowing_game',
            'whistleblowing_questionnaires', 'climate_questionnaire',
            'whistleblowing_final'
        ],
        num_demo_participants=6,
        real_world_currency_per_point=0.1,
        participation_fee=5.00,
        country="Vietnam",
        language="vi",
        treatment='cooperation',
        reward=False,
        doc="<p class='text-warning fw-bold'>The minimum is 6 participants.</p>"
    ),
    dict(
        name='whistleblowing_with_reward',
        display_name="Whistleblowing - With Reward",
        app_sequence=[
            'whistleblowing_welcome',
            'whistleblowing_counting', 'whistleblowing_maths', 'whistleblowing_sliders', 'whistleblowing_ios',
            'whistleblowing_transition', 'whistleblowing_game',
            'whistleblowing_questionnaires', 'climate_questionnaire',
            'whistleblowing_final'
        ],
        num_demo_participants=6,
        real_world_currency_per_point=0.1,
        participation_fee=5.00,
        country="Vietnam",
        language="vi",
        treatment='cooperation',
        reward=True,
        doc="<p class='text-warning fw-bold'>The minimum is 6 participants.</p>"
    ),
    dict(
        name='whistleblowing_game_only',
        display_name="Whistleblowing - Game only - With Reward",
        app_sequence=['whistleblowing_game'],
        num_demo_participants=6,
        real_world_currency_per_point=0.1,
        participation_fee=5.00,
        country="Vietnam",
        language="vi",
        treatment='cooperation',
        reward=True,
        doc="<p class='text-warning fw-bold'>The minimum is 6 participants.</p>"
    ),

    dict(
        name="whistleblowing_questionnaire_only",
        display_name="Whistleblowing - Questionnaire Only",
        app_sequence=['whistleblowing_questionnaires'],
        num_demo_participants=6,
        real_world_currency_per_point=0.1,
        participation_fee=5.00,
        country="Vietnam",
        language="en",
        treatment='cooperation',
        reward=False,
        doc="<p class='text-warning fw-bold'>The minimum is 6 participants.</p>"
    ),
    dict(
        name="whistleblowing_climate_questionnaire_only",
        display_name="Whistleblowing - Climate Questionnaire Only",
        app_sequence=['climate_questionnaire'],
        num_demo_participants=6,
        real_world_currency_per_point=0.1,
        participation_fee=5.00,
        country="Vietnam",
        language="en",
        treatment='cooperation',
        reward=False,
        doc="<p class='text-warning fw-bold'>The minimum is 6 participants.</p>"
    )

]
