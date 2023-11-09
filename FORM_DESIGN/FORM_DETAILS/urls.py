from django.contrib import admin
from django.urls import path
from django.views import View
from FORM_DETAILS import views
from FORM_DETAILS.forms import StudentForm



# from blogapp.views import NewView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home),
    path('welcome', views.welcome),
    path('itvedant', views.itvedant),
    path('add', views.add),
    path('combine/<p>',views.combine),
    # path('NewView', views.NewView.as_view()),
    path('udash/', views.udash_page),
    path('dtl/', views.view_html),
    path('about/', views.about_html),
    path('', views.index),
    path('contact/', views.contact),
    path('post/', views.post),
    path('cpost/', views.create_post,name="cpost/"),
    path('delete/<rid>', views.delete),
    path('edit/<rid>', views.edit),
    path('djform/', views.djangoform, name="djform/"),
    path('setcookie/', views.setcookies),
    path('getcookie/', views.getcookies),
    path('setsession/', views.setsessions),
    path('getsession/', views.getsession),
]

