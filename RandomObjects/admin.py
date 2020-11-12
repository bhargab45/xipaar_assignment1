from django.contrib import admin
from .models import randomobjects

class RandomObjectsAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'age')

admin.site.register(randomobjects, RandomObjectsAdmin)



