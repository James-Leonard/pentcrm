from xml.dom.minidom import Document
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from leads.views import  LandingPageView #landing_page,



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('leads/', include('leads.urls', namespace="leads")),
    
]


