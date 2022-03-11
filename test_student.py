"""
test_student.py
"""
import unittest
from student import Student


class TestStudent(unittest.TestCase):
    """
    Student class test
    """

    def test_full_name(self):
        """
        create an instance of the class in order
        to test it
        """
        student = Student('John', 'Doe')
        self.assertEqual(student.full_name, 'John Doe')
        # checking if full_name method returns correct

    def test_email(self):
        """
        test email
        """
        student = Student('John', 'Doe')
        self.assertEqual(student.email, 'john.doe@email.com')

    def test_alert_santa(self):
        """
        add student to Santa naughy list test
        """
        student = Student('John', 'Doe')
        student.alert_santa()

        self.assertTrue(student.naughty_list)


if __name__ == "__main__":
    unittest.main()
