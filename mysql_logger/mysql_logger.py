from aiomysql import connect as async_connect
from asyncio import get_event_loop


class MySQLLogger:
    def __init__(self, db, sw):
        """
        Initialize DB Connection
        db: dict -> {
            'user': 'username',
            'password': 'Pa55w0rd',
            'host': 'localhost',
            'port': 3306,
            'database': 'my_log_db'
        }
        sw: str -> Software name to identified (or create) the db table
        """

        self.db = db
        self.sw = sw.replace(' ', '_')
        self.__createTable()

    async def __execute(self, loop, query, args=None):
        conn = await async_connect(
            user = self.db['user'],
            password = self.db['password'],
            host = self.db['host'],
            port = self.db['port'],
            db = self.db['database'],
            loop = loop
        )
        async with conn.cursor() as cur:
            if args:
                await cur.execute(query, args)
            else:
                await cur.execute(query)
        await conn.commit()
        conn.close()

    def __asyncRun(self, query, args=None):
        loop = get_event_loop()
        loop.run_until_complete(self.__execute(loop, query, args))

    def __createTable(self):
        query = f'''
        CREATE TABLE IF NOT EXISTS {self.db["database"]}.{self.sw} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            level VARCHAR(30),
            text TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP()
        );
        '''
        self.__asyncRun(query)
        # loop = get_event_loop()
        # loop.run_until_complete(self.__execute(loop, query))

    def __insert(self, text, level):
        query = f'''
        INSERT INTO {self.db["database"]}.{self.sw} (level, text)
        VALUES (%s, %s);
        '''
        args = (level, text)
        self.__asyncRun(query, args)
        # loop = get_event_loop()
        # loop.run_until_complete(self.__execute(loop, query, args))

    def info(self, text):
        self.__insert(text, 'info')

    def debug(self, text):
        self.__insert(text, 'debug')

    def error(self, text):
        self.__insert(text, 'error')

    def warning(self, text):
        self.__insert(text, 'warning')

