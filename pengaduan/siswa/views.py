from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from siswa.models import *
import os

# Create your views here.
class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            current_user = request.user
            username = request.user.username
            jumlah=Pengaduan.objects.all().filter(user_id=request.user).count()
            content = {
                'username': username,
                'jumlah': jumlah,
            }
        return render(request, 'index.html', content)

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password= password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                messages.success(request, 'Login Successfully, Hi Boss! 😊')
                return redirect('/admin')
            elif user.is_staff:
                messages.success(request, 'Login successfuly')
                return redirect('/admin')
            else:    
                # messages.success(request, 'Login Successfully, Hi ' + username + '!')
                return redirect('/../')
        else:
            messages.error(request, 'Invalid Username or Password!')
            return redirect('/')

def LogoutView(request):
    logout(request)
    return redirect('../login/')

class RegisterView(View):
    def post(self, request):
        if request.method=="POST":
            username=request.POST['username']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            password=request.POST['password']
            nis=request.POST['nis']
            telp=request.POST['telp']
            # user_id=request.user.id
            obj=User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            sv=Biodata.objects.create(nis=nis, telp=telp, user_id=obj)
        obj.save()
        sv.save()
        # sv.save()
        return redirect('/../')
    def get(self, request):
        return render(request, 'register.html')

class AddPengaduanView(View):
    def post(self, request):
        if request.method == "POST":
            isi_laporan = request.POST['isi_laporan']
            foto = request.FILES.get('foto')
            user_id=request.user
            obj=Pengaduan.objects.create(isi_laporan=isi_laporan, foto=foto, user_id=user_id)
        obj.save()
        return redirect('/')
    def get(self, request):
        return render(request, 'tambah_pengaduan.html')

class DataView(View):
    def get(self, request):
        pengaduan=Pengaduan.objects.all().filter(user_id=request.user)
        
        content = {
            'pengaduan': pengaduan,
            'id': id,
        }
        return render(request, 'data.html', content)
