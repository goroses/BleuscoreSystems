# test_bleuscore.py
"""
Tests for Bleuscore module.
"""

import unittest
from bleuscore import Bleuscore

class TestBleuscore(unittest.TestCase):
    """Test cases for Bleuscore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Bleuscore()
        self.assertIsInstance(instance, Bleuscore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Bleuscore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
