


from django.shortcuts import render,redirect
from .models import Users
import requests
from decouple import AutoConfig

config=AutoConfig()

TEXT_LOCAL_API_KEY=config('TEXT_LOCAL_API_KEY')


def firstView(request):
     if request.method=='POST':
          return redirect('polls:myForm')
     return render(request,'polls/button1.html')



def registerView(request):
   chat1=Users.objects.get(pk=7)
   return render(request,"polls/index.html",{"chat1":chat1})

def myForm(request):
       if request.method=='POST':
              
              Users(first_name=request.POST["first_name"],last_name=request.POST["last_name"],ph_number=request.POST["ph_number"]).save()
              url='https://api.textlocal.in/send/'
              template_id = config('TEMPLATE_ID')
              message_content ='Hi there, thank you for sending your first test message from Textlocal. See how you can send effective SMS campaigns here: https://tx.gl/r/2nGVj/'
              params = {
                   'apiKey': TEXT_LOCAL_API_KEY,
                   'numbers': request.POST["ph_number"],
                   'template_id': template_id,  # Use the template ID here
                   'message': message_content,  # Specify the message content here
                   'sender': '600010',
                   'category': 'promotional',  # Add the 'category' parameter here
        }
              response = requests.post(url, data=params)
              print(response.status_code)
              print(response.text)
              if response.status_code == 200:
                  request.session['form_submittes']=True
                  return redirect('polls:thanks_page')  
              else:
                # Handle the error here and provide feedback to the user
                 print("API Error:", response.status_code)
                 print("API Response:", response.text)  
       return render(request,'polls/detail.html')

def thanksView(request):
      if request.session.get('form_submittes'):
           return render(request,"polls/thanks.html")
      else:
           return redirect('polls:myForm')