from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.02, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [dict(name='experiment_100057735',
                        display_name='experiment 100057735',
                        num_demo_participants=1,
                        app_sequence=['Experiment_100057735_Introduction', 'Experiment_100057735_Task',
                                      'Experiment_100057735_Survey'],),
                   dict(name='experiment_100057735_T2',
                        display_name='experiment 100057735 T2',
                        num_demo_participants=1,
                        app_sequence=['Experiment_100057735_Introduction_T2', 'Experiment_100057735_Task',
                                      'Experiment_100057735_Survey'],),
                   dict(name='experiment_100057735_T1',
                        display_name='experiment 100057735 T1',
                        num_demo_participants=1,
                        app_sequence=['Experiment_100057735_Introduction_T1', 'Experiment_100057735_Task_T1',
                                      'Experiment_100057735_Survey_T1'],),
                    ]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = '6cy%#1l1)00c+^d!a$0q9lgwcmih%c^0f(*r11)3+lwvhrg#%g'

INSTALLED_APPS = ['otree']

