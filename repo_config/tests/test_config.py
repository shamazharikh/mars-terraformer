"""
Testing config functionality
"""
from repo_config import mars_config


def test_mars_config():
    """
    Print config dataclass
    """
    print(mars_config)

if __name__ == "__main__":
    test_mars_config()
