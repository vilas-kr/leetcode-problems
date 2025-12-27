import unittest
import unit_test
class TestDemo(unittest.TestCase):
    
    def test_name(self):
        self.assertEqual(unit_test.check_name(), True)
        
        with self.assertRaises(ValueError):
            unit_test.check_name("Vil")
        
if __name__ == "__main__":
    unittest.main()