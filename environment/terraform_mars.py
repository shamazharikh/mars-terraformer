import json
from pathlib import Path
from typing import Any, SupportsFloat

import gymnasium as gym
from gymnasium.

DATA_PATH = Path(__file__) / "data" / "terraformingmars"


class TerraformMars(gym.Env):
    metadata = {
        "render_modes": ["human", "rbg_array", "vector"],
        "render_fps": 4,
    }

    def __init__(self, render_mode=None, game_version="base", num_players=5):
        self.terraforming_rating = [20 for i in range(num_players)]
        self.render_mode = render_mode
        self.game_version = game_version

    def get_board(self, board_path: str):
        board_data = json.read(board_path)
        return board_data

    def render(self) -> None:
        pass

    def step(self):
        pass
