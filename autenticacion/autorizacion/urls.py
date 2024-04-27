from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('comment/<int:texto_id>/', views.add_comment, name='add_comment'),
    path('view_comments/<int:texto_id>/', views.view_comments, name='view_comments'),
    path('add_comment_with_texto/<int:texto_id>/', views.add_comment_with_texto, name='add_comment_with_texto'),

]