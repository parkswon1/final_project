from django import forms
from signapp.models import Customer
from searchapp.models import Allergy

class SignupForm(forms.ModelForm):
    # gender 필드는 HiddenInput 위젯을 사용하여 숨겨진 필드로 정의되며 초기값은 1로 설정됩니다.
    gender = forms.IntegerField(widget=forms.HiddenInput(), initial=1)
    
    # 알러지 정보를 쉼표로 구분하여 저장할 TextField로 정의
    allerinfo = forms.ModelMultipleChoiceField(
        queryset=Allergy.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Customer  # 폼과 연결될 모델
        fields = ['username', 'email', 'phone', 'birthdate', 'gender', 'password', 'allerinfo']  # 폼에 사용될 필드들
    
    # 비밀번호 확인용 필드를 PasswordInput 위젯으로 정의합니다.
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    
    # 비밀번호가 같은지 검사하는 메서드
    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")

        return password_confirm

    # 이메일 중복 검사를 위한 메서드
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        # 이미 등록된 이메일이 존재하면 에러 발생
        if Customer.objects.filter(email=email).exists():
            raise forms.ValidationError("이미 있는 이메일입니다.")
        
        return email
    
    # 아이디 중복 검사를 위한 메서드
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        # 이미 등록된 이메일이 존재하면 에러 발생
        if Customer.objects.filter(username=username).exists():
            raise forms.ValidationError("이미 있는 ID입니다.")
        
        return username