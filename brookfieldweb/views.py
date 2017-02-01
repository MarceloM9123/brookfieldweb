from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail


def index(request):
    form = ContactForm()

    if request.method == 'POST':

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']

            recipients = ['marcelomata91@gmail.com']

            send_mail(subject, message, sender, recipients)

    return render(request, 'brookfieldweb/index.html', {'form': form})


