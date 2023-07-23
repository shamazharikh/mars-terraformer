"""Enumerator for Tag types"""
from enum import IntEnum


class TagType(IntEnum):
    """Tag types available in the game"""
    ANIMAL = 1
    BUILDING = 2
    CITY = 3
    EARTH = 4
    EVENT = 5
    JOVIAN = 6
    MICROBE = 7
    PLANT = 8
    POWER = 9
    SCIENCE = 10
    SPACE = 11
