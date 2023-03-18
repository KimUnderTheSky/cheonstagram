from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
class Join(APIView):
    def get(self, request):
        
        return render(request, "user/join.html")
    def post(self, request):
        email = request.data.get('email', None)
        nickname = request.data.get('nickname', None)
        name = request.data.get('name', None)
        password = request.data.get('password', None)

        User.objects.create(email=email,
                            nickname=nickname,
                            name=name,
                            password=make_password(password),
                            profile_image="default_profile.jpg")
        return Response(status = 200)
        #todo 회원가입


class Login(APIView):
    def get(self, request):
        return render(request, "user/login.html")
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = User.objects.filter(email=email).first() 
        #first가 없으면 리스트를 반환하는데 어차피 email은 unique고 하나만 필요해서 first쓰면 바로 하나만 반환
        if user is None:
            return Response(status=404, data=dict(message="회원정보가 잘못되었습니다."))
        
        if user.check_password(password):
            # TODO 로그인을 했다. 세션 or 쿠키
            request.session['email'] = email 
            #session에 email정보를 넣어준다.
            return Response(status=200)
        else:
            return Response(status=400,data=dict(message="회원정보가 잘못되었습니다."))
        
class LogOut(APIView):
    def get(self, request):
        request.session.flush()
        return render(request, "user/login.html")