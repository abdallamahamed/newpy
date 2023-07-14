from django.contrib import admin
from .models import category,cources,postcategory,post,home_interface,Price_Plans,Recommendations
from .models import contact_data,contact_information,my_contact,work_history,educational_history
# Register your models here.
admin.site.register(category)
admin.site.register(cources)
admin.site.register(postcategory)
admin.site.register(post)
admin.site.register(home_interface)
admin.site.register(Price_Plans)
admin.site.register(Recommendations)
admin.site.register(contact_information)
admin.site.register(contact_data)
admin.site.register(my_contact)
admin.site.register(work_history)
admin.site.register(educational_history)