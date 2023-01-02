from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Recipe, Comment
from django.urls import reverse, reverse_lazy
from .forms import CommentForm


class RecipeListView(ListView):
    # model we are using
    model = Recipe
    template_name = 'recipe_share/home.html'
    context_object_name = 'recipes'
    ordering = ['-date_posted']


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['recipe_name','recipe_description', 'time_to_prep', 'recipe_pic']

    # tells django who the author is of the recipe
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# does not need a template b/c it uses recipe_form template automatically
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = ['recipe_name','recipe_description']

    # tells django who the author is of the recipe
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # makes sure you can only update if you own the post
    def test_func(self):
        recipe=self.get_object()
        if self.request.user == recipe.author:
            return True
        else:
            return False

class RecipeDetailView(DetailView):
    model = Recipe

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = '/'
    # makes sure you can only update if you own the post
    def test_func(self):
        recipe=self.get_object()
        if self.request.user == recipe.author:
            return True
        else:
            return False

def home(request):
    return render(request, 'recipe_share/start.html')

def LikeView(request, pk):
    # will use the recipe_id passed from the form to get that post object from all Post objects
    post = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    # now adding a like to that post object from the current user
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('recipe_share-detail', args=[str(pk)]))

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')
    # tells django who the author is of the recipe
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
