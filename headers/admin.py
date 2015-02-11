from django.contrib import admin
from headers.models import Url
from headers.views import get_title

def get_title_urls(self, request, queryset):
    if queryset:
        for url in queryset:                #search urls
            title = get_title(url)
            message_bit = "%s - title; %s - url" % (title, url)
            self.message_user(request, "%s" % message_bit)
get_title_urls.short_description = "Get title"

class UrlAdmin(admin.ModelAdmin):
    actions = [get_title_urls]                   #add new action get_title

admin.site.register(Url, UrlAdmin)

