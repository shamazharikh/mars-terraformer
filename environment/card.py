"""Implementation of classes to handle behaviour of Cards"""
import typing
from dataclasses import dataclass

from environment.resources import ResouceProduction
from environment.tags import TagType


@dataclass
class BaseCard:
    """Base Class for define all properties of a card"""

    cost: int
    tags: typing.Optional[typing.List[TagType]]
    name: str
    production: typing.Optional[typing.List[ResouceProduction]]
    victory_points: typing.Optional[int]
