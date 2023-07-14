from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.ama,name='ama'),
    path('cources/<int:id>', views.detail_page,name='detail'),
    path('cource/', views.list_page,name='single'),

    path('blog/<int:id>', views.detail_post,name='detail_post'),
    path('blog/', views.list_post,name='post'),


    path('contact/', views.contact,name='contact'),
    path('contact/', views.contact,name='contact'),
    path('history/', views.history,name='history'),
    


]
if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)