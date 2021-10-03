import json
from typing import List
import psycopg2

from conf import conf


def __get_connection():
    connection = psycopg2.connect(user=conf.db_user,
                                  password=conf.db_pass,
                                  host=conf.db_host,
                                  port=conf.db_port,
                                  database=conf.db_name)
    return connection


def save(move):
    try:
        connection = __get_connection()
        cursor = connection.cursor()

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


__get_by_reference_query = """
select
    m.reference,
    m."previousMove",
    m.payload,
    m.step_number
from moves m
where m.reference = %s and m.reference = %s"""


def get_previous_moves(move) -> List:
    try:
        connection = __get_connection()
        cursor = connection.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor)

        old_moves = []
        reference = move["previousMove"]
        while reference != None:
            reference_to_check = (reference, reference)
            cursor.execute(__get_by_reference_query, reference_to_check)
            db_move = cursor.fetchone()
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


def get_latest_move():
    try:
        connection = __get_connection()
        cursor = connection.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor)

        cursor.execute(__get_latest_query)
        db_move = cursor.fetchone()
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
