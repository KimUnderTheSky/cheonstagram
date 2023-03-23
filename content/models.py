from django.db import models

# Create your models here.
class Feed(models.Model): # Feed라는 클래스를 만들건데 괄호 내용을 상속받겠다.
    content = models.TextField() #글내용
    image = models.TextField() #피드이미지
    email = models.EmailField(default='') # 실제 글쓴이
    like_count = models.IntegerField() # 좋아요 수

class Like(models.Model):
    feed_id = models.IntegerField(default=0) # 내가 어떤 글에 좋아요를 눌렀는지
    email = models.EmailField(default='') #좋아요를 누른 사람
    is_like = models.BooleanField(default=True)

class Reply(models.Model):
    feed_id = models.IntegerField(default=0) # 내가 어떤 컨텐츠에 대한 댓글이냐
    email = models.EmailField(default='')
    reply_content = models.TextField()

class Bookmark(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    is_marked = models.BooleanField(default=True) #아직도 걸려있는지
