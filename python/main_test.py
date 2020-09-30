import pathlib
import unittest

from python.core_service import CoreService


class MainTest(unittest.TestCase):

    def test_readJson(self):
        self.assertEqual(CoreService
                         .read_json(
            pathlib.Path(__file__).parent / "resources/testclass.json"), "{\"alma\":3}")
        # self.assertEqual(6, 7)
        # self.assertEqual(main.read_json(""), {"alma" : 3})


if __name__ == '__main__':
    unittest.main()
