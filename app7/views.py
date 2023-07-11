from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm,UserUpdateForm
from .models import contact,Menu_price,Manufacture,Car,Booking,Profile,parking_area
from datetime import datetime
from django.contrib import messages
import geocoder

# Create your views here.

    
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu_price(request):
    menu_price = Menu_price.objects.all()
    return render(request, 'menu_price.html', {'menu_price':menu_price})

def service(request):
    return render(request, 'service.html')



def booking(request):
    car_brands=Manufacture.objects.all()
    return render(request,'booking.html',{'car_brands':car_brands})

def Contact(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['email']
        subject = request.POST['Subject']
        message = request.POST['Message']

        Contact= contact(name=name, email=email, sub=subject, mes=message)
        Contact.save()
        messages.success(request, "Your message has been successfully sent")
        return redirect('/')
    else:
        return render(request, 'contact.html')
    return render(request, 'contact.html')

def get_json_brands_data(request):
    brand_id=request.GET.get('brand')
    cars=Car.objects.filter(m_id=brand_id)
    return render(request,'cars_dropdown_list_options.html',{'cars':cars})

def data_from_menu_price(request):
    #print("Ho gaya re ...ho gaya")
    b_id = request.GET.get('brands_menu')
    m_name=Manufacture.objects.get(m_id=b_id)
    check_price_data=Menu_price.objects.filter(brand_name=m_name)
    # print("from menu price-------------",check_price_data)
    #print("hohohohohhhhhhhhhhhhhhhhhhooooooooooooooooo  ")
    return render(request,'check_price.html',{'check_price_data':check_price_data})

# @login_required(login_url='login')
def Cust_Booking(request):
    if request.method == "POST":
        user = request.user
        car_Brand=request.POST['carBrand']
        car_name=request.POST['carName']
        cust_fname=request.POST['custfName']
        cust_lname=request.POST['custlName']
        cust_email=request.POST['Email']
        cust_mobile=request.POST['Mobile']
        dateTime =request.POST['DateTime']
        Address=request.POST['Address']
        Services =request.POST['Services']
        
        
#         string_input_with_date = "25/10/2017"
# past = datetime.strptime(string_input_with_date, "%d/%m/%Y")
# present = datetime.now()
# past.date() < present.date()
        past = datetime.strptime(dateTime,"%m/%d/%Y")
        present = datetime.now()
        
        if past.date() < present.date() :
            messages.error(request, "Please correct date")
            
        else:
            booking=Booking(user_id=user,cust_fname=cust_fname, cust_lname=cust_lname, cust_mobile=cust_mobile, Address=Address,car_name=car_name, cust_email=cust_email,car_Brand=car_Brand,dateTime=dateTime,Services=Services)
            booking.save()
            messages.success(request, "Your Booking has been successfully ")

    return redirect('/')   
    return render(request,'confirm_booking.html')

def confirm_booking(request,car):            
    booking_car= Car.objects.filter(c_name=car).first()
    bookig_brand= booking_car.m_id
    return render(request,'confirm_booking.html',{'booking_car':booking_car,'booking_brand':bookig_brand})

def search(request):
    query=request.GET['query']
    if len(query)>78:
        prices=Menu_price.objects.none()
    else:
        car=Menu_price.objects.filter(car_name__icontains=query)
        brand= Menu_price.objects.filter(brand_name__icontains=query)
        prices=car.union(brand)
        print(prices)
    if prices.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPrices': prices, 'query': query}
    return render(request, 'search.html', params)

# @login_required()
def userProfile(request):
    print(3)

    if request.method == 'POST':
        print(2)
        # u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,instance=request.user.profile)
        if p_form.is_valid():
            # u_form.save()
            p_form.save()
            messages.success(request, "Your Account Has Been Updated!")
            return redirect('userProfile')
    else:
        # u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context ={'p_form':p_form}

    return render(request,'profile.html', context)

def userProfile_edit(request):

    if request.method == 'POST':
        print(2)
        # u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,instance=request.user.profile)
        if p_form.is_valid():
            # u_form.save()
            p_form.save()
            messages.success(request, "Your Account Has Been Updated!")
            return redirect('userProfile')
    else:
        # u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context ={'p_form':p_form}

    return render(request,'profile_edit.html', context)


def booking_history(request):
    if request.user:
        user = request.user
        booking_detail=Booking.objects.filter(user_id=user)
        print(booking_detail)
        context={"booking_detail":booking_detail}
        # print("my user name is:-",myuser)
        return render(request,'history.html',context)
    else:
        return redirect('index')    

def invoice(request):
    
    if request.user:
        user = request.user
     
        booking_detail=Booking.objects.filter(user_id=user)
        print(booking_detail)
        context={"booking_detail":booking_detail}
        # print("my user name is:-",myuser)
        return render(request,'invoice.html',context)
    else:
        return redirect('index')    

def invoice_generate(request,id):
    booking_detail=Booking.objects.get(book_id=id)
    profile_details=Profile.objects.get(user=request.user)
    return render(request, 'invoice_generate.html',{'booking_detail':booking_detail,'profile_details':profile_details})


def parking_zone(request):
    if request.method == "POST":
        print("YES IT IS")
        pincode = request.POST['pincode']
        print(pincode)
        zip = parking_area.objects.filter(zipcode__iexact=pincode)
        if zip:
            print("Found")
        else:
            print("NO")
    else:
        pincode = None
        zip = parking_area.objects.none

    ipaddress = geocoder.ipinfo('me')
    post = ipaddress.latlng
    print(post)
    g = geocoder.ipinfo('me')
    g = g.postal

    template = 'parking_area.html'
    return render(request, template, {'zip': zip, 'postal': g})

    template = 'parking_area.html'
    return render(request, template)       