__author__ = 'Olushola Karokatose'

import os

config = {
    "database": {
        "sql": {
            "host": os.environ['DB_HOST'],
            "port": int(os.environ['DB_PORT']),
            "user": os.environ['DB_USER'],
            "pass": os.environ['DB_PASS'],
            "name": os.environ['DB_NAME']
        }
    },
    'app_port': os.environ['PORT'],
    'key': os.environ['KEY'],
    'version':'1.0'
}