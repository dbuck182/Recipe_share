from django.contrib import admin
from django.urls import path, include
from .views import RecipeListView, RecipeCreateView, RecipeDetailView, RecipeUpdateView, RecipeDeleteView, home, LikeView, CommentCreateView
urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe_share-home'),
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe_share-create'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_share-detail'),
    path('recipe/<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe_share-update'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe_share-delete'),
    path('homepage/', home, name='recipe_share-homepage'),
    path('like/<int:pk>', LikeView, name="like-recipe"),
    path('recipe/<int:pk>/comment', CommentCreateView.as_view(), name='recipe_share-comment')
]

