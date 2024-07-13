from django.shortcuts import render

# Create your views here.
from django.db.models import Max
from .models import user_login,customer_details

def home(request):
    cl=category_master.objects.all()
    bk = book_master.objects.all()
    context={'category_list': cl,'book_list': bk}
    return render(request,"myapp/home.html",context)

def about(request):
    context={}
    return render(request,"myapp/about.html",context)

def contact(request):
    context={}
    return render(request,"myapp/contact.html",context)

def book(request):
            cl=category_master.objects.all()
            bk = book_master.objects.all()
            context={'category_list': cl,'book_list': bk}
            return render(request,"myapp/book.html",context)

def author(request):
    context={}
    return render(request,"myapp/author.html",context)



def admin_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='admin')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id

            cl=category_master.objects.all()
            bk = book_master.objects.all()
            context={'category_list': cl,'book_list': bk}
            return render(request,'./myapp/admin_home.html',context)
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/admin_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/admin_login.html',context)
    
def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return admin_login(request)
    else:
        return admin_login(request)

def admin_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        cl=category_master.objects.all()
        bk = book_master.objects.all()

        context={'category_list': cl,'book_list': bk}
        return render(request,'./myapp/admin_home.html',context)
    
def admin_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        cpasswd = request.POST.get('cpasswd')
        uname = request.session['user_name']
        try:
            ul = user_login.objects.get(uname=uname,passwd=opasswd,u_type='admin')
            if ul is not None:
                ul.passwd=npasswd
                ul.save()
                context = {'msg': 'Password Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Err Not Changed'}
            return render(request, './myapp/admin_changepassword.html', context)
    else:
        context = {'msg': ''}
        return render(request, './myapp/admin_changepassword.html', context)
    
def customer_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname=email
        #status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='customer')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        cd = customer_details(user_id=user_id,fname=fname, lname=lname, gender=gender, dob=dob,addr=addr, pin=pin, contact=contact, email=email )
        cd.save()

        print(user_id)
        context = {'msg': 'Customer Registered'}
        return render(request, 'myapp/customer_login.html',context)

    else:
        return render(request, 'myapp/customer_details_add.html')
    

from .models import category_master

def admin_category_details_add(request):
    if request.method == 'POST':
        category_name= request.POST.get('category_name')
        c_d= category_master(category_name=category_name)
        c_d.save()
        cl= category_master.objects.all()
        context={'category_list':cl,'msg':'Category Added'}
        return render(request,'myapp/admin_category_details_view.html', context)
    else:
        return render(request,'myapp/admin_category_details_add.html')
    
def admin_category_details_view(request):
    cl=category_master.objects.all()
    context={'category_list': cl}
    return render(request,'myapp/admin_category_details_view.html',context)

def admin_category_details_edit(request):
    if request.method == 'POST':
        c_id= request.POST.get('c_id')
        category_name= request.POST.get('category_name')
        cde= category_master.objects.get(id=int(c_id))
        cde.category_name=category_name
        cde.save()

        msg='Category Record updated'
        ct_l=category_master.objects.all()
        context= {'category_list': ct_l,'msg':msg}
        return render(request,'myapp/admin_category_details_view.html', context)
    else:
        id= request.GET.get('id')
        ct= category_master.objects.get(id=int(id))
        context={'category_name': ct.category_name,'c_id':ct.id}
        return render(request,'myapp/admin_category_details_edit.html', context)
    
def admin_category_details_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    cg = category_master.objects.get(id=int(id))
    cg.delete()
    msg = 'Category Removed'

    ct_l = category_master.objects.all()
    context = {'category_list': ct_l, 'msg':msg}
    return render(request, './myapp/admin_category_details_view.html', context)

def admin_customer_details_view(request):
    acd= customer_details.objects.all()
    msg=''
    if len(acd)==0:
        msg='No Users..'
        context={ 'customer_list':acd,'msg':msg }
        return render(request,'myapp/admin_customer_details_view.html',context)
    else:
        context={ 'customer_list':acd,'msg':msg }
        return render(request,'myapp/admin_customer_details_view.html',context)
    
