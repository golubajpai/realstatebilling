from django.contrib import admin

# Register your models here.
from .models import User,MapImage

admin.site.register(User)
admin.site.register(MapImage)
