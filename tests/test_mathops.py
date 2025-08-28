import sys
import os

# E402 fix: Keep all imports at the top
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.mathops import multiply


# E302 fix: Add two blank lines before function
def test_multiply_basic():
    assert multiply(4, 5) == 20
