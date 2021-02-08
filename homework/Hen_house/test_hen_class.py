import unittest
from Hen_class import HenHouse, ErrorTimesOfYear
from unittest.mock import patch


class TestHenHouse(unittest.TestCase):

    def setUp(self) -> None:
        self.hen_house = HenHouse(5)

    def test_init_with_less_than_min(self):
        with self.assertRaises(ValueError) as e:
            self.hen_house = HenHouse(3)

    def test_season(self, month, season):
        with patch('datatime.datetime') as datetime_mock:
            datetime_mock.today.return_value.month = month
            self.assertEqual(self.hen_house, season)


    def test_productivity_index(self):
        pass

    def test_get_eggs_daily(self):
        pass

    def test_get_max_count_for_soup(self):
        pass

    def test_food_price(self):
        pass