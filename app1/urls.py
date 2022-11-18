from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('student/',views.add_show,name="stu"),
    path('register/',views.register,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name="login"),
    path("open/",views.open,name="open"),
    path("table/",views.table,name="table"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("update/<int:id>",views.update,name="update"),
    path('accounts/profile/',views.profile,name="profile"),
    path('',views.home,name="home")
]
