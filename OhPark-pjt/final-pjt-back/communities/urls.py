from django.urls import path
from . import views


app_name = 'communities'
urlpatterns = [
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/like/', views.article_like),
    path('<int:article_pk>/dislike/', views.article_dislike,),
    path('<int:article_pk>/comments/', views.comment_create),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_delete)
]
