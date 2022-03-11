"""
student.py
"""

from datetime import date, timedelta
# to allow us to define start and end date
import requests


class Student:
    """
    A Student class with properties and
    full_name method as a basis for method testing
    """
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        """
        full name method
        """
        return f"{self._first_name} {self._last_name}"

    @property
    def email(self):
        """
        email test
        """
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    def alert_santa(self):
        """
        alert santa
        """
        self.naughty_list = True

    def apply_extension(self, days):
        """
        student end date
        """
        self.end_date = self.end_date + timedelta(days=days)

    def course_schedule(self):
        """
        course schedule
        """
        response = requests.get(
            f"https://company.com/course-schedule/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong"
