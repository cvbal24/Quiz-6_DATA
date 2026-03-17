from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):
	def _create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError('The email field must be set.')
		email = self.normalize_email(email)
		username = extra_fields.pop('username', None) or email.split('@')[0]
		return super()._create_user(username, email, password, **extra_fields)

	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('role', CustomUser.Role.ADMIN)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
	class Role(models.TextChoices):
		ADMIN = 'Admin', 'Admin'
		SELLER = 'Seller', 'Seller'
		USER = 'User', 'User'

	email = models.EmailField(unique=True)
	username = models.CharField(max_length=150)
	phone_number = models.CharField(max_length=20, blank=True)
	first_name = models.CharField(max_length=150, blank=True)
	last_name = models.CharField(max_length=150, blank=True)
	location = models.CharField(max_length=255, blank=True)
	gender = models.CharField(max_length=50, blank=True)
	role = models.CharField(max_length=20, choices=Role.choices, default=Role.USER)
	merchant_id = models.CharField(max_length=255, null=True, blank=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = CustomUserManager()

	def __str__(self):
		return self.email
