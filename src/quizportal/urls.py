from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

     #Home Index App
    path('',include("web.urls")),

     #quiz App
    path('quiz/',include("quiz.urls")),
]

#Media Root static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
