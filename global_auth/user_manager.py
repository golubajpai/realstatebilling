from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone:
            raise ValueError('Users must have an phone number')

        user = self.model(
            phone=phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,phone, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        u = self.create_user(phone,
                        password=password,
                    
                    )
        u.is_admin = True
        u.is_mapper=True
        u.save(using=self._db)
        return u


class AbstractUser(AbstractBaseUser):
    phone = models.CharField(
                        verbose_name='phone number',
                        max_length=10,
                        unique=True,
                    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_mapper=models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone'


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


    class Meta:
        abstract=True