from django.contrib import admin
from users.models import Friend

class TafInline(admin.TabularInline):
	pass

class AdminFriend(admin.ModelAdmin):
	fields = ('name', 'friends')
	list_display = ('name', 'return_friend')

admin.site.register(Friend, AdminFriend)