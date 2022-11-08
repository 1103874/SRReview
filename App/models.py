from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.

def file_size(value):
    limit = settings.MAX_UPLOAD_FILESIZE * 1024 * 1024  # Mbytes

    if value.size > limit:
        raise ValidationError(f'첨부파일 크기가 {settings.MAX_UPLOAD_FILESIZE} Mbytes 보다 작아야 합니다.')


class SRType(models.Model):
    type = models.CharField(max_length=10, blank=False, verbose_name='SR 구분')

    def __str__(self):
        return self.type

    class Meta :
        verbose_name_plural = 'SR 구분(목록 생성)'


class SRList(models.Model):
    region = models.CharField(max_length=10, verbose_name='담당')
    dt = models.DateField(verbose_name='날짜')
    sr_type = models.ForeignKey(SRType, on_delete=models.CASCADE, verbose_name='SR 구분')
    title = models.CharField(max_length=100, verbose_name='사례명')
    description = models.TextField(verbose_name='내용 및 추진성과')
    file_upload = models.FileField(upload_to='SRList/files/%Y/%m/%d/', blank=True, validators=[file_size])
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta :
        verbose_name_plural = 'SR 사례 현황'