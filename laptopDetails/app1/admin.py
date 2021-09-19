from .models import Laptop
from django.contrib import admin

# Register your models here.

class laptopAdmin(admin.ModelAdmin):
    list_display=['id','company_name','model_name','Ram','rom','processor','price']

admin.site.register(Laptop,laptopAdmin)
