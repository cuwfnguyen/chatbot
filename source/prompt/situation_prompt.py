import psycopg2
from psycopg2 import pool
from psycopg2.extras import DictCursor
import logging

connection_pool = pool.ThreadedConnectionPool(
    1,
    20,
    host='192.168.12.55',
    port='5432',
    database='chatbot_db',
    user='chatbot_user',
    password='cunx4869'
)

def get_db_connection():
    return connection_pool.getconn()

def release_db_connection(conn):
    connection_pool.putconn(conn)

def execute_query(query, params=None):
    conn = get_db_connection()
    try:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(query, params)
            conn.commit()
            results = cur.fetchall()
            return [dict(row) for row in results]
    except psycopg2.Error as e:
        conn.rollback()
        logging.info(f"Database error: {e}")
        raise
    finally:
        release_db_connection(conn)


def get_agent_prompt(agent_code):
    query = f"select agent_prompt from intent_prompt where agent_code = {agent_code}"
    data = execute_query(query)
    return data
