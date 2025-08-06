# test_strapicms.py
"""
Tests for StrapiCms module.
"""

import unittest
from strapicms import StrapiCms

class TestStrapiCms(unittest.TestCase):
    """Test cases for StrapiCms class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StrapiCms()
        self.assertIsInstance(instance, StrapiCms)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StrapiCms()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
