from django.shortcuts import redirect, render
from django.http import request, JsonResponse
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from todolist.forms import TodoForm

def home_redirect(request):
    return redirect('/accounts')

# def new_taskilon(request):
#     return render(request, 'accounts/new_taskilon.html')
@login_required(redirect_field_name='next', login_url='accounts:login')
def new_taskilon(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            expire = form.cleaned_data['expire']
            return redirect(to='home')
        return render(request, 'accounts/new_taskilon.html', locals())
    else:
        form = TodoForm()
        return render(request, 'accounts/new_taskilon.html', {'form': form})
    return redirect(to='accounts:login')
