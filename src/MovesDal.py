import json
from typing import List
import psycopg2



class MovesDal():

    def __init__(self, config):
        self._conf = config


    __get_by_reference_query = """
        select
            m.reference,
            m."previousMove",
            m.payload,
            m.step_number
        from moves m
        where m.reference = %s and m.reference = %s"""


    __get_latest_query = """
        select
            m.reference,
            m."previousMove",
            m.payload,
            m.step_number
        from moves m
        left join moves newer_m on newer_m.id > m.id
        where newer_m.id is null
        """

    def save(self, move):
        connection = self.__get_connection()
        cursor = connection.cursor()

        try:
            postgres_insert_query = """ INSERT INTO moves (reference, "previousMove", payload, step_number) VALUES (%s,%s,%s,%s)"""
            record_to_insert = (
                move["reference"], move["previousMove"], json.dumps(move), move["stepNumber"])
            cursor.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into moves table")

        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into moves table", error)
            raise error

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def get_previous_moves(self, move) -> List:
        connection = self.__get_connection()
        cursor = connection.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor)

        try:

            old_moves = []
            reference = move["previousMove"]
            while reference != None:
                reference_to_check = (reference, reference)
                cursor.execute(self.__get_by_reference_query, reference_to_check)
                db_move = cursor.fetchone()
                if db_move == None:
                    return []
                move = db_move["payload"]
                old_moves.insert(0, move)
                reference = db_move["previousMove"]

            print(len(old_moves), "moves fetched successfully.")
            return old_moves

        except (Exception, psycopg2.Error) as error:
            print("Failed to fetch chain of moves", error)
            raise error

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def get_latest_move(self):
        connection = self.__get_connection()
        cursor = connection.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor)

        try:

            cursor.execute(self.__get_latest_query)
            db_move = cursor.fetchone()
            if db_move == None:
                return None
            move = db_move["payload"]

            print("Latest move fetched successfully.")
            return move

        except (Exception, psycopg2.Error) as error:
            print("Failed to fetch chain of moves", error)
            raise error

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")


    def __get_connection(self):
        connection = psycopg2.connect(user=self._conf.db_user,
                                    password=self._conf.db_pass,
                                    host=self._conf.db_host,
                                    port=self._conf.db_port,
                                    database=self._conf.db_name)
        return connection
