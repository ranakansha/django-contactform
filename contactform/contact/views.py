from django.shortcuts import render
from contact.models import Contact
from contact.forms import ContactForm
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def index(request):
    return HttpResponse("hii")

def home(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # return HttpResponse(str(form))
        if form.is_valid():
            if form.save():
                subject = form.cleaned_data['subject']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['ranakansha321@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

                messages.success(request, 'Profile details updated.')
            
            
            return render(request,'contact.html')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")

    else:
        return render(request,'contact.html')
