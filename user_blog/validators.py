import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class SpecialCharacterValidator:
    def validate(self, password, user=None):
        if not re.findall("[^A-Za-z0-9]", password):
            raise ValidationError(
                _("The password must contain at least 1 special character."),
                code="password_no_special",
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 special character.")
