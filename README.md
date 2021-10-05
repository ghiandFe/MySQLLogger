## MySQLLogger
###### A simple logger class for MySQL and MariaDB
##

##### Installation
```sh
$ pip install mysql-logger
```

##### Usage example
```py
from mysql_logger import MySQLLogger

# DB must be created before
db_settings = {
    'user': 'username',
    'password': 'Pa55w0rd',
    'host': 'localhost',
    'port': 3306,
    'database': 'my_log_db'
}

# Table will be automatically created (if not exists)
table_name = 'software_name'

# Initialize the logger
logger = MySQLLogger(db_settings, table_name)

# Log messages
logger.info('log info level message')
logger.error('log error level message')
```

##

##### Dependencies

* [asyncio](https://pypi.org/project/asyncio/) v3.4.3
* [aiomysql](https://pypi.org/project/aiomysql/) v0.0.21
* [PyMySQL](https://pypi.org/project/PyMySQL/) v0.9.3

##

##### Changes

v0.0.1 (2021-10-05)

* Initial release.
* Logger levels: debug, info, warning, error.