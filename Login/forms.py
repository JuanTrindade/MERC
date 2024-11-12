from django import forms
from acl.models import User as UserModel

class UserForm(forms.ModelForm):
    
    class Meta:
        model = UserModel
        fields = ['email', 'first_name', 'last_name','password', 'is_superuser']
