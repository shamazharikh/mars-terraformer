""" 
This module contains definitions of resource types available and 
a dataclass for denoting a resource production
"""
from enum import IntEnum
from dataclasses import dataclass


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


@dataclass
class ResouceProduction:
    """
    Resource Production
    """

    resource_type: ResourceType
    value: int
    is_global: bool
