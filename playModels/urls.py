from django.urls import path
from . import views


app_name="polls"
urlpatterns = [
    path("",views.firstView,name="YourFirstView"),
    path("register/",views.registerView,name="registerView"),
    path("newtask/",views.myForm,name="myForm"),
    path("thanks/",views.thanksView,name="thanks_page"),
    
]
