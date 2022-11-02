from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from form_demos2.web.views import index, create_person, list_persons

urlpatterns = [
    path('', index, name='index'),
    path('persons/', list_persons, name='list persons'),
    path('persons/create', create_person, name='create person'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)