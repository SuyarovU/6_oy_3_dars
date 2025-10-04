from django.urls import path
from blog.views import main, blogs, about

urlpatterns = [
    path('', main),
    path('blogs/', blogs),
    path('about/', about)
]
