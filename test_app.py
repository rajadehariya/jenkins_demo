import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)

if _name_ == '_main_':
    unittest.main()
