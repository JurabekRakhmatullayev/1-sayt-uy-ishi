from django.urls import path
from .views import home_view,about_view,blog_view,gallary_view
urlpatterns = [
    path('', home_view , name= "home-page"),
    path('about/',about_view, name= "about-page"),
    path('blog/',blog_view, name= "blog-page"),
    path('gallery/',gallary_view, name= "gallary-page"),
    # path('service/',service_view,name="service-page"),

]