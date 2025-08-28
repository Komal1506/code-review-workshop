import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.mathops import multiply

def test_multiply_basic():
    assert multiply(4, 5) == 20
