from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    PermissionsMixin,
    AbstractBaseUser,
)
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime

class UserManager(BaseUserManager):
    """User model manager."""
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email field must be set.')
        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user =self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User Model"""
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=99)
    last_name = models.CharField(max_length=99)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


class Category(models.TextChoices):
    """Enumerated Category Choice"""
    WORK = 'WRK', 'Work'
    PERSONAL = 'PRL', 'Personal'
    STUDY = 'STU', 'Study'
    OTHER = 'OTR', 'Other'


class Priority(models.TextChoices):
    """Enumerated Priority Choice"""
    LOW = 'LW', 'Low'
    MEDIUM = 'MD', 'Medium'
    HIGH = 'HG', 'High'


class Status(models.TextChoices):
    """Enumerated Status Choice"""
    PENDING = 'PND', 'Pending'
    IN_PROGRESS = 'IP', 'In Progress'
    COMPLETED = 'COM', 'Completed'
    OVERDUE = 'OVD', 'Overdue'


def validate_due_date(value):
    if value < timezone.now().date():
        raise ValidationError('Due date cannot be in the past.')


class Task(models.Model):
    """Task Model"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(
        max_length=3,
        choices=Category.choices,
        default=Category.OTHER
    )
    status = models.CharField(
        max_length=3,
        choices=Status.choices,
        default=Status.PENDING
    )
    priority = models.CharField(
        max_length=2,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )
    created_at = models.DateField(auto_now_add=True)
    due_date = models.DateField(validators=[validate_due_date])
    completed_at = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def mark_as_completed(self):
        self.status = Status.COMPLETED
        self.completed_at = timezone.now()
        self.save()

    def check_status(self):
        if self.status == Status.COMPLETED:
            self.mark_as_completed()
            self.save()

        if self.due_date < timezone.now().date() and self.status != Status.COMPLETED:
            self.status = Status.OVERDUE
            self.save()

        if self.due_date >= timezone.now().date() and self.status == Status.OVERDUE:
            self.status = Status.PENDING
            self.save()

    def duration(self):
        if self.completed_at:
            diffrence = (self.completed_at - self.created_at)
            return diffrence.days
        return None

    def __str__(self):
        return self.title
