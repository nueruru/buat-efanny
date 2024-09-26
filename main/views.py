from django.shortcuts import render, redirect
from main.models import UserProfile
from .forms import UserProfileForm

def video(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect ke halaman yang sama
    else:
        form = UserProfileForm()

    users = UserProfile.objects.all()  # Ambil data pengguna yang sudah di-submit
    return render(request, 'index.html', {'form': form, 'users': users})
