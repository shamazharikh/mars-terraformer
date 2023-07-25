"""
Loads Config Classes and loads them with data from YAML files
"""
from .data_config import MarsConfig

mars_config: MarsConfig = MarsConfig.from_yaml_file(
    "/workspaces/mars-terraformer/config/mar_config.yml"
)
