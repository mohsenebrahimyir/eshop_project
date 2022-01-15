from django import forms
from .models import ContactUs


class ContactUsForm(forms.Form):
    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        max_length=50,
        error_messages={
            'required': 'لطفا نام و نام خانوادگی خود را وارد کنید.',
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام و نام خانوادگی',
        })
    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیـل',
        })
    )
    title = forms.CharField(
        label='عنوان',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'عنوان'
        })
    )
    message = forms.CharField(
        label='متن',
        widget=forms.Textarea(attrs={
            'id': 'message',
            'class': 'form-control',
            'placeholder': 'متن پیام',
            'rows': 8,
        })
    )


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['email', 'full_name', 'title', 'message']
        # fields = '__all__' # Select All
        # exclude = ['is_read_by_admin', 'response', 'created_date'] # Unselect some one
        widgets = {
            'full_name':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی',
            }),
            'email':forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیـل',
            }),
            'title':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان'
            }),
            'message':forms.Textarea(attrs={
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