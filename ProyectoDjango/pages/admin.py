from django.contrib import admin
from .models import Page

#Configuracion extra
class PageAdmin(admin.ModelAdmin):
    readonly_fields= ('create_at', 'update_at')
    search_fields= ('title','content')
    list_filter = ('visible',)
    list_display =  ('title','visible','create_at')
    ordering=('-create_at,')
    
# Register your models here.
admin.site.register(Page)

#Configuración del Panel de Administración
titulo= "Proyecto con Django"
subtitulo="Panel de gestión"

admin.site.site_header=titulo
admin.site.site_title=titulo
admin.site.index_title=subtitulo