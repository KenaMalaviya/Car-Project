from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import contact,Menu_price,Manufacture,Car,Booking,Profile,parking_area
# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'user_id','cost','status', )
    list_filter = ('dateTime', 'status',)

@admin.register(Booking)
class BookingAdmin_export(ImportExportModelAdmin,BookingAdmin):
    pass


    
admin.site.register(Profile)
admin.site.register(contact)
admin.site.register(Menu_price)
admin.site.register(Manufacture)
admin.site.register(Car)
# admin.site.register(Booking)
admin.site.register(parking_area)


