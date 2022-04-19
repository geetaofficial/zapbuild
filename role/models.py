from django.db import models
from django.contrib.auth.models import  AbstractUser
import jwt

from datetime import datetime, timedelta

from django.conf import settings


# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('mng', 'Manager'),
        ('emp', 'employee'),
        ('cln', 'client')
    )
    user_type = models.CharField(max_length=3,
                                choices=USER_TYPE_CHOICES,
                                default=USER_TYPE_CHOICES[1][0])
    # tasks = models.ManyToManyField('tasks.Tasks',)

    def __str__(self):
        return f'{self.username}'


    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()


    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

