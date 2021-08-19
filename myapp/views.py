from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


# Create your views here.
def index(request):
	return render(request, "index.html")

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'agapereality@gmail.com', ['agapereality@gmail.com']) 
				messages.success(request, "Your message was successfully sent.")
			except BadHeaderError:
				messages.error(request, "An error occurred. Please try again")
				return HttpResponse('Invalid header found.')
			except Exception as e:
				messages.error(request, str(e))
			return redirect ("index")
      
	form = ContactForm()
	return render(request, "contact.html", {'form':form})

def education(request):
    return render(request, 'education.html')

def project(request):
    return render(request, 'project.html')

def skill(request):
    return render(request, 'skill.html')


