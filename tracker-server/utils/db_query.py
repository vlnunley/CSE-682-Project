from dataclasses import fields
from flask import jsonify, make_response
import psycopg
from psycopg.rows import class_row, dict_row
import logging
from time import sleep
#local
from .models import TrackerBaseModel

def get_db_connection(app_config) -> psycopg.Connection:
    # Setup connection parameters
    params = {
        "host": app_config.get("DBHOST", "postgresql"),
        "port": app_config.get("DBPORT", "5432"),
        "dbname": app_config.get("DATABASE", "tracker"),
        "user": app_config.get("DBUSER", "postgres"),
        "password": app_config["DBPASS"]
    }

    return _connect_with_retry(params)

def _connect_with_retry(params) -> psycopg.Connection:
    attempts = 3
    while attempts > 0:
        attempts -= 1
        try:
            return psycopg.connect(**params, row_factory=dict_row)
        except psycopg.Error as exc:
            if attempts == 0:
                raise exc from None
            logging.exception(
                "Failed to connect to %s/%s (%d attempts remaining, waiting 10s):",
                params["host"],
                params["dbname"],
                attempts,
                exc_info=exc
            )
            sleep(10)
        except Exception as exc:
            logging.exception(
                "Failed to connect to %s/%s ",
                params["host"],
                params["dbname"],
                attempts,
                exc_info=exc
            )
            raise exc from None

def fetch_all_model_data(db: psycopg.Connection, cls: type[TrackerBaseModel]) -> list[type[TrackerBaseModel]]:
    sql = f"SELECT * FROM {cls.TABLE}"
    with db.cursor(row_factory=class_row(cls)) as cur:
        cur.execute(sql)
        rows = cur.fetchall()
        results = [obj_to_dict(row) for row in rows]
        return results
    
def fetch_model_data_by_id(db: psycopg.Connection, cls: type[TrackerBaseModel], row_ids: list[id]) -> list[type[TrackerBaseModel]] :
    sql = f"SELECT * FROM {cls.TABLE} where id = ANY(%s)"
    with db.cursor(row_factory=class_row(cls)) as cur:
        cur.execute(sql, (row_ids,))
        rows = cur.fetchall()
        results = [obj_to_dict(row) for row in rows]
        ret = {
            "success": True,
            "data": results,
            "error": None 
        }
        return ret
    
def update_model(db: psycopg.Connection, instance: TrackerBaseModel, row_id: int) -> None:
    cols = [f.name for f in fields(instance) if f.name != "id"]
    sql = f"UPDATE {instance.TABLE} set {','.join(['%s=%%s' % c for c in cols])} WHERE id = %s"
    with db.curser() as cur:
        cur.execute(sql, tuple([getattr(instance, c) for c in cols] + [row_id]))
        if cur.rowcount == 0:
            raise KeyError(f"No row with id={row_id} exists")
        db.commit()

def create_model(db: psycopg.Connection, instance: TrackerBaseModel) -> type[TrackerBaseModel]:
    try:
        cols = [f.name for f in fields(instance) if f.name != "id"]
        sql = f"INSERT INTO {instance.TABLE} ({','.join(cols)}) VALUES ({','.join(len(cols)*['%s'])}) returning id"
        with db.cursor() as cur:
            cur.execute(sql, tuple([getattr(instance, c) for c in cols]))
            row_id = cur.fetchone()["id"]
            db.commit()
        return fetch_model_data_by_id(db, instance.__class__, [row_id])
    except Exception as exc:
        ret = {
            "success": False,
            "data": None,
            "error": str(exc) 
        }
        return ret


   

def delete_model(db: psycopg.Connection, cls: TrackerBaseModel, row_id: int) -> None:
    sql = f"DELETE FROM {cls.TABLE} WHERE id = %s"
    with db.cursor() as cur:
        cur.execute(sql, (row_id,))
        db.commit()
    
def obj_to_dict(obj):
    """Convert object to dict for jsonify."""
    return obj.__dict__.copy()