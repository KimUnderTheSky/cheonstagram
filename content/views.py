from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed # 나와 같은 소스 폴더에 있는 models파일에서 Feed class를 가져올거다. 

class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all() 
        #쿼리셋 = Feed 안에 있는 모든 데이터를 가져오겠다.
        # select * from content_feed랑 똑같음
        #print(feed_list)
        
        for feed in feed_list:
            print(feed.content)

        return render(request, "cheonstagram/main.html",context=dict(feeds=feed_list))
    