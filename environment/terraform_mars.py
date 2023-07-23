import gymnasium as gym
import json
from pathlib import Path

DATA_PATH = Path(__file__) / "data" / "terraformingmars"


class TerraformMars(gym.Env):
    metadata = {
        "render_modes": ["human", "rbg_array", "vector"],
        "render_fps": 4,
    }

    def __init__(self, render_model=None, game_version="base", num_players=5):
        self.terraforming_rating = [20 for i in range(num_players)]

    def get_board(self, board_path):
        pass
