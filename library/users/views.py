from django.shortcuts import redirect, render
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from users.forms import UserRegisterForm as UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
     return render(
        request,
        'users/profile.html'
    )

def register(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! Now you can log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    form = UserCreationForm()
    
    return render(
        request,
        'users/register.html',
        {
            'form': form
        }
    )