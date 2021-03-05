from django.contrib import admin
from .models import User, Profile, Award
# Register your models here.



 
# class ProfileAdmin(admin.ModelAdmin):
#     fields= [
#         'name',
#         'phone',
#         'location',
#         'picture',
#         ]
    
#     readonly_fields= ['createdAt', 'updatedAt',]

#     class Meta:
#         model= Profile

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Award)