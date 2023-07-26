"""
Loads Config Classes and loads them with data from YAML files
"""
from .data_config import MarsConfig

mars_config: MarsConfig = MarsConfig.from_yaml_file(
    "/app/repo_config/mars_config.yml"
)
