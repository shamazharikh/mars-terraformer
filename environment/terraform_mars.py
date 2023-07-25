"""
Defines the game environment
"""
import json
from pathlib import Path

import gymnasium as gym

DATA_PATH = Path(__file__) / "data" / "terraformingmars"


class TerraformMars(gym.Env):
    """
    Subclasses gym Env
    """

    metadata = {
        "render_modes": ["human", "rbg_array", "vector"],
        "render_fps": 4,
    }

    def __init__(self, render_mode=None, game_version="base", num_players=5):
        self.terraforming_rating = [20 for i in range(num_players)]
        self.render_mode = render_mode
        self.game_version = game_version

    def get_board(self, board_path: str):
        """
        Gets board data
        """
        board_data = json.load(board_path)
        return board_data

    def render(self) -> None:
        pass

    def step(self, action):
        pass
