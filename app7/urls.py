from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('menu_price/', views.menu_price, name='menu_price'),
    path('service/', views.service, name='service'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.Contact, name='contact'),
    path('search/',views.search,name='search'),
    path('history/',views.booking_history,name='booking_history'),
    path('invoice/',views.invoice,name='invoice'),
    path('profile/',views.userProfile,name='userProfile'),
    path('profile-edit/',views.userProfile_edit,name='userProfile-edit'),
    path('check-price-from-selection/',views.data_from_menu_price,name='data-from-menu-price'),  
    path('brands-json/',views.get_json_brands_data,name='brands-json'),
    path('confirm-booking/<str:car>',views.confirm_booking,name='confirm-booking'),
    path('Cust_Booking/',views.Cust_Booking,name='Cust_Booking'),
    path('invoice_generate/<int:id>',views.invoice_generate,name='invoice_generate'),
    path('parking_area/', views.parking_zone, name="parking_zone"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)