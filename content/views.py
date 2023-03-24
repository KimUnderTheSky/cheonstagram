from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feed, Reply, Like, Bookmark # 나와 같은 소스 폴더에 있는 models파일에서 Feed class를 가져올거다. 
from uuid import uuid4
import os
from cheonstagram.settings import MEDIA_ROOT
from user.models import User

class Main(APIView):
    
    def get(self, request):

        email = request.session.get('email', None)
        
        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email = email).first()

        if user is None:
            return render(request, "user/login.html")
        

        feed_object_list = Feed.objects.all().order_by("-id") #모든 피드를 다가져온다.
        feed_list = []
        for feed in feed_object_list: #피드를 하나씩 꺼내서
            user = User.objects.filter(email= feed.email).first() #피드를 쓴 user의 정보
            reply_object_list = Reply.objects.filter(feed_id=feed.id) #피드에 달린 댓글 전부가져오기
            reply_list = []
            for reply in reply_object_list:
                user = User.objects.filter(email=reply.email).first() # 댓글을 쓴 유저 email 가져오기
                reply_list.append(dict(feed_id = reply.feed_id,
                                       reply_content = reply.reply_content,
                                       nickname=user.nickname))
            like_count = Like.objects.filter(feed_id=feed.id, is_like=True).count()
            #Like 테이블 중에서 feed_id가 feed.id값과 같고 is_like가 True인 값의 총 개수 
            is_liked = Like.objects.filter(feed_id=feed.id, email=email,is_like=True).exists()
            #Like 테이블 중에서 feed_id가 feed.id값과 같고 email이 session에 있는 email이면서 is_like가 존재하면 exists() 존재한다.
            is_marked = Bookmark.objects.filter(feed_id=feed.id, email=email, is_marked=True).exists()
            feed_list.append(dict(id=feed.id,
                                  image=feed.image,
                                  content=feed.content,
                                  like_count=like_count,
                                  profile_image=user.profile_image,
                                  nickname=user.nickname,
                                  reply_list=reply_list,
                                  is_liked=is_liked,
                                  is_marked=is_marked,
                                  ))
        # feed를 전부가져와서 리스트에 담고 유저정보는 따로 가져와서 append해서 user정보가 바뀔때 바로 적용할 수 있다.

        #쿼리셋 = Feed 안에 있는 모든 데이터를 가져오겠다.
        # select * from content_feed랑 똑같음
        #print(feed_list)
        
        
        return render(request, "cheonstagram/main.html",context=dict(feeds=feed_list, user=user))
    
class UploadFeed(APIView): # UploadFeed가 cheonstagram의 url이랑 매핑이돼야함
    def post(self, request):
        #일단 파일 불러와
        file = request.FILES['file'] #formdata 끄집어내는 방법.

        uuid_name = uuid4().hex #랜덤하게 글자를 만들어줌 id값임
        save_path = os.path.join(MEDIA_ROOT, uuid_name) #path를 만들어주기 위해서 더함
        # ~/media/uuid4asdfasdfasdf로 저장

        with open(save_path, 'wb+') as destination: #save_path 파일을 어디에 저장할건지 경로
            for chunk in file.chunks(): # file은 file을 넣은 file변수
                destination.write(chunk)
        image = uuid_name
        content = request.data.get('content')
        email = request.session.get('email', None)
        Feed.objects.create(image=image, content=content,email = email)
        
        print(file) # 서버측에서 데이터가 잘 들어왔는지 print로그 찍어보는 것.
        print(image)

        return Response(status = 200) 
        #response는 restFramework함수를 이미 만들어놓음 http 응답 코드 200은 성공을 뜻함
        
class Profile(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        
        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email = email).first()

        if user is None:
            return render(request, "user/login.html")
        
        return render(request, "content/profile.html", context=dict(user=user))
    
class UploadReply(APIView):
        #content
    def post(self, request):
        feed_id = request.data.get('feed_id',None)
        reply_content = request.data.get('reply_content',None)
        email = request.session.get('email',None)


        Reply.objects.create(feed_id=feed_id, reply_content=reply_content, email=email)
        return Response(status=200)
    
class ToggleLike(APIView):
        #content
    def post(self, request):
        feed_id = request.data.get('feed_id',None)
        favorite_text = request.data.get('favorite_text',True)
        if favorite_text == 'favorite_border':
            is_like = True
        else:
            is_like = False
        email = request.session.get('email',None)

        like = Like.objects.filter(feed_id=feed_id, email=email).first()
        if like:
            like.is_like = is_like
            like.save()
        else:
            Like.objects.create(feed_id=feed_id, is_like=is_like, email=email)

        return Response(status=200)

class ToggleBookmark(APIView):
        #content
    def post(self, request):
        feed_id = request.data.get('feed_id',None)
        bookmark_text = request.data.get('bookmark_text',True)
        if bookmark_text == 'bookmark_border':
            is_marked = True
        else:
            is_marked = False
        email = request.session.get('email',None)

        bookmark = Bookmark.objects.filter(feed_id=feed_id, email=email).first()
        if bookmark:
            bookmark.is_marked = is_marked
            bookmark.save()
        else:
            Bookmark.objects.create(feed_id=feed_id, is_marked=is_marked, email=email)

        return Response(status=200)