from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from notifications.models import Messages


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, job_class, organizations, notification):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            data_joined=now,
            job_class=job_class,
            organizations=organizations,
            notification=notification,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, job_class, organizations):
        return self._create_user(username, email,password,False,False,job_class,organizations, None)

    def create_superuser(self, username, email, password):
        user = self._create_user(username, email, password, True, True, None, None, None)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    username = models.CharField(max_length=254, null=False, blank=True, unique=True, db_index=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=False)
    data_joined = models.DateTimeField(auto_now_add=True,null=True)
    ORG_Manager = 'Office Manager'
    ORG_Employee = 'Office Employee'
    Employee = 'Employee'
    Job_Class = (
        (ORG_Manager, 'Office Manager'),
        (ORG_Employee, 'Office Employee'),
        (Employee, 'Employee')
    )
    job_class = models.CharField(max_length=40, choices=Job_Class, default=Employee, blank=True, null=True, db_index=True)
    organizations = models.CharField(max_length=254, default=None, null=True, blank=True, db_index=True)
    notification = models.ForeignKey(Messages, blank=True, on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_absolute_url(self):
        return "/accounts/%i" % (self.pk)









