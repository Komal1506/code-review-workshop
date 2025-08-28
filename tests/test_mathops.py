import sys
import os

# Avoid E501: break long line manually if needed
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_path)

from src.mathops import multiply  # noqa: E402


def test_multiply_basic():
    assert multiply(4, 5) == 20
