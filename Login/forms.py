from django import forms
from acl.models import User as UserModel

class UserForm(forms.ModelForm):
    
    class Meta:
        model = UserModel
        fields = ['email', 'username', 'password', 'is_superuser']
