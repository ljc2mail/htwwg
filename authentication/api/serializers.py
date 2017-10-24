from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField,
	SerializerMethodField,
	EmailField
	)

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class UserCreateSerializer(ModelSerializer):
	email = EmailField(label="Email Address")
	email2 = EmailField(label="Confirm Email Address")

	class Meta:
		model=User
		fields = ('email', 'date_of_birth', 'password')

		extra_kwargs = {"password":
									{'write_only': True}
		}


	def validate_email2(self, value):
		data = self.get_initial()
		email1 = data.get("email")
		email2 = value
		if email2 != email1 :
			raise ValidationError ('Email must match')
		return value

	"""
		email_qs = User.objects.filter(email=email2)
		if email_qs.exists() :
			raise ValidationError('email already exists')
	"""



	def create(self, validated_data):
		email = validated_data['email']
		date_of_birth = validated_data['date_of_birth']
		password = validated_data['password']
		user_obj = User(
			email = email,
			date_of_birth = date_of_birth,
			password = password
			)
		user_obj.set_password(password)
		user_obj.save()
		return user_obj
