"""
Module to define classes to track player information and behaviour
"""
import typing

from resources import ResouceProduction, ResourceType


class BasePlayer:
    """
    Base player class
    """
    def __init__(self, terraforming_rating: int, resource_productions: typing.Optional[typing.Union[int, typing.List[int]]] , resources: typing.Optional[typing.Union[int, typing.List[int]]]):  
        self.terraforming_rating = terraforming_rating
        
        resource_production: typing.List[ResouceProduction]
        resources: typing.Dict[ResourceType, int]

 