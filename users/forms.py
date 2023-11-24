from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


#비밀번호 변경 폼 정의
class PasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].label = '기존 비밀번호'
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'autofocus': False,
        })
        self.fields['new_password1'].label = '새 비밀번호'
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['new_password2'].label = '새 비밀번호 확인'
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
        })

class UserChangeForm(UserChangeForm):
    password = None
    last_name = forms.CharField(label='성', widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength':'80', 'oninput':"maxLengthCheck(this)",}),
    )
    first_name = forms.CharField(label='이름', widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength':'80', 'oninput':"maxLengthCheck(this)",}),
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email']



# 사용자 로그인 폼 정의
class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)  # 아이디 입력 필드
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)  # 비밀번호 입력 필드

# 사용자 회원가입 폼 정의
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='이름')  # 이름 입력 필드
    last_name = forms.CharField(max_length=30, label='성')   # 성 입력 필드
    class Meta:
        model = User  # 내장 User 모델을 사용
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        # 폼에서 사용할 필드들을 지정


# 20231124 비밀번호 찾기 화면에서 초기화랑 비밀번호 새로 변경
class ResetPasswordForm(forms.Form):
    username = forms.CharField(max_length=65, label='아이디')
    email = forms.EmailField(label='이메일')
    new_password = forms.CharField(max_length=65, widget=forms.PasswordInput, label='새 비밀번호')
    confirm_new_password = forms.CharField(max_length=65, widget=forms.PasswordInput, label='새 비밀번호 확인')
    # 새로운 비밀번호가 일치하는지 확인하는 코드인데 필요한가?
    # def clean(self):
    #     cleaned_data = super().clean()
    #     new_password = cleaned_data.get('new_password')
    #     confirm_new_password = cleaned_data.get('confirm_new_password')
    #
    #     if new_password and confirm_new_password and new_password != confirm_new_password:
    #         raise forms.ValidationError("새 비밀번호가 일치하지 않습니다.")
    #     return cleaned_data





