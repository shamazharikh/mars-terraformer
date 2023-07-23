"""Implementation of classes to handle behaviour of Cards"""
import typing

from dataclasses import dataclass
from environment.tags import TagType
from environment.resources import ResouceProduction


@dataclass
class BaseCard:
    """Base Class for define all properties of a card"""

    cost: int
    tags: typing.Optional[typing.List[TagType]]
    name: str
    production: typing.Optional[typing.List[ResouceProduction]]
