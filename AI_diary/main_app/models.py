from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Django User 모델과 1:1 관계
    user_identifier = models.CharField(max_length=255, unique=True)  # 고유 사용자 ID
    email = models.EmailField(unique=True)  # 고유 이메일
    profile_info = models.JSONField(null=True, blank=True)  # 추가 프로필 정보 (JSON 형태)
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시간

    def __str__(self):
        return self.user_identifier

class DiaryEntry(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='diary_entries')
    entry_text = models.TextField()  # LLM 생성된 텍스트 저장
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Diary Entry by {self.user.user_identifier} on {self.created_at}"

class Image(models.Model):
    entry = models.OneToOneField(DiaryEntry, on_delete=models.CASCADE, related_name='image')
    style = models.CharField(max_length=50, null=True, blank=True)
    image_path = models.CharField(max_length=255)
    created_img = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for Entry {self.entry.id}"

class Statistics(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='statistics')
    emotion_count = models.JSONField()  # JSON 필드
    period = models.CharField(max_length=50)

    def __str__(self):
        return f"Statistics for {self.user.user_identifier}"

class Diary(models.Model):
    title = models.CharField(max_length=255)  # 제목
    description = models.TextField()  # 내용
    image_path = models.CharField(max_length=255, blank=True, null=True)  # 생성된 이미지 경로
    created_at = models.DateTimeField(auto_now_add=True)  # 작성 시간 자동 추가


    def __str__(self):
        return self.title