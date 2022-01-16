from .forms import ContactUsModelForm
from django.views.generic.edit import CreateView

class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'
