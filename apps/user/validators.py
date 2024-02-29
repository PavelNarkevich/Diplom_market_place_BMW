from django.core.exceptions import ValidationError

import re

from apps.user.errors_massages import (
    RUSSIAN_SYMBOL_IN_PWD,
    NUM_IN_PWD,
    PASSWORD_DO_NOT_MATCH_ERROR,
    PHONE_NOT_VALID
)


class ValidateRegisterData:
    def __init__(self, password, password2, phone):
        self.password = password
        self.password2 = password2
        self.phone = phone

    def validate_eng_symbol_and_digits(self):
        password = self.password

        if re.search(r'[0-9]', password):
            if re.search(r'[^a-zA-Z 0-9]', password):
                raise ValidationError(
                    RUSSIAN_SYMBOL_IN_PWD
                )
            return True
        else:
            raise ValidationError(
                NUM_IN_PWD
            )

    def validate_phone(self):
        phone = self.phone

        country_code = ('+375', '80')
        operator_code = ('25', '33', '29', '44')

        if len(phone) == 13:
            if phone[:4] in country_code and phone[4:6] in operator_code:
                return True
            else:
                raise ValidationError(PHONE_NOT_VALID)

        if len(phone) == 12:
            if phone[:2] in country_code and phone[2:4] in operator_code:
                return True
            else:
                raise ValidationError(PHONE_NOT_VALID)
        else:
            raise ValidationError(PHONE_NOT_VALID)

    def validate_password_match(self):
        password = self.password
        password2 = self.password2

        if password != password2:
            raise ValidationError(
                PASSWORD_DO_NOT_MATCH_ERROR
            )
        return self.validate_eng_symbol_and_digits()

    def validate_pwd(self):
        return self.validate_password_match()
