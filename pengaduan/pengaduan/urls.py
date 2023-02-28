from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from siswa.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(IndexView.as_view(), login_url='login/'), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('tambah_aduan/', AddPengaduanView.as_view(), name='tambah_aduan'),
    path('data/', DataView.as_view(), name='data'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)