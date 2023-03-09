from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feed # 나와 같은 소스 폴더에 있는 models파일에서 Feed class를 가져올거다. 

class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by("-id") 
        #쿼리셋 = Feed 안에 있는 모든 데이터를 가져오겠다.
        # select * from content_feed랑 똑같음
        #print(feed_list)
        
        for feed in feed_list:
            print(feed.content)

        return render(request, "cheonstagram/main.html",context=dict(feeds=feed_list))
    
class UploadFeed(APIView): # UploadFeed가 cheonstagram의 url이랑 매핑이돼야함
    def post(self, request):
        file = request.data.get('file') #formdata 끄집어내는 방법.
        image = request.data.get('image')
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')
        
        print(file) # 서버측에서 데이터가 잘 들어왔는지 print로그 찍어보는 것.
        print(image)

        return Response(status = 200) 
        #response는 restFramework함수를 이미 만들어놓음 http 응답 코드 200은 성공을 뜻함
        
