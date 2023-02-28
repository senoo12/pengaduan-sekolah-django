from django.contrib import admin
from siswa.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Biodata)
class BiodataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'nis', 'telp', 'user_id')
    readonly_fields = ('user_id',)

@admin.register(Pengaduan)
class PengaduanAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'tgl_pengaduan', 'isi_laporan', 'foto', 'status', 'tgl_tanggapan', 'tanggapan', 'user_id')
    list_editable = ('status', 'tgl_tanggapan', 'tanggapan',)
    readonly_fields = ('tgl_tanggapan', 'tanggapan', 'status')