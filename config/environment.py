from decouple import config

ENVIRONMENT = config("ENVIRONMENT")

if ENVIRONMENT == 'local':
    SETTINGS_MODULE = 'config.settings.local'
elif ENVIRONMENT == 'development':
    SETTINGS_MODULE = 'config.settings.development'
elif ENVIRONMENT == 'production':
    SETTINGS_MODULE = 'config.settings.production'
elif ENVIRONMENT == 'ci':
    SETTINGS_MODULE = 'config.settings.ci'
else:
    raise ValueError(f"Unknown ENVIRONMENT: {ENVIRONMENT}")
