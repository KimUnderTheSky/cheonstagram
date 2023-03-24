from django.urls import path
from .views  import ToggleBookmark, ToggleLike, UploadFeed, Profile, UploadReply # content폴더 views파일의 Main class 가져오기

urlpatterns = [
    path('upload', UploadFeed.as_view()),
    # content/upload로 호출하면 content.views에 있는 UploadFeed함수가 실행됨
    path('reply', UploadReply.as_view()),
    path('profile', Profile.as_view()),
    path('like', ToggleLike.as_view()),
    path('bookmark', ToggleBookmark.as_view()),
]
