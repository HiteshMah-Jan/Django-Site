#manmade stuff
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
    #return HttpResponse('<h1> Welcome to Hitesh tour.</h1> ')

def background(request):
    return render(request, 'about.html')

def LeaveAMessage(request):
    message = ['','','']
    message[0] = (request.GET.get('name', ''))
    message[1] = (request.GET.get('number', ''))
    message[2] = (request.GET.get('message', ''))
    print(message)
    if message != ['','','']:
        isMessage = True
        file = open(r'messages.txt', 'a')
        file.writelines(message)
        file.write('\n')
        file.close()
    else:
        isMessage = False

    return render(request, 'LeaveAMessage.html', {'message': isMessage})

def contact(request):
    return render(request, 'contact.html')
