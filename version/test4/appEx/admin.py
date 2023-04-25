from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Acc)
admin.site.register(Invested)
admin.site.register(FavoriteStock)