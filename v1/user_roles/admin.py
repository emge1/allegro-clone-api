from django.contrib import admin
from .models.administrator import Administrator
from .models.staff import Staff
from .models.merchant import Merchant
from .models.customer import Customer


admin.site.register(Administrator)
admin.site.register(Staff)
admin.site.register(Merchant)
admin.site.register(Customer)
