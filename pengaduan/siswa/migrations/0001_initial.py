# Generated by Django 4.0.6 on 2023-02-27 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pengaduan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl_pengaduan', models.DateTimeField(auto_now_add=True)),
                ('isi_laporan', models.CharField(max_length=255)),
                ('foto', models.ImageField(default=False, null=True, upload_to='media/%Y/%m/%d/')),
                ('status', models.CharField(choices=[('Belum', 'Belum'), ('Proses', 'Proses'), ('Selesai', 'Selesai')], default='Belum', max_length=15)),
                ('tgl_tanggapan', models.DateTimeField(blank=True, null=True)),
                ('tanggapan', models.CharField(blank=True, max_length=255)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Biodata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nis', models.IntegerField(max_length=5)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
