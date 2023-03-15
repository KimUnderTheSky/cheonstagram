"""cheonstagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import Sub
from content.views import Main, UploadFeed # content폴더 views파일의 Main class 가져오기
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', Main.as_view()),
    #path('content/upload', UploadFeed.as_view()),
    # content/upload로 호출하면 content.views에 있는 UploadFeed함수가 실행됨
    path('content/', include('content.urls')), 
    # include를 통해 다른 앱에 있는 urls를 불러올 수 있다.
    # 앱에 있는 urls를 연결할때는 앞에 content/처럼 폴더명을 넣어줘야한다. 그럼 그 안에 있는 urls사용가능.
    path('user/', include('user.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)