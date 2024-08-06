from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def personaldetails(request):
    return render(request, 'sign_up/personal_details.html')

def jobstatus(request):
    return render(request, 'sign_up/job_status.html')

def jobdetails(request):
    return render(request, 'sign_up/job_details.html')