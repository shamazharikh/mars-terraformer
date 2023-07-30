"""
Defines the game environment
"""
from pathlib import Path

import gymnasium as gym

from environment.mars_boards import BaseBoard
from environment.player import BasePlayer

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

        self.render_mode = render_mode
        self.game_version = game_version
        self.board = BaseBoard(self.game_version)
        self.players = [BasePlayer(terraforming_rating=20) for i in range(num_players)]
    
    def render(self) -> None:
        pass

    def step(self, action):
        pass
