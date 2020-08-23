from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

#Authentication
from quiz.views.views import UserLoginView,UserLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

     #Home Index App
    path('',include("web.urls")),

    #quiz App
    path('quiz/',include("quiz.urls")),

    #user log in /Log out
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),

]

#Media Root static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
