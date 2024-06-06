from django.contrib import admin
from .models import goods_main, supplier, in_details, out_details, person_details, home_admission, nurse_duty, user_details, login_info, dropdown_table

admin.site.register(goods_main)
admin.site.register(supplier)
admin.site.register(in_details)
admin.site.register(out_details)
admin.site.register(person_details)
admin.site.register(home_admission)
admin.site.register(nurse_duty)
admin.site.register(user_details)
admin.site.register(login_info)
admin.site.register(dropdown_table)
