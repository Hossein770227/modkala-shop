from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, first_name, last_name,  password):
        if not first_name:
            raise ValueError(_("user must have first name"))
        if not last_name:
            raise ValueError(_("user must have last name"))
        if not phone_number:
            raise ValueError(_("user must have phone number"))
        
        user = self.model(phone_number=phone_number, first_name=first_name, last_name=last_name)
        user.set_password((password))
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, first_name, last_name, password):
        user = self.create_user(phone_number, first_name, last_name, password)
        user.is_admin = True
        user.save(using=self._db)
        return user