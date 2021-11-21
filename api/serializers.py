from rest_framework import serializers

from .models import User, UserShift, Schedule, Organisation

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('username', 'real_name')