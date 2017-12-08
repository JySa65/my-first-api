from rest_framework import serializers
from account.models import Account


class UserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Account
		fields = ('url', 'username', 'ci', 'name', 'last_name', 'email', 'is_active', 'is_staff')