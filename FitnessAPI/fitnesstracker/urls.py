from django.urls import path

from .views import send_email,signupview,signinview,Workoutviewsbyuserid,Dietviewsbyuserid,Userview,Userviewbyid,Workoutview,workoutviewsbyid,dietviews,dietviewsbyid#login_view

urlpatterns = [
     path('Login/',signinview.as_view()),
     path('signup/',signupview.as_view()),
     path('sendmail/',send_email.as_view()),
     path('User/',Userview.as_view(),name="Userview"),
     path('User/<int:id>',Userviewbyid.as_view()),
     path('Workout/',Workoutview.as_view()),
     path('Workout/<int:id>',workoutviewsbyid.as_view()),
     path('Workoutbyuser/<int:id>',Workoutviewsbyuserid.as_view()),
     path('Dietbyuser/<int:id>',Dietviewsbyuserid.as_view()),
     path('Diet/',dietviews.as_view()),
     path('Diet/<int:id>',dietviewsbyid.as_view()),
     
  
]