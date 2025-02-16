import os
import sqlite3
from typing import Any
from core.config import config


class SqliteConnector:
    def __init__(self):
        self.db_path = os.path.abspath(config.db_path.get_secret_value())

    async def db(self, query: str, fetchone: bool = True, fetchall: bool = False) -> Any:
        db = sqlite3.connect(self.db_path, check_same_thread=False, timeout=6)
        sql = db.cursor()
        try:
            if 'select' in query.lower():
                try:
                    if fetchall:
                        value = sql.execute(query).fetchall()
                    elif fetchone:
                        result = sql.execute(query).fetchone()
                        value = result[0] if result else None
                    else:
                        value = sql.execute(query).fetchone()
                except:
                    value = None
                return value
            else:
                sql.execute(query)
                db.commit()
                return True
        except:
            return None
        finally:
            sql.close()
            db.close()
