import unittest

from .services import get_output

class GetOutputTest(unittest.TestCase):
    def test_output_includes_build_number(self):
        output = get_output(10)
        self.assertTrue("10" in output)
