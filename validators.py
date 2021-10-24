import datetime
import re
from exceptions import PasswordError


class BaseValidator:
    def __init__(self, text):
        self.text = text

    def validate(self) -> bool:
        return True if self.text else False


class DateValidator(BaseValidator):
    def __init__(self, datetime_timestamp: int):
        self.datetime_timestamp = datetime.datetime.fromtimestamp(datetime_timestamp)
        super().__init__(datetime_timestamp)

    def validate(self) -> bool:
        if self.datetime_timestamp > datetime.datetime.now():
            return False

        return True


class PasswordValidator(BaseValidator):
    def __init__(self, password):
        self.password = password
        super().__init__(password)

    def _check_password_len(self):
        return not len(self.password) <= 8

    def _check_digits_in_password(self):
        for letter in self.password:
            if letter.isdigit():
                return True
        else:
            return False

    def _check_upper_and_lower_case_in_password(self):
        upper_count = 0
        lower_count = 0

        for letter in self.password:
            if letter.isupper():
                upper_count += 1
            elif letter.islower():
                lower_count += 1

            if upper_count >= 1 and lower_count >= 1:
                return True
        else:
            return False

    @staticmethod
    def _rplce_lttr_to_anthr_lttr_in_kbrd(password, first_row, second_row):
        new_password = ''

        for letter in password.lower():
            for keyboard_row_index in range(len(first_row)):
                if letter in first_row[keyboard_row_index]:
                    letter_index = first_row[keyboard_row_index].index(letter)
                    letter = second_row[keyboard_row_index][letter_index]
                    new_password += letter
                    break
            else:
                new_password += letter

        return new_password

    def validate(self) -> bool:
        try:
            if not self._check_password_len():
                raise PasswordError()

            if not self._check_upper_and_lower_case_in_password():
                raise PasswordError()

            if not self._check_digits_in_password():
                raise PasswordError()

        except PasswordError:
            return False

        return True


class EmailValidator(BaseValidator):
    def __init__(self, email):
        super().__init__(email)
        self.email = email

    def validate(self) -> bool:
        email_regex = r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
        if re.search(email_regex, self.email):
            return True
        
        return False


