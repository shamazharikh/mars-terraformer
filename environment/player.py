"""
Module to define classes to track player information and behavior
"""
import typing

from resources import RESOURCE_LIST, ResourceProduction


class BasePlayer:
    """
    Base player class
    """

    def __init__(
        self,
        terraforming_rating: int,
        resource_productions_inits: typing.Optional[
            typing.Union[int, typing.List[int]]
        ],
        resource_inits: typing.Optional[typing.Union[int, typing.List[int]]],
    ):
        self.terraforming_rating = terraforming_rating
        if resource_productions_inits:
            if isinstance(resource_productions_inits, int):
                self.resource_production = {
                    r_type: ResourceProduction(
                        r_type, resource_productions_inits, is_global=False
                    )
                    for r_type in RESOURCE_LIST
                }
            elif isinstance(resource_productions_inits, list) and len(
                resource_productions_inits
            ) == len(RESOURCE_LIST):
                self.resource_production = {
                    r_type: ResourceProduction(r_type, r_init, is_global=False)
                    for r_type, r_init in zip(
                        RESOURCE_LIST, resource_productions_inits
                    )
                }
            else:
                raise ValueError("incorrect Player init")
        else:
            self.resource_production = [
                ResourceProduction(r_type, 0, is_global=False)
                for r_type in RESOURCE_LIST
            ]
        if resource_inits:
            if isinstance(resource_inits, int):
                self.resources = {
                    r_type: resource_inits for r_type in RESOURCE_LIST
                }
            elif isinstance(resource_inits, list) and len(
                resource_inits
            ) == len(RESOURCE_LIST):
                self.resources = {
                    r_type: r_init
                    for r_type, r_init in zip(RESOURCE_LIST, resource_inits)
                }
            else:
                raise ValueError("incorrect Player init")
        else:
            self.resources = {r_type: 0 for r_type in RESOURCE_LIST}
            
    
