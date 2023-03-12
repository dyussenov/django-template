LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'stat_time': {'format': '[%(asctime)s] %(message)s'},
        'verbose': {
            'format': 'LOG ({levelname}) {asctime} {filename} — {message}',
            'style': '{',
        },
    },
    'handlers': {
        'main_console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'stat_time',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['main_console'],
            'level': 'INFO',
        },
        'app': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}