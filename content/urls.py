from django.urls import path
from .views  import UploadFeed, Profile # content폴더 views파일의 Main class 가져오기

urlpatterns = [
    path('upload', UploadFeed.as_view()),
    path('profile', Profile.as_view()),
    # content/upload로 호출하면 content.views에 있는 UploadFeed함수가 실행됨
]
