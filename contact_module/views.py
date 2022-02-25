from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import ContactUsModelForm
from .models import UserProfile


class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'


def store_file(file):
    with open('temp/image.png', "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):
    tempplate_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = 'contact-us/create-profile'


class ProfilesView(ListView):
    model = UserProfile
    template_name = 'contact_module/profiles_list_page.html'
    context_object_name = 'profiles'
