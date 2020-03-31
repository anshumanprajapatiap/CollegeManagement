from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
from .models import *
def FirstPage(request):
    return HttpResponse("<h1>Welcome</h1>")

def Secondpage(request):
    students = ['s1','s2','s3','s4','s5']
    numbers = [12,23,45,55,90]
    x = zip(students,numbers)
    d = {"data":x}
    return render(request,'index.html',d)

def All_student(request):
    all_s = Student.objects.all()
    d = {"all_student":all_s}
    return render(request,'students.html',d)

def All_college(request):
    all_c = College.objects.all()
    d = {"all_college":all_c}
    return render(request,'all_college.html',d)

def single_student(request):
    data = Student.objects.get(id = 1)

    d = {"detail":data}
    return render(request,'single.html',d)


def Home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'home.html')

def Student_detail(request,num):
    data = Student.objects.get(id = num)
    d = {"sdata":data}
    return render(request,'student_detail.html',d)

def College_detail(request,cid):
    data = College.objects.get(id = cid)
    d = {"cdata":data}
    return render(request,'college_detail.html',d)

def Add_college(request):
    if request.method == "POST":
        d = request.POST
        n = d['clg_name']
        dn = d['dname']
        c = d['code']
        ct = d['city']
        cn = d['cn']
        College.objects.create(cname = n,director_name = dn,
                               code = c,city = ct,contact_no = cn)
        return redirect('all_c')

    return render(request,'add_college.html')

def Add_student(request):
    all_college = College.objects.all()
    d = {"all_college":all_college}
    if request.method == "POST":
        d1 = request.POST
        c = d1['clg']
        n = d1['sname']
        b = d1['bname']
        e = d1['em']
        m = d1['mob']
        a = d1['add']
        cdata = College.objects.get(id=c)
        try:
           i = request.FILES['img']
           Student.objects.create(clg=cdata, name=n, email=e,
                                  branch=b, mobile=m, address=a,
                                  image=i)
           return redirect('all_s')
        except:
            Student.objects.create(clg=cdata, name=n, email=e,
                                   branch=b, mobile=m, address=a,
                                   )
            return redirect('all_s')




    return render(request,'add_student.html',d)

def Delete(request,num,type):
    if type == 'Student':
        data = Student.objects.get(id=num)
        data.delete()
        return redirect('all_s')
    if type == 'College':
        data = College.objects.get(id=num)
        data.delete()
        return redirect('all_c')


def Edit_student(request,sid):
    all_college = College.objects.all()
    data = Student.objects.get(id = sid)
    if request.method == "POST":
        d1 = request.POST
        c = d1['clg']
        n = d1['sname']
        b = d1['bname']
        e = d1['em']
        m = d1['mob']
        a = d1['add']
        cdata = College.objects.get(id=c)
        data.name = n
        data.branch = b
        data.email = e
        data.mobile = m
        data.address =a
        data.clg = cdata
        data.save()
        try:
           i = request.FILES['img']
           data.image = i
           data.save()
        except:
            pass

    d = {"all_college": all_college,"data":data}
    return render(request,'edit_student.html',d)

from django.contrib.auth import authenticate,login,logout
def Login_form(request):
    if request.user.is_authenticated:
        return redirect('button')
    error = False
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username = u,password = p)
        if user:
            login(request,user)
            return redirect('button')
        else:
            error = True
    d = {"error":error}
    return render(request,'login.html',d)

def Logout(request):
    logout(request)
    return redirect('login')


def Signup(request):
    error = False
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        e = request.POST['em']
        f = request.POST['fname']
        l = request.POST['lname']
        user = User.objects.filter(username = u)
        if user:
            error = True
        else:
            User.objects.create_user(username=u,password=p,email=e,
                                     first_name = f,last_name = l)
            return redirect('login')
    d = {"error":error}
    return render(request,'signup.html',d)