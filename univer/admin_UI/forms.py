# -*- coding: utf-8 -*-
from django import forms
from models import Teacher

choise_faculty = (
    ('ксис', 'ксис'),
    ('иф', 'иф'),
    ('фиту', 'фиту'),
    ('фрэ', 'фрэ')
)


class SignUpForm(forms.ModelForm):
    error_css_class = "error_field"
    password2 = forms.CharField(widget=forms.PasswordInput,
                                error_messages={'required':"input pass"},
                                label='повторите пароль')

    class Meta:
        model = Teacher
        exclude = ['last_login', 'is_active']
        fields = ['last_name', 'first_name',  'third_name', 'faculty',
                  'avatar', 'email', 'password', 'password2']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'пароль'}),
             'faculty': forms.Select(choices=choise_faculty)
        }

        labels = {
            'password': 'пароль',
            'first_name':'имя',
            'last_name': 'фамилия',
            'third_name': 'отчество',
            'faculty': 'факультет',
            "email": 'email',
            'avatar': 'фото'
        }

    def clean(self, *args, **kwargs):
        pas1 = self.cleaned_data.get('password')
        pas2 = self.cleaned_data.get('password2')
        email = self.cleaned_data.get('email')
        print self.cleaned_data.get('avatar')
        if self.cleaned_data.get('avatar') == None:
            raise forms.ValidationError("Image is None")
        if pas1 != pas2:
            self.add_error('password2', "пароли должны совпадать")
        return super(SignUpForm, self).clean(*args, **kwargs)
