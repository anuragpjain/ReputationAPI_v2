import psycopg2
import psycopg2.extensions

from logger import RepLogger

"""This class is related to db config which rerturn the db object  and run th query on db"""
class connection_cls(dict):

    def __init__(self, host=None, port=None, dbname=None, username=None, password=None):
        self.host = host
        self.dbname = dbname
        self.username = username
        self.password = password
        self.port = port
        self.logged = RepLogger()

    def connet_to_postgresdb(self):
        try:
            postgres_conn = psycopg2.connect(host=self.host,
                                             dbname=self.dbname,
                                             port=self.port,
                                             user=self.username,
                                             password=self.password)
            print("Connected to postgres")
            return postgres_conn
        except psycopg2.Error as e:
            self.logged.error('error in Postgres databse connection')
            self.logged.error(e)

    def excute_sql_on_postgresdb(self, obj_con_postgres, sqlquery):
        cur = obj_con_postgres.cursor();
        try:
            cur.execute(sqlquery)
            response = cur.fetchone();
            self.logged.info('query is executed on postgres:' + sqlquery)
            cur.close()
            return response
        except psycopg2.Error as e:
            self.logged.error(e)
