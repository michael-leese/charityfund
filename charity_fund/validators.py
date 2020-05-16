from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import re

#Password validation to ensure that password has a number
class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                _("Password must contain at least 1 digit, 0-9."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "Password must contain at least 1 digit, 0-9."
        )

#Password validation to ensure that password has an uppercsae character
class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("Password must contain at least 1 uppercase letter, A-Z."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _(
            "Password must contain at least 1 uppercase letter, A-Z."
        )

#Password validation to ensure that password has a lowercsae character
class LowercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _("Password must contain at least 1 lowercase letter, a-z."),
                code='password_no_lower',
            )

    def get_help_text(self):
        return _(
            "Password must contain at least 1 lowercase letter, a-z."
        )

#Password validation to ensure that password has a symbol
class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|`~!@#$%^*_\-+=;:\'",<>]', password):
            raise ValidationError(
                _("Password must contain at least 1 symbol: " +
                  "()[]{}|`~!@#$%^*_-+=;:'\",<>"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "Password must contain at least 1 symbol: " +
            "()[]{}|`~!@#$%^*_-+=;:'\",<>"
        )