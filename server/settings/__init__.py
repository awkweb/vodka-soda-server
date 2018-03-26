import os

if os.environ['DJ_DB_HOST'] == 'localhost':
    from .dev import *
else:
    from .prod import *
