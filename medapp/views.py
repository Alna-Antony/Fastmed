from django.shortcuts import render,redirect
from medapp.models import catdb,prodb,prescriptiondb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from frontend.models import contactdb
from frontend.models import cartdb
from frontend.views import cartpg

# Create your views here.
def medpg(request):
    return render(request,"index.html")
def addcat(request):
    return render(request,"add_category.html")

def savedata(request):
    if request.method == "POST":
        cn=request.POST.get('cname')
        cd=request.POST.get('cdes')
        ci=request.FILES['cimg']
        obj=catdb(categoryname=cn,description=cd,categoryimage=ci)
        obj.save()
        return redirect(addcat)

def catdisplay(request):
    cat=catdb.objects.all()
    return render(request,"dis_category.html",{'cat':cat})

def catedit(request,catid):
    cat=catdb.objects.get(id=catid)
    return render(request,"edit_category.html",{'cat':cat})
def catupdate(request,catid):
    if request.method == "POST":
        cn=request.POST.get('cname')
        cd=request.POST.get('cdes')
        try:
            img=request.FILES['cimg']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=catdb.objects.get(id=catid).categoryimage
        catdb.objects.filter(id=catid).update(categoryname=cn,description=cd,categoryimage=file)
        return redirect(catdisplay)

def catdelete(request,catid):
    cat=catdb.objects.filter(id=catid)
    cat.delete()
    return redirect(catdisplay)


def addpro(request):
    cat=catdb.objects.all()
    return render(request,"add_product.html",{'cat':cat})
def savesprod(request):
    if request.method == "POST":
        cn=request.POST.get('cname')
        pn=request.POST.get('pname')
        pdes=request.POST.get('pdes')
        pp=request.POST.get('pprice')
        pi=request.FILES['pimg']
        obj=prodb(categoryname=cn,productname=pn,productdescription=pdes,productprice=pp,productimage=pi)
        obj.save()
        return redirect(addpro)

def prodisplay(request):
    pro=prodb.objects.all()
    return render(request,"dis_product.html",{'pro':pro})

def proedit(request,proid):
    pro=prodb.objects.get(id=proid)
    cat=catdb.objects.all()
    return render(request,"edit_product.html",{'pro':pro,'cat':cat})

def proupdate(request,proid):
    if request.method == "POST":
        cn=request.POST.get('cname')
        pn=request.POST.get('pname')
        pp=request.POST.get('pprice')
        pdes = request.POST.get('pdes')
        try:
            img=request.FILES['pimg']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=prodb.objects.get(id=proid).productimage
        prodb.objects.filter(id=proid).update(categoryname=cn,productname=pn,productprice=pp,productdescription=pdes,productimage=file)
        return redirect(prodisplay)

def prodelete(request,proid):
    pro=prodb.objects.filter(id=proid)
    pro.delete()
    return redirect(prodisplay)

def admins(request):
    return render(request,"adminlogin.html")

def adminlogin(re):
    if re.method =="POST":
        un=re.POST.get('username')
        pwd=re.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            user=authenticate(username=un,password=pwd)
            if user is not None:
                login(re,user)
                re.session['username']=un
                re.session['password']=pwd
                return redirect(medpg)
            else:
                return redirect(admins)
        else:
            return redirect(admins)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admins)
def contactdis(request):
    con = contactdb.objects.all()
    return render(request,"dis_contacts.html",{'con':con})
def cartdis(request):
    cart=cartdb.objects.all()
    return render(request,"dis_cart.html",{'cart':cart})

