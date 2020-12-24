from django.shortcuts import render
from django.core.mail import send_mail
from Project10.settings import EMAIL_HOST_USER


def showIndex(request):
    return render(request, "index.html")


def sendMail(request):
    # Sending Mail to 1 Person

    # to = request.POST.get("t1")
    # subject = request.POST.get("t2")
    # message = request.POST.get("t3")
    #
    # send_mail(subject,message,EMAIL_HOST_USER,[to])
    #
    # return render(request,"index.html",{"message":"Mail Sent"})

    # Sending mail to Multiple Persons
    to = request.POST.get("t1")
    to_list = to.split(",")
    subject = request.POST.get("t2")
    message = request.POST.get("t3")

    send_mail(subject, message, EMAIL_HOST_USER, to_list)

    return render(request, "index.html", {"message": "Mail Sent"})


