import os

if os.getenv('DJ_ENV') == 'prod':
    from .prod import *
else:
    from .dev import *
