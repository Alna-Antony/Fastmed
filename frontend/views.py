from django.shortcuts import render,redirect
from medapp.models import catdb,prodb,prescriptiondb
from frontend.models import contactdb,signupdb,cartdb,paymentdb,checkoutdb,pdfdb
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from reportlab.pdfgen import canvas






# Create your views here.
def homepg(request):
    cat = catdb.objects.all()
    return render(request,"home.html",{'cat':cat})
def storepg(request):
    cat = catdb.objects.all()
    pro = prodb.objects.all()
    return render(request,"store.html",{'pro':pro,'cat':cat})




def filterpg(request,cat_name):
    cat = catdb.objects.all()
    data=prodb.objects.filter(categoryname=cat_name)
    return render(request,"filter_product.html",{'data':data,'cat':cat})

def singlepg(request,proid):
    cat = catdb.objects.all()
    data=prodb.objects.get(id=proid)
    return render(request,"singleproduct.html",{'data':data,'cat':cat})
def aboutpg(request):
    cat = catdb.objects.all()
    return render(request,"about.html",{'cat':cat})
def contactpg(request):
    cat = catdb.objects.all()
    return render(request,"contact.html",{'cat':cat})
def savecontact(request):
    if request.method == "POST":
        fn=request.POST.get('c_fname')
        ln=request.POST.get('c_lname')
        e=request.POST.get('c_email')
        s=request.POST.get('c_subject')
        m=request.POST.get('c_message')
        obj=contactdb(firstname=fn,lastname=ln,email=e,subject=s,message=m)
        obj.save()
        return redirect(contactpg)

def reg(request):
    return render(request,"registration.html")

def saves(request):
    if request.method == "POST":
        n=request.POST.get('uname')
        e=request.POST.get('remail')
        m=request.POST.get('rmobile')
        p=request.POST.get('rpass')
        obj=signupdb(username=n,email=e,mobile=m,password=p)
        obj.save()
        return redirect(reg)

def userlogin(request):
    if request.method == "POST":
        un= request.POST.get('username')
        pwd = request.POST.get('password')
        if signupdb.objects.filter(username=un, password=pwd).exists():
            request.session['username']=un
            request.session['password']=pwd
            messages.success(request, "Login...!")
            return redirect(homepg)
        else:
            messages.warning(request, "Incorrect Password or Username...!")
            return redirect(reg)
    return redirect(reg)

def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(homepg)


def cartpg(request):
    if 'username' in request.session:
        cat = catdb.objects.all()
        data = cartdb.objects.filter(username=request.session['username'])
        total_price = 0
        for i in data:
            total_price = total_price + i.totalprice
        return render(request, "cart.html", {'data': data, 'total_price': total_price, 'cat': cat})
    else:
        return redirect(reg)


def savecarts(request):
    if request.method == "POST":
        un = request.POST.get('uname')
        pn = request.POST.get('pname')
        cn = request.POST.get('cname')
        q = request.POST.get('qnty')
        tp = request.POST.get('tprice')
        pp = request.POST.get('price')

        try:
            pres = request.FILES['prescimg']
        except MultiValueDictKeyError:
            pres = None  # or handle the missing case in a way that makes sense for your application

        obj = cartdb(username=un, productname=pn, quantity=q, totalprice=tp, price=pp, categoryname=cn, prescrip=pres)
        obj.save()
        return redirect(cartpg)


def med_search(request):
    cat = catdb.objects.all()
    query = request.GET.get('query')
    results = []

    if query:
        results = prodb.objects.filter(productname__icontains=query)



    return render(request, 'search_med.html', {'query': query, 'results': results,'cat':cat})


def cartdelete(request,pro_id):
    pro=cartdb.objects.filter(id=pro_id)
    pro.delete()
    return redirect(cartpg)


def apply_coupon(request, total_price):
    cat = catdb.objects.all()
    # Default coupon code and discount
    data = cartdb.objects.filter(username=request.session['username'])
    default_coupon_code = "DEFAULTCODE"
    default_discount = 200

    if request.method == 'POST':
        entered_coupon = request.POST.get('coupon', '')

        if entered_coupon == default_coupon_code and total_price>1000:
            total_price -= default_discount


    return render(request, 'cart2.html', {'total_price': total_price, 'data':data,'cat':cat})



def checkoutpg(request):
    # Fetch all categories
    cat = catdb.objects.all()

    if 'username' in request.session:
        # Fetch cart data for the authenticated user
        data = cartdb.objects.filter(username=request.session['username'])

        # Calculate the total price of items in the cart
        total_price = sum(item.totalprice for item in data)

        # Check if a coupon was applied
        if 'applied_coupon' in request.session:
            # If a coupon was applied, update the total_price
            applied_coupon_discount = request.session['applied_coupon_discount']
            total_price -= applied_coupon_discount

        # Render the checkout.html template with cart data, total price, and categories
        return render(request, "checkout.html", {'data': data, 'total_price': total_price, 'cat': cat})
    else:
        # Redirect to the registration page if the user is not authenticated
        return redirect('homepg')  # Adjust the URL pattern name based on your actual setup







# views.py


def forgot_password(request):
    return render(request, "forgot_password.html")


