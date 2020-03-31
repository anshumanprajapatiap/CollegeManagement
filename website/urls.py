"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mypage/',FirstPage),
    path('temp/',Secondpage),
    path('students/',All_student,name = 'all_s'),
    path('colleges/',All_college,name = 'all_c'),
    path('single_detail/',single_student),
    path('page/',Home,name = 'button'),
    path('student_detail/<int:num>',Student_detail,name ='sdetail'),
path('college_detail/<int:cid>',College_detail,name ='cdetail'),
    path('add_college/',Add_college,name='add_c'),
path('add_student/',Add_student,name='add_s'),
    path('delete/<int:num>/<str:type>',Delete,name='delete'),
path('edit_student/<int:sid>/',Edit_student,name='edit_s'),
    path('',Login_form,name = 'login'),
    path('logout/',Logout,name = 'logout'),
path('signup/',Signup,name = 'signup')

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
