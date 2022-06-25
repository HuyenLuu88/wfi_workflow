from .base import *
# you need to set "DJANGO_SETTINGS_MODULE = 'wfi_workflow.settings.prod'" as an environment variable
# in your OS (on which your website is hosted)
if os.environ['DJANGO_SETTINGS_MODULE'] == 'wfi_workflow.settings.prod':
    from .prod import *
else:
    from .dev import *


