from os import name
from this import d
from tkinter import RIDGE
from django.shortcuts import redirect, render, HttpResponse
from FORM_DETAILS.forms import StudentForm
from FORM_DETAILS.models import Post



# Create your views here.
def home(request):
    # return HttpResponse("Hello from home")
    return redirect('/udash')

def welcome(request):
    return HttpResponse("Welcome to django")

def itvedant(request):
    return HttpResponse("Welcome to itvedant, chennai")

def add(request):
    x=10
    y=5
    z=(x+y)
    return HttpResponse(z)

def combine(request,p):
    return HttpResponse("Good morning" + p)


# class based view

'''class NewView(view):
    def display(self,request):
        return HttpResponse("Output from CBV")'''
    
def udash_page(request):
    return render(request,'udash.html')

def view_html(request):
    # d={'name': 'itvedant','location': 'chennai', 'batch': 'Django'}
    d = {}
    #d['x']= 10
    #d['da'] = [100,200,300,400]
    # d['name'] = 'itvedant'
    return render(request,'udash.html', d)
def about_html(request):
    return render(request,'about.html')
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def post(request):
    return render(request,'post.html')
def create_post(request):
    if request.method=="POST":
            
       
        a = request.POST['ptitle']
        b = request.POST['sdesc']
        c = request.POST['det']
        d = request.POST['cat']
        e = request.POST['FirstName']
        f = request.POST['LastName']
        g = request.POST['gender']
        h = request.POST['country_code']
        i = request.POST['Mobile_No']
        k = request.POST['Emailid']
        l = request.POST['password']
        m = request.POST['cpassword']
        o = request.POST['pactive']
        # create orm query
        # ob = modelname.objects.create(dm1=v1, dm2=v2,...)
        P = Post.objects.create(title=a,sdesc=b,detail=c,category=d,FirstName=e,LastName=f,gender=g,country_code=h,Mobile_No=i,Emailid=k,password=l,cpassword=m,isactive=o)
        P.save
        return redirect("/udash")
    
    else:
        print("In get section")
    return render(request,'create_post.html')

def udash_page(request):  
    rec= Post.objects.all()
    # print(rec)
    content = {'data': rec}
    return render(request,'udash.html', content)

def delete(request,rid):
    P= Post.objects.get(id=rid)
    P.delete()
    return redirect('/udash')


# TODO Rename this here and in `edit`
def edit(request,rid):
    # sourcery skip: extract-method, merge-dict-assign, remove-unnecessary-else
    if request.method=="POST":
        a = request.POST['ptitle']
        b = request.POST['sdesc']
        c = request.POST['det']
        d = request.POST['cat']
        e = request.POST['FirstName']
        f = request.POST['LastName']
        g = request.POST['gender']
        h = request.POST['country_code']
        i = request.POST['Mobile_No']
        k = request.POST['Emailid']
        l = request.POST['password']
        m = request.POST['cpassword']
        o = request.POST['pactive']
        # create orm query
        # ob = modelname.objects.create(dm1=v1, dm2=v2,...)
        P = Post.objects.filter(id=rid)
        P.update(title=a,sdesc=b,detail=c,category=d,FirstName=e,LastName=f,gender=g,country_code=h,Mobile_No=i,Emailid=k,password=l,cpassword=m,isactive=o)
        return redirect("/udash")
        

    else:
        P = Post.objects.filter(id=rid)
        con= {}
        con['data'] = P
        return render(request,'edit.html', con)
    

        
    
        
    # return Httpresponse("the id to be edited is "+rid)


    
def djangoform(request):
    fo=StudentForm()
    content={}
    content['form']= fo
    return render(request,'djform.html',content)


def setcookies(request):
    res = render(request,'setcookie.html') # store response object in res
    res.set_cookie('name','itvedant')
    res.set_cookie('per',89.0)
    return res

def getcookies(request):
    content={}
    content['n'] = request.COOKIES['name']
    content['p'] = request.COOKIES['per']

    return render(request,'getcookies.html', content)

def setsessions(request):
    request.session['username'] = "ITVEDANT"
    request.session['password'] = "Tn22cp8492()@"

    return render(request,'setsession.html')

def getsession(request):
    data = {}
    data['name']=request.session['username']
    data['pass']=request.session['password']
    return render(request,'getsession.html', data)


