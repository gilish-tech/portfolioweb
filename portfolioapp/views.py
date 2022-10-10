from django.shortcuts import render,redirect
from .models import Messages

# Create your views here.


def home_page(request):
    if request.method == "POST":
        
        name  = request.POST.get("name")
        email =  request.POST.get("email")
        subject  = request.POST.get("subject")
        message =  request.POST.get("message")

        print(name)
        print(email)
        print(subject)
        print(message)

        

        check = name + subject + message

        if name.strip() != "" or message.strip() != "" or subject.strip() !=  "":


            if not "dennis" in check.lower() or "denis"  in check.lower() or check.strip() == "" :
                print("Noooooo0")
                Messages.objects.create(message=message,name=name,subject=subject,email=email)
                return redirect("comment")
    return render(request,"index.html")



def comment_page(request):
    messages = Messages.objects.all()
    context = {
        "messages":messages
    }
    return render(request,"comments.html",context)