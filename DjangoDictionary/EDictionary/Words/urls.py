from django.urls import re_path, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    re_path(r'^$', views.MainView.as_view(), name='index'),
    re_path(r'add_word/$', views.WordsAdding.as_view(), name='add_word'),
    re_path(r'words_list/$', views.WordsList.as_view(), name='words_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)