from datetime import (
    datetime,
    timedelta,
)
from typing import TYPE_CHECKING

from django.contrib.auth.models import (
    AbstractUser,
    Group,
    UserManager,
)
from django.db import models
from django.utils import timezone


if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager

    from houses.models import (
        House,
        HouseProfile,
        PointsTransaction,
    )


def current_year() -> int:
    """Gets the current year.
    """
    return datetime.now().year


class User(AbstractUser):
    """Custom user model.
    """

    id: 'models.AutoField[int, int]'

    objects: 'UserManager[User]'

    groups: 'RelatedManager[Group]'

    house_managers: 'RelatedManager[House]'
    house_points: 'RelatedManager[PointsTransaction]'
    house_profile: 'HouseProfile | None'

    is_verified: 'models.BooleanField[bool, bool]' = models.BooleanField(
        'e-mail verificado', default=False,
    )

    verify_email_sent = models.DateTimeField(
        'último envío de correo de verificación',
        blank=True, null=True,
    )

    telegram_user: 'models.CharField[str, str]' = models.CharField(
        'usuario de telegram', max_length=64, blank=True
    )
    telegram_id: 'models.IntegerField[int | None, int | None]' = models.IntegerField(
        'ID de telegram', blank=True, null=True
    )

    first_year: 'models.IntegerField[int, int]' = models.IntegerField(
        'año de ingreso', default=current_year
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'

    @property
    def display_name(self) -> str:
        """Gets the display name for this user.

        The display name is either the full name of the username. This
        method always returns a non-blank string.
        """
        return self.get_full_name() or self.username

    def can_send_verify_email(self) -> bool:
        """Checks if the user can send a verify email.
        """
        return (
            self.verify_email_sent is None
            or self.verify_email_sent + timedelta(seconds=60) < timezone.now()
        )
