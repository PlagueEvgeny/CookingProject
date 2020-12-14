from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control {name}'


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'password1', 'password2', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control {name}'
            item.help_text = ''


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name',
                   'email')

    def __init__( self, *args, **kwargs ):
        super( UserChangeForm, self ).__init__( *args, **kwargs )
        if self.instance and self.instance.pk:
            # Since the pk is set this is not a new instance
            self.fields['username'] = self.instance.username
            self.fields['username'].widgets.attrs['readonly'] = True
