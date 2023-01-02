from django.shortcuts import render, redirect
from .forms import NewUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from recipe_share.models import Recipe
def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = NewUserForm()
    return render(request, 'users/register.html', {'form':form})
"""
@login_required
class UserProfileListView(ListView):
    model = Recipe
    template_name = 'users/profile.html'
    context_object_name = 'recipes'
    ordering = ['-date_posted']
    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)
"""
@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        # Now before we save we need to check forms
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
    'u_form':u_form,
    'p_form':p_form
    }
    return render(request, 'users/profile.html', context)