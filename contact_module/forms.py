from django import forms
from .models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['email', 'full_name', 'title', 'message']
        # fields = '__all__' # Select All
        # exclude = ['is_read_by_admin', 'response', 'created_date'] # Unselect some one
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیـل',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان'
            }),
            'message': forms.Textarea(attrs={
                'id': 'message',
                'class': 'form-control',
                'placeholder': 'متن پیام',
                'rows': 8,
            })
        }

        labels = {
            'full_name': 'نام و نام خانوادگی شما',
            'email': 'ایمیل شما',
            'title': 'موضوع تماس',
            'message': 'پیام شما'
        }

        error_messages = {
            'full_name': {
                'required': 'لطفا نام و نام خانوادگی خود را وارد کنید.',
            }
        }


class ProfileForm(forms.Form):
    user_image = forms.FileField()