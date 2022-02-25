# ENVIRONMENT = 'local'
ENVIRONMENT = 'development'
# ENVIRONMENT = 'production'

DJANGO_SETTINGS_MODULE = 'config.settings.local'

if ENVIRONMENT == 'local':
    DJANGO_SETTINGS_MODULE = 'config.settings.local'
if ENVIRONMENT == 'development':
    DJANGO_SETTINGS_MODULE = 'config.settings.development'
if ENVIRONMENT == 'production':
    DJANGO_SETTINGS_MODULE = 'config.settings.production'
