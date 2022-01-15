from django.shortcuts import render, redirect
from .forms import ContactUsForm
from .models import ContactUs


def contact_us_page(request):
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
            content = ContactUs(
                title = contact_form.cleaned_data.get('subject'),
                full_name = contact_form.cleaned_data.get('full_name'),
                email = contact_form.cleaned_data.get('email'),
                message = contact_form.cleaned_data.get('text'),
            )
            
            content.save()
            return redirect('home_page')
    else:
        contact_form = ContactUsForm()

    return render(request, 'contact_module/contact_us_page.html', {
        'contact_form': contact_form
    })
