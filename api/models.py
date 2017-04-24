from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

#계정
class Account(models.Model):
    token = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, help_text="유저 네임")
    level = models.PositiveIntegerField(default=1,validators=[ MinValueValidator(1),MaxValueValidator(30)],help_text="레벨")
    coin = models.PositiveIntegerField(help_text="보유 코인")
    exp = models.PositiveIntegerField(help_text="유저 경험치")

#문화재
class Culture(models.Model):
    title = models.CharField(max_length=100,help_text="문화재 이름")
    description = models.CharField(max_length=500,help_text="문화재 설명")
    extent = models.CharField(max_length=50, help_text="시대")
    subjectkeword = models.CharField(max_length=30, help_text="문화재 형태")
    spatial = models.CharField(max_length=30, help_text="문화재 주소")
    latitude = models.FloatField(help_text="위도")
    longtitude = models.FloatField(help_text="경도")

#업적
class Achievements(models.Model):
    token = models.ForeignKey(Account,related_name="achievements")

    ach_name = models.CharField(max_length=100, help_text="업적 이름")
    ach_case = models.CharField(max_length=100, help_text="업적 조건")
    ach_exp = models.PositiveIntegerField(default=10, help_text="업적 겸치보상")
    ach_coin = models.PositiveIntegerField(help_text="업적 코인보상")
    ach_explain = models.CharField(max_length=1000, help_text="업적 설명")

#도감
class Book(models.Model):
    token = models.ForeignKey(Account,related_name="book")

    book_name = models.CharField(max_length=100, help_text="도감 이름")
    book_image = models.CharField(max_length=300, help_text="도감 이미지")
    book_get_where = models.ForeignKey(Culture,related_name="get_where")
    book_get_when = models.CharField(max_length=30,help_text="get_when")

#오랑캐
class Barbarian(models.Model):

    name = models.CharField(max_length=100, help_text="오랑캐 이름")
    level = models.PositiveIntegerField(default=1 , validators=[ MinValueValidator(1),MaxValueValidator(30)], help_text="오랑캐 난이도 (1~30)")
    exp = models.PositiveIntegerField(default=10, validators=[ MinValueValidator(1),MaxValueValidator(1000)], help_text="오랑캐 잡으면 주는 경험치")
    money = models.PositiveIntegerField(validators=[ MinValueValidator(1),MaxValueValidator(10)], help_text="오랑캐 잡으면 주는 돈")

