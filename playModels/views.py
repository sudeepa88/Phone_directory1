


from django.shortcuts import render,redirect
from .models import Users


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
             request.session['form_submittes']=True
             return redirect('polls:thanks_page')
            
       return render(request,'polls/detail.html')

def thanksView(request):
      if request.session.get('form_submittes'):
           return render(request,"polls/thanks.html")
      else:
           return redirect('polls:myForm')

           