def admin_customer_details_delete(request):
     id = request.GET.get('id')
     print('id = ' + id)
     cg = customer_details.objects.get(user_id=int(id))
     ud = user_login.objects.get(id=int(cg.user_id))
     ud.delete()
     cg.delete()
     msg = 'customer Removed'

     s_l = customer_details.objects.all()
     context = {'customer_list': s_l, 'msg': msg}
     return render(request, './myapp/admin_customer_details_view.html', context)

from .models import book_master
from django.core.files.storage import FileSystemStorage
from datetime import datetime
def admin_book_master_add(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        pic = fs.save(uploaded_file.name, uploaded_file)

        book_name = request.POST.get('book_name')
        category_name= request.POST.get('category_name')
        description = request.POST.get('description')
        price = float(request.POST.get('price'))
        stock = int(request.POST.get('stock'))
        author = request.POST.get('author')
        keywords = request.POST.get('keywords')

        status='new'

        pm = book_master(book_name=book_name,category_name=category_name, description=description, pic=pic,
                            price=price, stock=stock,author=author, keywords=keywords, status=status)
        pm.save()

        cm_l = category_master.objects.all()
        pm_l = book_master.objects.all()

        context = {'book_list': pm_l,'category_list':cm_l,'msg':'Record added'}
        return render(request, 'myapp/admin_book_master_view.html',context)

    else:
        cm_l = category_master.objects.all()
        context = {'category_list':cm_l,'msg':''}
        return render(request, 'myapp/admin_book_master_add.html',context)
    
def admin_book_master_view(request):

    pm_l = book_master.objects.all()

    cm_l = category_master.objects.all()

    context = {'book_list': pm_l, 'category_list': cm_l, 'msg': ''}
    return render(request, 'myapp/admin_book_master_view.html', context)

def admin_book_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    pm = book_master.objects.get(id=int(id))
    pm.delete()

    #seller_id = request.session['user_id']

    pm_l = book_master.objects.all()

    cm_l = category_master.objects.all()

    context ={'book_list':pm_l,'category_list': cm_l,'msg':'Record deleted'}
    return render(request,'myapp/admin_book_master_view.html', context)

def admin_book_master_stock_edit(request):
    '''
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return seller_login_check(request)
        '''

    if request.method == 'POST':
        s_id = request.POST.get('s_id')
        stock = int(request.POST.get('stock'))
        price = float(request.POST.get('price'))
        dd = book_master.objects.get(id=int(s_id))
        dd.stock = stock
        dd.price = price
        dd.save()
        msg = 'Record Updated'
        #seller_id = request.session['user_id']
        pm_l = book_master.objects.all()

        cm_l = category_master.objects.all()

        context = {'book_list': pm_l, 'category_list': cm_l, 'msg': ''}
        return render(request, 'myapp/admin_book_master_view.html', context)
    else:
        id = request.GET.get('id')
        dd = book_master.objects.get(id=int(id))
        context = {'stock': dd.stock, 'price': dd.price, 's_id': dd.id}
        return render(request, './myapp/admin_book_master_stock_edit.html',context)
    
def admin_book_master_edit(request):
    cm_l = category_master.objects.all()  # Move this line outside the if-else block

    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        pic = fs.save(uploaded_file.name, uploaded_file)

        s_id = request.POST.get('s_id')
        book_name = request.POST.get('book_name')
        category_name = request.POST.get('category_name')
        description = request.POST.get('description')
        author = request.POST.get('author')
        keywords = request.POST.get('keywords')
        
        dd = book_master.objects.get(id=int(s_id))
        dd.book_name = book_name
        dd.category_name = category_name
        dd.description = description
        dd.author = author
        dd.keywords = keywords
        dd.pic = pic
        dd.save()
        msg = 'Record Updated'	

        pm_l = book_master.objects.all()
        context = {'book_list': pm_l, 'category_list': cm_l, 'msg': msg}
        return render(request, 'myapp/admin_book_master_view.html', context)

    else:
        id = request.GET.get('book_id')
        dd = book_master.objects.get(id=int(id))
        context = {'book_name': dd.book_name, 'category_name': dd.category_name, 'description': dd.description, 'keywords': dd.keywords, 's_id': dd.id, 'category_list': cm_l}
        return render(request, './myapp/admin_book_master_edit.html', context)
    

def admin_bill_view(request):
    user_id = request.session['user_id']
    suc_l = bill_master.objects.all()
    bill_list = []
    for suc in suc_l:
        pr_l = bill_details.objects.filter(bill_id=int(suc.id))
        for pr in pr_l:
            p_l = book_master.objects.filter(id=pr.product_id)
            if len(p_l) >= 1:
                bill_list.append(suc)
                break
    ud_l = customer_details.objects.all()
    context = {'transaction_list': suc_l, 'msg': '', 'user_list': ud_l}
    return render(request, './myapp/admin_bill_view.html', context)


def admin_bill_details_view(request):
    user_id = request.session['user_id']
    bill_id = request.GET.get('bill_id')
    pr_l = bill_details.objects.filter(bill_id=int(bill_id))
    bill_list = []
    for pr in pr_l:
        p_l = book_master.objects.filter(id=pr.product_id)
        if len(p_l) >=1:
            bill_list.append(pr)
    pm_l = book_master.objects.all()
    context = {'details_list': pr_l, 'product_list': pm_l, 'msg': ''}
    return render(request, 'myapp/admin_bill_details_view.html', context)

####################################CUSTOMER#####################################################
    
def customer_login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='customer')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/customer_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/customer_login.html',context)
    else:
        return render(request, 'myapp/customer_login.html')
    
