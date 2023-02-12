import pandas as pd
import os
import dotenv
import sqlalchemy


class PostgresDB:

    def __init__(self):
        pass

    @staticmethod
    def construct_connect_string():
        dotenv.load_dotenv()
        return 'postgresql://{}:{}@{}:{}/{}'.format(
            os.getenv("DB.USER"),
            os.getenv("DB.PASSWORD"),
            os.getenv("DB.HOST"),
            os.getenv("DB.PORT"),
            os.getenv("DB.DATABASE"))

    @staticmethod
    def connect_string():
        return 'postgresql://{}:{}@{}:{}/{}' \
            .format('postgres',
                    'Te8JIdo$3mwFdR!#o4On04',
                    'lobster.ckjdyxlcimmo.us-east-1.rds.amazonaws.com',
                    5432,
                    'lobster')

    @staticmethod
    def table_to_df(tbl_name):
        engine = sqlalchemy.create_engine(PostgresDB.connect_string())
        with engine.connect() as conn:
            df = pd.read_sql(tbl_name, conn)
        engine.dispose()
        return df

    @staticmethod
    def fetch_table_names():
        engine = sqlalchemy.create_engine(PostgresDB.connect_string())
        for table_name in engine.table_names():
            print(table_name)
        engine.dispose()

    @staticmethod
    def df_to_table(df, table_name):
        engine = sqlalchemy.create_engine(PostgresDB.connect_string())
        with engine.connect() as conn:
            df.columns.str.lower()
            df.to_sql(table_name, conn, index=False, if_exists='append')
        engine.dispose()

    @staticmethod
    def query_to_df(sql):
        engine = sqlalchemy.create_engine(PostgresDB.connect_string())
        with engine.connect() as conn:
            df = pd.read_sql(sql=sql, con=conn)
        engine.dispose()
        return df

    @staticmethod
    def drop_table(tbl_name):
        engine = sqlalchemy.create_engine(PostgresDB.connect_string())
        conn = engine.raw_connection()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS {};".format(tbl_name))
        conn.commit()
        cursor.close()
        engine.dispose()
        pass
