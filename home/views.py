from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

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
                settings.DEFAULT_EMAIL_ADDRESS,
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
    
    