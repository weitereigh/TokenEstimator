# test_tokenestimator.py
"""
Tests for TokenEstimator module.
"""

import unittest
from tokenestimator import TokenEstimator

class TestTokenEstimator(unittest.TestCase):
    """Test cases for TokenEstimator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenEstimator()
        self.assertIsInstance(instance, TokenEstimator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenEstimator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
