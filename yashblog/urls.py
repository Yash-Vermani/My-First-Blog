from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('AboutYash/', include('AboutYash.urls')),
    path('admin/', admin.site.urls),

]
