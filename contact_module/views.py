from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView

from .forms import ContactUsModelForm, ProfileForm
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
    def get(self, request):
        form = ProfileForm()
        return render(request, 'contact_module/create_profile_page.html', {
            'form': form
        })
    
    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)
        
        if submitted_form.is_valid():
            # store_file(request.FILES["profile"])
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()
            return redirect('/contact-us/create-profile/')
        
        return render(request, 'contact_module/create_profile_page.html', {
            'form': submitted_form
        })
            