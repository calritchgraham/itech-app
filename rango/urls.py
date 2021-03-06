from django.urls import path 
from rango import views


app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.ShowCategory.as_view(), name='show_category'),
    #path('add_category/', views.add_category, name='add_category'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('category/<slug:category_name_slug>/add_video/', views.add_video, name='add_video'),
    # path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    # path('logout/', views.user_logout, name='logout'),
    path('restricted/', views.restricted, name='restricted'),
    path('search/', views.search, name='search'),
    path('like_category/', views.LikeCategoryView.as_view(), name='like_category'),
    path('like_page/', views.LikePageView.as_view(), name='like_page'),
    path('like_video/', views.LikeVideoView.as_view(), name='like_video'),
    path('suggest/', views.CategorySuggestionView.as_view(), name='suggest'),
    path('all_categories/', views.AllCategories.as_view(), name='all_categories'),
    path('register_profile/', views.register_profile, name='register_profile'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('all_cat/', views.AllCategories.as_view(), name='all_cat'),
   
]