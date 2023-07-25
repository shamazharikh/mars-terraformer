"""
class defines config dataclasses that can load yaml files and load config variables
"""

from dataclasses import dataclass

from dataclass_wizard import YAMLWizard


@dataclass
class BoardConfig:
    """
    Define config variables dealing with board data
    """

    dir_path: str


@dataclass
class MarsConfig(YAMLWizard):
    """
    Define config variables for the terraforming mars game
    """

    board_config: BoardConfig