def customer_home(request):
    cl=category_master.objects.all()
    bk = book_master.objects.all()
    context = {'category_list': cl,'book_list': bk}
    return render(request,'./myapp/customer_home.html',context)

def customer_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return customer_login(request)
    else:
        return customer_login(request)
    
def customer_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/customer_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/customer_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/customer_changepassword.html', context)
    else:
        return render(request, './myapp/customer_changepassword.html')
    
def customer_contact_us(request):
    context={}
    return render(request,"myapp/customer_contact_us.html",context)


def customer_about(request):
    context={}
    return render(request,"myapp/customer_about.html",context)

def top_seller(request):
    cl=category_master.objects.all()
    bk = book_master.objects.all()
    context={'category_list': cl,'book_list': bk}
    return render(request,'myapp/top_seller.html',context)

def customer_view_more_details(request):
    cl=category_master.objects.all()
    bk = book_master.objects.all()
    context={'category_list': cl,'book_list': bk}
    return render(request,'myapp/customer_view_more_details.html',context)

def customer_book_search(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')

        bm_l = book_master.objects.filter(book_name__contains=book_name)

        cm_l = category_master.objects.all()
       

        context = {'book_list': bm_l, 'category_list': cm_l, 'msg': ''}
        return render(request, 'myapp/customer_book_search.html', context)
    else:
        return render(request, 'myapp/customer_book_search.html')
    

from .models import shopping_cart,customer_details,book_master
def customer_cart_add(request):
    # Get book_id from the query parameters
    book_id = int(request.GET.get('book_id'))

    # Get user_id from the session
    user_id = request.session.get('user_id')

    # Set other required values
    book_name = book_master.objects.get(id=book_id).book_name
    qty = 1
    dt = datetime.today().strftime('%Y-%m-%d')
    tm = datetime.today().strftime('%H:%M:%S')
    status = 'ok'

    # Create and save the shopping cart entry
    pr = shopping_cart(
        book_id=book_id,
        user_id=user_id,
        book_name=book_name,
        qty=qty,
        dt=dt,
        tm=tm,
        status=status
    )
    pr.save()

    context = {'msg': 'Added to cart'}
    return render(request, 'myapp/customer_book_search.html', context)


def customer_cart_view(request):
    user_id = request.session['user_id']
    pr_l = shopping_cart.objects.filter(user_id=int(user_id))
    pm_l = book_master.objects.all()
    context = {'cart_list': pr_l, 'book_list': pm_l, 'msg': ''}
    return render(request, 'myapp/customer_cart_view.html', context)

def customer_cart_delete(request):
    id = request.GET.get('id')

    print("id="+id)
    pp = shopping_cart.objects.get(id=int(id))
    pp.delete()

    user_id = request.session['user_id']
    pr_l = shopping_cart.objects.filter(user_id=int(user_id))
    pm_l = book_master.objects.all()
    context = {'cart_list': pr_l, 'book_list': pm_l, 'msg': 'Deleted'}
    return render(request, 'myapp/customer_cart_view.html', context)

def customer_cart_quantity_edit(request):
    if request.method == 'POST':
        c_id= request.POST.get('c_id')
        qty= request.POST.get('qty')
        cde= shopping_cart.objects.get(id=int(c_id))
        cde.qty=qty
        cde.save()

        msg='Quantity Record updated'
        ct_l=shopping_cart.objects.all()
        pm_l = book_master.objects.all()
        context= {'cart_list': ct_l,'book_list': pm_l,'msg':msg}
        return render(request,'myapp/customer_cart_view.html', context)
    else:
        id= request.GET.get('id')
        ct= shopping_cart.objects.get(id=int(id))
        context={'qty': ct.qty,'c_id':ct.id}
        return render(request,'myapp/customer_cart_quantity_edit.html', context)
    
from .models import bill_master,bill_details, payment_master
from django.db.models import Sum
from django.db.models import Max
from django.db.models import F

def customer_payment_add(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        amt = request.POST.get('amt')
        card_no = request.POST.get('card_no')
        cvv = request.POST.get('cvv')

        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'ok'

        pm_l = book_master.objects.all()
        user = customer_details.objects.get(user_id=int(user_id))

        # Create a bill for the user
        bm = bill_master(user_id=int(user_id), bill_no='bno', bill_addr=user.addr,
                         total_amt=float(amt), dt=dt, tm=tm)
        bm.save()

        # Fetch the created bill_id
        bill_id = bm.id

        # Create a payment record
        pm = payment_master(bill_id=bill_id, user_id=int(user_id), amt=float(amt),
                            card_no=card_no, cvv=cvv, dt=dt, tm=tm, status='ok')
        pm.save()

        pr_l = shopping_cart.objects.filter(user_id=int(user_id))
        for pr in pr_l:
            pm = book_master.objects.get(id=pr.book_id)
            if pm.stock >= pr.qty:  # Check if there is enough stock
                amt =float(amt) + pm.price * pr.qty
                pm.stock = F('stock') - pr.qty
                pm.save()
                bd = bill_details(bill_id=bill_id, product_id=pm.id, qty=pr.qty, amt=pm.price * pr.qty)
                bd.save()
                sc = shopping_cart.objects.get(id=pr.id)
                sc.delete()

        sc_l = shopping_cart.objects.filter(user_id=int(user_id))
        context = {'cart_list': sc_l, 'book_list': pm_l, 'msg': 'Payment successfully done'}
        return render(request, 'myapp/customer_cart_view.html', context)

    else:
        user_id = request.session['user_id']
        pr_l = shopping_cart.objects.filter(user_id=int(user_id))
        cart_list = []
        pm_l = book_master.objects.all()
        amt = 0.0
        for pr in pr_l:
            pm = book_master.objects.get(id=pr.book_id)
            if pm.stock >= pr.qty:
                amt += pm.price * pr.qty
                cart_list.append(pr)
        context = {'cart_list': cart_list, 'book_list': pm_l, 'msg': '', 'amt': amt}
        return render(request, './myapp/customer_payment_add.html', context)
    
def customer_payment_view(request):
    user_id = request.session['user_id']
    suc_l = payment_master.objects.filter(user_id=int(user_id))
    ud_l = customer_details.objects.all()
    context = {'transaction_list': suc_l, 'msg': '', 'user_list': ud_l}
    return render(request, './myapp/customer_payment_view.html', context)

def customer_bill_view(request):
    user_id = request.session['user_id']
    suc_l = bill_master.objects.filter(user_id=int(user_id))
    ud_l = customer_details.objects.all()
    context = {'transaction_list': suc_l, 'msg': '', 'user_list': ud_l}
    return render(request, './myapp/customer_bill_view.html', context)

def customer_bill_details_view(request):
    user_id = request.session['user_id']
    bill_id = request.GET.get('bill_id')
    pr_l = bill_details.objects.filter(bill_id=int(bill_id))
    pm_l = book_master.objects.all()
    context = {'details_list': pr_l, 'product_list': pm_l, 'msg': ''}
    return render(request, 'myapp/customer_bill_details_view.html', context)


