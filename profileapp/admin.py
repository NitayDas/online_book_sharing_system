from django.contrib import admin

from .models import *

admin.site.register(UserProfile)
admin.site.register(Book)
admin.site.register(BookRequest)
