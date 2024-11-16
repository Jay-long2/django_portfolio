from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
#create your views here
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully.")
            return redirect('contact')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})

def home_view(request):
    return render(request, 'portfolio/home.html')