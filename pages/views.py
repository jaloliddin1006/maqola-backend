from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
# Create your views here.
from .models import Message

class HomePageView(TemplateView):
    template_name = 'home.html'

# class ContactView(TemplateView):
#     template_name = 'contact.html'
    
def ContactView( request):
    if request.method == "POST":
            
        my_data = request.POST
        context = {}
        print(my_data)
        
        
        name = request.POST['contact_name']
        email = request.POST['contact_email']
        subject = request.POST['contact_subject']
        message = request.POST['contact_message']
        Message.objects.create(name=name, email = email, subject = subject, body = message).save()

        # return super(TemplateView,self).render_to_response(context)
        return render(request, 'home.html')
    else:
        return render(request, 'contact.html')
        