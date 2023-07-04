from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', )

class CatAdmin(admin.ModelAdmin):
    list_display = ('category_title', 'category_slug', 'post_count',)
    search_fields = ('category_title',)
    list_per_page = 20

class TagDictAdmin(admin.ModelAdmin):
    list_display = ('tag', 'slug', 'count',)
    search_fields = ('tag',)
    list_per_page = 20

class Contact_detailsAdmin(admin.ModelAdmin):
    form = Contact_detailsForm
    list_display = ['id', 'address']
    list_per_page = 20

class PostAdmin(admin.ModelAdmin):
    list_display = ('imagealt', 'title', 'metadsc',
                    'slug', 'author', 'created_on', 'updated_on', 'status',)
    search_fields = ('title', 'post_description', 'metadsc',)
    list_filter = ('category_id',)
    list_per_page = 20

class HomeserviceshowAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    list_per_page = 20
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message',)
    search_fields = ('title', 'message',)
    list_per_page = 20


class PagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author','status',)
    search_fields = ('title', 'post_description',)
    list_per_page = 20

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body','email', 'phone', 'created_on',)
    search_fields = ('title', 'body',)
    list_per_page = 20

class SliderAdmin(admin.ModelAdmin):
    list_display = ('smalltitle', 'bigtitle')
    list_per_page = 20

class Service_publisherAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_per_page = 20

class Attractive_locationAdmin(admin.ModelAdmin):
    list_display = ('id','title','paragraph')

class Project_publisherAdmin(admin.ModelAdmin):
    list_display = ('projectstartdate', 'title', 'clientnamme')
    list_per_page = 20

class OngoingprojectAdmin(admin.ModelAdmin):
    list_display = ('village_name', 'tall', 'dist')
    list_per_page = 20

class AboutusAdmin(admin.ModelAdmin):
       list_display = ('Topheading', 'smalltitle', 'title') 
       list_per_page = 20
# Register your models here.
admin.site.register(Home, HomeAdmin)
admin.site.register(Category, CatAdmin)
admin.site.register(TagDict, TagDictAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Pages, PagesAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Service_publisher, Service_publisherAdmin)
admin.site.register(Project_publisher, Project_publisherAdmin)
admin.site.register(Homeserviceshow, HomeserviceshowAdmin)
admin.site.register(Ongoingproject, OngoingprojectAdmin)
admin.site.register(Contact_details, Contact_detailsAdmin)
admin.site.register(Aboutus,AboutusAdmin)
admin.site.register(Attractive_location, Attractive_locationAdmin)