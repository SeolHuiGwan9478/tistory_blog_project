from django import forms
from .models import User
from django.contrib.auth.hashers import check_password
class RegisterForm(forms.Form):
    username = forms.CharField(label='사용자 이름', error_messages={'required': "이름을 입력하세요."})
    email = forms.EmailField(label='이메일', error_messages={'required': "이메일을 입력하세요."})
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput, error_messages={'required': "비밀번호를 입력하세요."})
    re_password = forms.CharField(label='비밀번호 재확인', widget=forms.PasswordInput, error_messages={'required': "비밀번호를 입력하세요."})

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if (password and re_password):
            if password != re_password:
                self.add_error('password', "비밀번호가 틀렸습니다.")
                self.add_error('re_password', "비밀번호가 틀렸습니다.")

class Loginform(forms.Form):
    email = forms.EmailField(label='이메일', error_messages={'required': "이메일을 입력하세요."})
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput, error_messages={'required': "비밀번호를 입력하세요."})

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except user.DoesNotExist:
                self.add_error('email', "이메일이 존재하지 않습니다.")
                return
            if not (check_password(password, user.password)):
                self.add_error('password', "비밀번호가 틀렸습니다.")