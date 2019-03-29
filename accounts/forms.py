from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

    # what is the use of the UserCreationForm ?
    # it is a modelForm for creating new User
    # has three fields : username , password1 and password2

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
