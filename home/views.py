from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from profiles.models import UserProfile

from .forms import NewsletterForm, MessageForm

# Create your views here.

def home(request):
    """ A view to return index page """
    
    if request.method == "POST":
        subscribers_email = request.POST["email"]
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = render_to_string(
                "home/newsletter/newsletter_subject.txt"
            )
            body = render_to_string(
                "home/newsletter/newsletter_content.txt"
            )
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [subscribers_email]
            )
            messages.success(request,
                            "You have been signed up for our newsletter")
            
            return redirect("home")
        else:
            messages.error(request,
                        "Something has gone wrong.\
                            Please check your email address and try again.")
            return redirect("home")
    else:
        form = NewsletterForm()

    template = "home/index.html"
    context = {
        
        "form": form,
        
    }

    return render(request,
                template,
                context)
    
    
    
def contact(request):
     ''' renders the contact us page '''
     if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                            "Your message has been sent.\
                            Someone from our customer service team will be in contact soon.")
            return redirect("home")
        else:
            messages.error(request,
                            "Something has gone wrong.\
                            Please try again soon")
            return redirect("contact")
     else:
        if request.user.is_authenticated:
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                form = MessageForm(initial={
                    "user_email": user_profile.user.email
                })
            except UserProfile.DoesNotExist:
                form = MessageForm()
        else:
            form = MessageForm()

     template = "home/contact.html"
     context = {
        "form": form,
    }

     return render(request,
                  template,
                  context)