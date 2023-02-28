from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Biodata(models.Model):
    nis = models.IntegerField(max_length=5, unique=True)
    telp = models.CharField(max_length=15, unique=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
        

class Pengaduan(models.Model):
    B = 'Belum'
    T = 'Tidak Valid'
    P = 'Proses'
    S = 'Selesai'

    status = (
        (B, B),
        (T, T),
        (P, P),
        (S, S),
    )

    tgl_pengaduan = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    isi_laporan = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='media/%Y/%m/%d/', null=True, default=False)
    status = models.CharField(max_length=15, choices=status, default=B)
    tgl_tanggapan = models.DateTimeField(blank=True, null=True)
    tanggapan = models.CharField(max_length=255, blank=True)