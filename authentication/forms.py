from .admin import UserChangeForm

from .models import MyUser

class EditProfileForm(UserChangeForm):

	class meta:
		model = MyUser
		fields = (
			'email',
			'password',
			'picture'
			)