from django.contrib import admin
from app.models import contact
from django.contrib.auth.models import Group # this is imported to unregister group from authorization and authentication

# Register your models here.
# admin.site.register(contact)


#unregistering group 
admin.site.unregister(Group)

# customizing admin panel 
admin.site.site_header='CONTACTS'
admin.site.site_title='contact admin'
admin.site.index_title='welcome to contacts'

#changing layout/displaycx of admin panel [contacts]
class contactadmin (admin.ModelAdmin):
    list_display = ('id','name','email','phone','info','phone')
    list_editable=('info',)                                             # allows users to edit 'info' table of the user from the admin page only
    # search_fields=('name','email','phone','info','phone')               # creates a search field at the top which displays result from the ('') values
    # list_filter=('gender')                                              # creates a filter property for gender (male or female)    

admin.site.register(contact,contactadmin)