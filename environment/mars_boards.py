"""
Defines class to load board data and present it to other modules
"""
import json
from pathlib import Path

from repo_config import mars_config


class BaseBoard:
    """
    Defines  the base board class
    """
    def __init__(self, board_name="base"):
        self.board_name = board_name
        self.board_path = Path(mars_config.board_config.dir_path) / f"{board_name}.json"
        with open(str(self.board_path), "r", encoding="utf-8") as f:
            self.board_data = json.load(f)
        print(self.board_data)
