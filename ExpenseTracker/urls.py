from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('addexpense/',views.addexpense,name="addexpense"),
    path('saveexpense/',views.saveexpense,name="saveexpense"),
    path('deleteexpense/<int:id>,<int:budget>',views.deleteexpense,name="deleteexpense"),
    path('report/',views.filter_records,name="report"),
    path('homepage/',views.homepage,name="homepage"),
    
]

  
 
   
 