
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = None
    last_login = None
    last_name = None


    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username




    
#далее - setting :AUTH_USER_MODEL = 'users.User'




