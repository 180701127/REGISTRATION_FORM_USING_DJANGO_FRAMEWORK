from django.contrib import admin

# Register your models here.
from FORM_DETAILS.models import Post
# admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title','sdesc','detail','category','FirstName','LastName','gender','country_code','Mobile_No','Emailid','password','cpassword','isactive']
    list_filter=['category','isactive']
    
# registering model with model admin class
admin.site.register(Post)
admin.site.index_title = "custom Blog app Admin index"
admin.site.site_title="custom Blog App site"

