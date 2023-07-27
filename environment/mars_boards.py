"""
Defines class to load board data and present it to other modules
"""
import json
import typing
from pathlib import Path

from environment.resources import ResourceType
from repo_config import mars_config


class BaseBoard:
    """
    Defines  the base board class
    """

    def __init__(self, board_name="base"):
        self.board_name = board_name
        self.board_path = (
            Path(mars_config.board_config.dir_path) / f"{board_name}.json"
        )
        with open(str(self.board_path), "r", encoding="utf-8") as f:
            self.board_data = json.load(f)
        print(self.board_data.keys())
        assert "board" in self.board_data

    def print_board(self):
        tile_data: typing.List[typing.List[str]] = self.board_data["board"]
        for row_idx, board_row in enumerate(tile_data):
            row_str = []
            for tile in board_row:
                if tile == "0":
                    row_str.append("..")
                elif ":" in tile:
                    row_str.append(tile.split(":")[1][0])
                else:
                    row_str.append(tile[0])
            if row_idx % 2:
                print("".join([f"..{i}" for i in row_str]))
            else:
                print("".join([f"{i}.." for i in row_str]))
