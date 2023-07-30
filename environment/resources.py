""" 
This module contains definitions of resource types available and 
a dataclass for denoting a resource production
"""
import typing
from dataclasses import dataclass
from enum import IntEnum


class ResourceType(IntEnum):
    """
    All resource types available
    """

    MEGACREDIT = 1
    STEEL = 2
    TITANIUM = 3
    PLANT = 4
    POWER = 5
    HEAT = 6


RESOURCE_LIST = [
    ResourceType.MEGACREDIT,
    ResourceType.STEEL,
    ResourceType.TITANIUM,
    ResourceType.PLANT,
    ResourceType.POWER,
    ResourceType.HEAT,
]


@dataclass
class ConditionalResource:
    """
    ResourceType that is conditioned on game state
    """

    counter_func: typing.Callable


@dataclass
class ResouceProduction:
    """
    Resource Production
    """

    resource_type: ResourceType
    value: typing.Union[int, ConditionalResource]
    is_global: bool
