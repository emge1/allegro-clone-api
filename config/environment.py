from decouple import config

ENVIRONMENT = config("ENVIRONMENT")

if ENVIRONMENT == 'local':
    SETTINGS_MODULE = 'config.settings.local'
elif ENVIRONMENT == 'development':
    SETTINGS_MODULE = 'config.settings.development'
elif ENVIRONMENT == 'production':
    SETTINGS_MODULE = 'config.settings.production'
else:
    raise ValueError(f"Unknown ENVIRONMENT: {ENVIRONMENT}")
