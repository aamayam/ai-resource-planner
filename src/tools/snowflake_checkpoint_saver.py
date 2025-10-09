import pickle
import json
import snowflake.connector
from typing import Optional, Dict, Any, Sequence, Tuple
from contextlib import contextmanager
from langgraph.checkpoint.base import (
    BaseCheckpointSaver,
    Checkpoint,
    CheckpointMetadata,
    CheckpointTuple
)

class SnowflakeCheckpointSaver(BaseCheckpointSaver):
    def __init__(
        self,
        account: str,
        user: str,
        password: str,
        warehouse: str,
        database: str,
        schema: str,
        table_name: str = "langgraph_checkpoints",
        **kwargs
    ):
        super().__init__()
        self.connection_params = {
            "account": account,
            "user": user,
            "password": password,
            "warehouse": warehouse,
            "database": database,
            "schema": schema,
            **kwargs
        }
        self.table_name = table_name
        self._setup_table()
