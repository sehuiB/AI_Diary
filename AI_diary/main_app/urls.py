from django.urls import path
from . import views
from .views import create_diary
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    
    path('emotion-tracking/', views.emotion_tracking, name='emotion_tracking'),
    path('faq/', views.faq, name='faq'),
    path('gallery/', views.gallery, name='gallery'),
    path('greet/', views.greet, name='greet'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),  # 추가 확인
    path('logout/', views.user_logout, name='logout'),
    # path("generate-image/", views.generate_image, name="generate_image"),
    # path("generate-image/", generate_diary_image, name="generate_image"),
    path('create-diary/', create_diary, name='create-diary'),
    path('create-diary/', views.create_diary, name='create_diary'),
    path('generate/', views.prompt_view, name='generate_prompt'),
    path('result/', views.result_page, name='result_page'),
    # path('diary/create/', views.create_diary, name='create_diary'),
    # path('diary/', views.diary_list, name='diary_list'),
    # path('diary/<int:entry_id>/', views.diary_detail, name='diary_detail'),
    # path('diary/<int:entry_id>/update/', views.update_diary, name='update_diary'),
    # path('diary/<int:entry_id>/delete/', views.delete_diary, name='delete_diary'),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)