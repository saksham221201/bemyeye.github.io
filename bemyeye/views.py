# from django.http import HttpResponse
from unicodedata import category
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from information.models import Information
from django.core.paginator import Paginator
from information.models import Information
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def homePage(request):
    companies = Information.objects.all().values('company_name').distinct()
    print(companies)

    # for product in informationData:
    #     print(product.product_name)
    informationData = Information.objects.all()
    if request.method == "GET":
        st = request.GET.get('titlesearch')
        if st != None:
            informationData = Information.objects.filter(product_name__icontains = st)

    paginator = Paginator(informationData, 5) # adding LIMIT to the add
    page_number = request.GET.get('page') # to get from URL that which page number we are at (*By default it is set to 1*)
    informationDataFinal = paginator.get_page(page_number) # which page number data you want to show
    totalPages = informationDataFinal.paginator.num_pages # returns the total number of pages

    obj = "Text From Views"

    data = {
        'data':companies,
        'informationData':informationDataFinal,
        'lastPage':totalPages,
        'obj':obj,
        'totalPageList':[i + 1 for i in range(totalPages)]
    }
    return render(request, "home.html", data)

def home(request):
    companyData = Information.objects.all().values('company_name').distinct()
    categoryData = Information.objects.all().values('product_category').distinct()
    print(companyData)
    print(categoryData)
    data = {
        'companyData':companyData,
        'categoryData':categoryData
    }
    return render(request, "index.html", data)

def submitform(request):
    try:
        Ftitle = ""
        FcompanyName = ""
        Fdescription = ""
        Fcost = 0
        FmanuDate = ""
        FexpDate = ""
        data = {}
        if request.method == "POST":
        # title = int(request.GET.get('title'))
            title = request.POST['title']
            company = request.POST['company']
            description = request.POST['description']
            cost = request.POST['cost']
            manudate = request.POST['manudate']
            expdate = request.POST['expdate']
            Ftitle = title
            FcompanyName = company
            Fdescription = description
            Fcost = cost
            FmanuDate = manudate
            FexpDate = expdate
            data = {'Ftitle': Ftitle, 'FcompanyName':FcompanyName, 'Fdescription':Fdescription, 'Fcost':Fcost, 'FmanuDate':FmanuDate, 'FexpDate':FexpDate}
            # return HttpResponse(Ftitle + " " + FcompanyName + " " + Fdescription + " " + Fcost + " " + FmanuDate + " " + FexpDate)
            return render(request, "index.html", data)
    except:
        pass

def saveInformation(request):
    if request.method == "POST":
        title = request.POST.get('title')
        company = request.POST.get('company')
        category = request.POST.get('category')
        description = request.POST.get('description')
        cost = request.POST.get('cost')
        # product_image = request.POST.get('product_image')
        manudate = request.POST.get('manudate')
        expdate = request.POST.get('expdate')

        info = Information(product_name = title, company_name = company, product_category = category, product_description = description, product_cost = cost, manu_date = manudate, exp_date = expdate)
        info.save() # This line will save the data in the Database
        messages.success(request, "Your Item has been Saved Successfully.")
        return HttpResponseRedirect('/home')
    else:
        messages.error(request, "Error in saving the Item.")

def aboutUs(request):
    informationData = Information.objects.all().values('company_name').distinct()
    print(informationData)
    data = {'data':informationData}
    return render(request, "about.html", data)

def companyRegister(request):
    informationData = Information.objects.all().values('company_name').distinct()
    print(informationData)
    data = {'data':informationData}
    return render(request, "companyRegister.html", data)

def developers(request):
    informationData = Information.objects.all().values('company_name').distinct()
    print(informationData)
    data = {'data':informationData}
    return render(request, "developers.html", data)

def highlights(request):
    informationData = Information.objects.all().values('company_name').distinct()
    print(informationData)
    companyData = Information.objects.all().values('company_name').distinct()
    categoryData = Information.objects.all().values('product_category').distinct()
    print(companyData)
    print(categoryData)
    data = {
        'companyData':companyData,
        'categoryData':categoryData,
        'data':informationData
    }
    return render(request, "highlights.html", data)

def handleSignup(request):
    if request.method == "POST":
        signupusername = request.POST['signupusername']
        signupemail = request.POST['signupemail']
        signuppassword = request.POST['signuppassword']
        fname = request.POST['fname']
        lname = request.POST['lname']
    
        # Create a New User
        myuser = User.objects.create_user(signupusername, signupemail,signuppassword)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "User created successfully.")
        return HttpResponseRedirect("/")
    else:
        return HttpResponse("404 - Not Found")

def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')

        user = authenticate(username = loginusername, password = loginpassword)
        
        if user is not None:
            login(request, user)
            messages.success(request, "User Logged in Successfully.")
            return HttpResponseRedirect("/home")
        else:
            messages.error(request, "Invalid Credentials")
            return HttpResponseRedirect("/")
    return HttpResponse("404 - Not Found")

def handleLogout(request):
        logout(request)
        messages.success(request, "User Logged out Successfully.")
        return HttpResponseRedirect("/")