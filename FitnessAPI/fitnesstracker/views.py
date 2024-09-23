from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import User,Workout,Diet
from .serializers import user_serializer,Workout_serializer,Diet_serializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
class signinview(APIView):
    
  authentication_classes = [BasicAuthentication] 
  permission_classes = [IsAuthenticated]
  
  def post(self,request):
    username = request.data["username"]
    password = request.data["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        users = User.objects.get(id=user.id)
        data=user_serializer(users).data
        return Response({'status':'Login Successful','users':data},status=200)
    else:
        return Response({"message": "Invalid credentials"}, status=401)


class signupview(APIView):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        
        new_user = User(username=request.data["username"],email=request.data["email"],age=request.data["age"],
                         height=request.data["height"],weight=request.data["weight"],contact_no=request.data["contact_no"])
        new_user.set_password(request.data["password"])
        
        new_user.save()
        email=[request.data["email"]]
        settings.EMAIL_HOST_USER = 'sportsclub3115@gmail.com'
        settings.EMAIL_HOST_PASSWORD = 'lkbq ewpe spbz qsya'
        send_mail("Confirmation Mail","You have Registered successfully",settings.EMAIL_HOST_USER ,email)

        
        
        return Response({'status':'New User Added'},status=200)
        
       
    
    
class Userview(APIView):
    
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    
            
    
    def get(self,request):
        
        datas = User.objects.all()
        serialized_data = user_serializer(datas,many=True).data
        return Response({'status':'success','users':serialized_data},status=200)
    
class Userviewbyid(APIView):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,id):
        
        data = User.objects.get(id=id)
        if data is not None:
         serialized_data = user_serializer(data).data
         return Response({'status':'success','user':serialized_data},status=200)
     
        else:
            return Response({'status':'error'},status=status.HTTP_400_BAD_REQUEST)
    
    
   
    
    def patch(self,request,id):
        
        data = User.objects.get(id=id)
        serialized_data = user_serializer(data,data = request.data,partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
        return Response({'status':'User Data Updated','user':serialized_data.data},status=200)
    
    def put(self,request,id):
        userdata = User.objects.get(id=id)
        serialized_data = user_serializer(userdata,data = request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'status':'User Data Updated','user':serialized_data.data},status=200)
        

    def delete(self,request,id):
        
        data = User.objects.get(id=id)
        data.delete()
        return Response({'status':'User Data Deleted'},status=200)
    
    
    
    
class Workoutview(APIView):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        
        Workout_all = Workout.objects.all()
        serialized_data = Workout_serializer(Workout_all,many=True).data
        return Response({'status':'success','user':serialized_data},status=200)  
    
    def post(self,request):
        
        new_workout = Workout_serializer(data = request.data)
        if new_workout.is_valid():
            new_workout.save()
            return Response({'status':'workout Details Added','workout':new_workout.data},status=200)
        
class workoutviewsbyid(APIView):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,id):
        
        Workout_data = Workout.objects.get(id=id)
        serialized_data = Workout_serializer(Workout_data).data
        return Response({'status':'success','Workout':serialized_data},status=200)
    
    def delete(self,request,id):
        
        data = Workout.objects.get(id=id)
        data.delete()
        return Response({'status':'Data Deleted'},status=200)
    
    def patch(self,request,id):
        
        data = Workout.objects.get(id=id)
        serialized_data = Workout_serializer(data,data=request.data,partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'status':'Data Updated','Workout':serialized_data.data},status=200)  
    
    def put(self,request,id):
        
        workout_data = Workout.objects.get(id=id)
        serialized_data = Workout_serializer(workout_data,data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'status':'Data Updated','Workout':serialized_data.data},status=200)    
 
 
class Workoutviewsbyuserid(APIView):
    
      authentication_classes = [BasicAuthentication]
      permission_classes = [IsAuthenticated]
      
      def get(self,request,id):
        Workout_data = Workout.objects.filter(user=id)
        serialized_data = Workout_serializer(Workout_data,many=True).data
        return Response({'status':'success','Workout':serialized_data},status=200)
    
      def delete(self,request,id):
        data = Workout.objects.filter(user=id)
        data.delete()
        return Response({'status':'Data Deleted'},status=200)
         
          
        
class  dietviews(APIView):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        
        diet_all = Diet.objects.all()
        serialized_data = Diet_serializer(diet_all,many=True).data
        return Response({'status':'success','Diet':serialized_data},status=200)
    
    def post(self,request):
        
        new_data = Diet_serializer(data = request.data) 
        if new_data.is_valid():
            new_data.save()
            return Response({'status':'New Data Added','Diet':new_data.data},status=200)     
        
class dietviewsbyid(APIView):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,id):
        
        diet_data = Diet.objects.get(id=id)
        serialized_data = Diet_serializer(diet_data).data
        return Response({'status':'success','Diet':serialized_data},status=200)
    
    def delete(self,request,id):
        
        diet_data = Diet.objects.get(id=id)
        diet_data.delete()
        return Response({'status':'Data Deleted'},status=200)
    
    def patch(self,request,id):
        
        diet_data = Diet.objects.get(id=id)
        serialized_data = Diet_serializer(diet_data,data= request.data,partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
        return Response({'status':'Data Modified','user':serialized_data.data},status=200)
    
    def put(self,request,id):
        
        diet_data = Diet.objects.get(id=id)
        serialized_data = Diet_serializer(diet_data,data= request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'status':'Data Modified','user':serialized_data.data},status=200)
            
class send_email(APIView):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        
         subject = request.data["subject"]
         message = request.data["message"]
         settings.EMAIL_HOST_USER = request.data["email_from"]
         settings.EMAIL_HOST_PASSWORD = request.data["password"]
         
         email_from = settings.EMAIL_HOST_USER
         recipient_list = ['sportsclub3115@gmail.com']
    
         send_mail(subject, message, email_from, recipient_list)   
         return Response("mail sent successfully")
     
class Dietviewsbyuserid(APIView):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,id):
        
        data = Diet.objects.filter(user=id)
        serialized_data=Diet_serializer(data,many=True).data
        return Response({'status':"success",'Diet_info':serialized_data},status=200)
    
            
    def delete(self,request,id):
        
        data=Diet.objects.filter(user=id)
        data.delete()
        return Response({'status':'Data Deleted'},status=200)
        
        
        
    
        
        
        
    
    
