import aiosqlite
from config import DB_PATH
from logger import logger
from models import OperationRequest

CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS operations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    operation TEXT NOT NULL,
    input TEXT NOT NULL,
    result TEXT NOT NULL,
    timestamp TEXT NOT NULL
)
"""

INSERT_OPERATION_QUERY = """
INSERT INTO operations (operation, input, result, timestamp)
VALUES (?, ?, ?, ?)
"""

GET_LAST_RESULT_QUERY = """
SELECT result, timestamp FROM operations
WHERE operation = ? AND input = ?
ORDER BY timestamp DESC
LIMIT 1
"""

class Database:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path

    async def initialize(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(CREATE_TABLE_QUERY)
            await db.commit()
            logger.info("Baza de date a fost initializata.")

    async def insert_operation(self, op: OperationRequest):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                INSERT_OPERATION_QUERY,
                (op.operation, op.input, op.result, op.timestamp.isoformat())
            )
            await db.commit()
            logger.debug(f"Operatie salvata in DB: {op}")

    async def get_last_result(self, operation: str, input_str: str) -> str:
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute(GET_LAST_RESULT_QUERY, (operation, input_str)) as cursor:
                row = await cursor.fetchone()
                if row:
                    result, timestamp = row
                    return f"Rezultat: {result} (salvat la {timestamp})"
                else:
                    return "Nu s-a gasit rezultatul."
