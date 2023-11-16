"""
# The package/library imports required for the project
---
"""

from numpy import zeros

def create_empty_array(x: int, y: int):
    """Generates a numpy empty array object
    """

    empty_array = zeros(shape=(x, y))
    return empty_array

print(create_empty_array(30, 30))