def reset_password(request):
    if request.method == 'POST':
        fe = request.POST.get('femail')
        if signupdb.objects.filter(email=fe).exists():
            # Email exists, redirect to confirmpass
            return redirect('confirmpass')  # Replace 'confirmpass' with your desired URL name
        else:
            # Email doesn't exist, redirect to the registration page
            return redirect('reg')  # Replace 'register' with your desired URL name

    # If the request method is not POST, render the initial form
    return render(request, 'forgot_password.html')


def confirmpass(request):
    return render(request,"confirm_password.html")


def update_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'confirm_password.html')

        # Assuming you have the user's email stored in the session or somewhere
        fe = request.session.get('femail')  # Adjust this based on how you store the email

        # Use filter instead of get to handle multiple instances
        users = signupdb.objects.filter(email=fe)

        if users.exists():
            # Assuming that the email is unique, use first() to get the user
            user = users.first()

            # Update the password using make_password
            user.password = make_password(new_password)
            user.save()

            messages.success(request, 'Password updated successfully.')
            return redirect('reg')  # Redirect to the login page or another page

        else:
            messages.error(request, 'User with the provided email does not exist.')
            return redirect('reg')

    return render(request, 'confirm_password.html')











def password_reset_done(request):
    return render(request, 'password_reset_done.html')


def prescr(request):
    if request.method == "POST":
        a=request.FILES['prescimg']
        obj=prescriptiondb(prescription=a)
        obj.save()
        messages.success(request, "Prescription successfully Added")
        return redirect(cartpg)

def paymentpg(request):
    data = checkoutdb.objects.filter(username=request.session['username'])
    return render(request, "payment.html", {'data': data})

def savepay(request):
    if request.method == "POST":
        cn=request.POST.get('cname')
        num=request.POST.get('cnum')
        mm=request.POST.get('expmm')
        yy=request.POST.get('expyy')
        a=request.POST.get('cvv')
        obj=paymentdb(cardnum=num,cardhold=cn,expmon=mm,expy=yy,ccvv=a)
        obj.save()
        return redirect(thank)

def thank(request):
    cat = catdb.objects.all()
    if 'username' in request.session:
        data = checkoutdb.objects.filter(username=request.session['username'])
        return render(request, "thankyou.html", {'data': data,'cat':cat})


def savecheck(request):
    if request.method == "POST":
        # Get form data
        cou = request.POST.get('c_country')
        fn = request.POST.get('c_fname')
        ln = request.POST.get('c_lname')
        use = request.POST.get('uname')
        pn_list = request.POST.getlist('pname[]')
        tp = request.POST.get('tprice')
        ad = request.POST.get('c_address')
        st = request.POST.get('c_state_country')
        em = request.POST.get('c_email_address')
        ph = request.POST.get('c_phone')

        # Validate form data (add your validation logic)

        try:
            # Save data to the database
            obj = checkoutdb(country=cou, firstname=fn, lastname=ln, username=use, productname='\n'.join(pn_list),
                             total_price=tp, address=ad, state=st, email=em, phone=ph)
            obj.save()
            return redirect('paymentpg')  # Make sure 'paymentpg' is the correct URL name
        except Exception as e:
            # Handle any exceptions (e.g., database error)
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('checkoutpg')  # Redirect to an error page



def savepdf(request):
    if request.method == "POST":
        use = request.POST.get('pdf_uname')
        fn = request.POST.get('pdf_fname')
        ln = request.POST.get('pdf_lname')
        pn_list = request.POST.getlist('pdfpname[]')  # Update the field name to match the form
        tp = request.POST.get('pdf_tprice')
        ad = request.POST.get('pdf_address')
        em = request.POST.get('pdf_email')
        mo = request.POST.get('pdf_mobile')

        # Join the list of product names into a single string with line breaks
        product_names = '\n'.join(pn_list)

        obj = pdfdb(username=use, firstname=fn, lastname=ln, productname=product_names, total_price=tp, address=ad,
                    Email=em, mobile=mo)
        obj.save()

        return redirect('thanks')  # Make sure to provide the correct URL name or path for the 'thank' view


def thanks(request):
    cat = catdb.objects.all()
    return render(request,"thankyou2.html",{'cat':cat})
def generate_dynamic_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="dynamic_report.pdf"'

    pdf = canvas.Canvas(response)
    pdf.drawString(100, 800, "DYNAMIC PDF DOCUMENT")

    if 'username' in request.session:
        pdfdb_instances = pdfdb.objects.filter(username=request.session['username'])

        for pdfdb_instance in pdfdb_instances:
            pdf.drawString(100, 750, f"UserName: {pdfdb_instance.username}")
            pdf.drawString(100, 710, f"First Name: {pdfdb_instance.firstname}")
            pdf.drawString(100, 670, f"Last Name: {pdfdb_instance.lastname}")
            pdf.drawString(100, 630, f"Product Name: {pdfdb_instance.productname}")
            pdf.drawString(100, 590, f"Address: {pdfdb_instance.address}")
            pdf.drawString(100, 550, f"TotalPrice: {pdfdb_instance.total_price}")
            pdf.drawString(100, 510, f"Mobile: {pdfdb_instance.mobile}")
            pdf.drawString(100, 470, f"Email: {pdfdb_instance.Email}")
            pdf.drawString(100, 430, f"Successfully Ordered")
            pdf.drawString(100, 400, "-" * 30)  # Separator between instances

        pdf.save()
        return response

def deleteuser(request):
    pro=cartdb.objects.filter(username=request.session['username'])
    pro.delete()
    return redirect(homepg)








