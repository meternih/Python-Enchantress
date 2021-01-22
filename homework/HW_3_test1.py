import unittest
from homework.tests_simple_employee import Employee


class TestSimpleEmployee(unittest.TestCase):

    def setUp(self) -> None:
        self.employee = Employee("Thor", "Odinson", 2000)

    def test_email(self):
        self.assertEqual(self.employee.email, "Thor.Odinson@gmail.com")

    def test_fullname(self):
        self.assertEqual(self.employee.fullname, "Thor Odinson")

    def test_apply_raise(self):
        self.employee.apply_raise()
        self.assertEqual(self.employee.pay, 2000)

    # def test_monthly_schedule(self):
    #     pass


if __name__ == "__main__":
    unittest.main()
