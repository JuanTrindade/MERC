from django import forms
from .models import User as UserModel
from .models import UserClient as UserClientModel
from .models import UseerSupplier as UserSupplierModel


class UserForm(forms.ModelForm):
    
    class Meta:
        model = UserModel
        fields = ['email', 'first_name', 'last_name', 'username', 'password', 'is_superuser']

# 
# 
class UserClientForm(forms.ModelForm):

    class Meta:
        model = UserClientModel
        fields = ('__all__')

        widgets = {'cpf': forms.TextInput(attrs={'data-mask': '000.000.000-00'})}

# 
# 
class UserSupplierForm(forms.ModelForm):

    class Meta:
        model = UserSupplierModel
        fields = ('__all__')

        widgets = {'cnpj': forms.TextInput(attrs={'data-mask': '00.000.000/0000-00'})}