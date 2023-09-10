
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ChatCheck,Check
urlpatterns = [
    path('api/ChatCheck/<str:data>', ChatCheck.as_view(), name='Check'),
    path('', Check.as_view(), name='Checkpass'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
