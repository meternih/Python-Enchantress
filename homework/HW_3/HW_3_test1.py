import unittest
from homework.tests_simple_employee import Employee
from unittest.mock import patch


class TestSimpleEmployee(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        self.employee = Employee("Thor", "Odinson", 2000)

    def test_email(self):
        self.assertEqual(self.employee.email, "Thor.Odinson@gmail.com")

    def test_fullname(self):
        self.assertEqual(self.employee.fullname, "Thor Odinson")

    def test_apply_raise(self):
        self.employee.apply_raise()
        self.assertEqual(self.employee.pay, 2500)

    def test_monthly_schedule(self):
        with patch('tests_simple_employee.requests.get') as mock_requests:
            mock_requests.return_value.ok = True
        self.assertNotEqual(self.employee.monthly_schedule('june'), 'Bad Response!')


if __name__ == "__main__":
    unittest.main()
