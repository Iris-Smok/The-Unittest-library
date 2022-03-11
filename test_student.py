"""
test_student.py
"""
import unittest
from datetime import timedelta
from unittest.mock import patch
from student import Student


class TestStudent(unittest.TestCase):
    """
    Student class test
    """
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')

    def tearDown(self):
        print('tearDown')

    def test_full_name(self):
        """
        create an instance of the class in order
        to test it
        """
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')
        # checking if full_name method returns correct

    def test_email(self):
        """
        test email
        """
        print('test_email')
        self.assertEqual(self.student.email, 'john.doe@email.com')

    def test_alert_santa(self):
        """
        add student to Santa naughy list test
        """
        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_apply_extension(self):
        """
        student end date
        """
        old_end_date = self.student.end_date
        self.student.apply_extension(5)

        self.assertEqual(self.student.end_date, old_end_date +
                         timedelta(days=5))

    def test_course_schedule_failed(self):
        """
        In the path "student" comes from the name of the file student.py
        If you have named the file something else - it will need to match
        eg, students.py would need "students.requests.get"
        """
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong")
            

if __name__ == "__main__":
    unittest.main()
