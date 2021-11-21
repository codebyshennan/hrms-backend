from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.db.models.base import ModelBase
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Organisation(models.Model):
  created_user_id = models.IntegerField()
  name = models.TextField()
  shift_types = models.TextField(unique=True)
  leaves_per_worker = models.IntegerField()
  workhours_per_worker = models.IntegerField()
  global_total_shifts = models.IntegerField()
  global_remaining_shifts = models.IntegerField()


class User(models.Model):

  class ShiftType(models.TextChoices):
    A = 'A', _('Shift A')
    B = 'B', _('Shift B')
    C = 'C', _('Shift C')

  org_id = models.ForeignKey(Organisation, on_delete=models.CASCADE)
  username = models.TextField()
  real_name = models.TextField()
  password = models.TextField()
  type = models.CharField(choices=ShiftType.choices, default=ShiftType.A, max_length=255, blank=False)

  def __str__(self):
    return self.username

class UserShift(models.Model):
  user_id = models.OneToOneField(User, on_delete=models.CASCADE)
  month = models.IntegerField()
  shift_dates = models.JSONField()
  leave_dates = models.JSONField()
  remainder_shifts = models.IntegerField()
  year = models.IntegerField()
  allocated_leaves = models.IntegerField()

  def __str__(self):
    return self.user_id

class Schedule(models.Model):
  org_id = models.ForeignKey(Organisation, on_delete=models.CASCADE, to_field="shift_types")
  created_user_id = models.IntegerField()
  created_at = models.DateTimeField()
  choices = models.JSONField()

  def __str__(self):
    return self.created_user_id