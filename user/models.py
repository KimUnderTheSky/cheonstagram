from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    """
        유저 프로필 사진
        유저 닉네임 -> 화면에 표기되는 이름
        유저 이름 -> 실제 사용자 이름
        유저 이메일주소 -> 회원가입할때 사용하는 아이디
        유저 비밀번호 ->
    """