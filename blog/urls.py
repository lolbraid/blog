from django.urls import path
from . import views
from .views import PostCreateView, PostUpdateView, PostDeleteView, Like, CategoryList, category, AddCategory

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),      
    path('detail/<int:post_id>/', views.post_detail, name='detail'),
    path('new_post/', PostCreateView.as_view(), name='new_post'),
    path('detail/<slug:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('detail/<slug:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('add_category/' , AddCategory.as_view(), name = "add_category"),
    path('category/<str:cats>/', category, name = 'category'),
    path('category-list', CategoryList, name = 'category_ist'),
    path('like/<int:pk>', Like, name = 'like_post'),

]
