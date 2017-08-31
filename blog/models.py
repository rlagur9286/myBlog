from django.db import models
import re
from django import forms


def lnglat_validator(value):
    if not re.match(r'[+-]?\d+\.?\d*, [+-]?\d+\.?\d*', value):
        raise forms.ValidationError('경도/위도를 입력 해주세요.')


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lnglat = models.CharField(max_length=50, blank=True, help_text="지도에서 선택 해주세요.", validators=[lnglat_validator])

    def __str__(self):
        return self.title

    def lng(self):
        if self.lnglat:
            return self.lnglat.split(',')[0]
        return None

    def lat(self):
        if self.lnglat:
            return self.lnglat.split(',')[1]
        return None

