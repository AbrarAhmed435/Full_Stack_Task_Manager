from django.contrib import admin
from django.contrib.auth.models import User
from .models import Task
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.unregister(User)


class TaskInline(admin.TabularInline):
    model=Task
    extra=0
    fields = ['title', 'completed', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    
    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser or not (obj and obj.is_superuser)

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or not (obj and obj.is_superuser)

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or not (obj and obj.is_superuser)

class CustomUserAdmin(UserAdmin):
    list_display=['id','username','email','is_staff','is_superuser']
    search_fields=['username','email']
    list_display_links=['username']
    list_filter=['is_staff','is_superuser']
    inlines = [TaskInline]
    
    def get_queryset(self, request):
        qs=super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_superuser=False)
    
    def has_delete_permission(self, request, obj =None):
        return request.user.is_superuser
    
    def get_readonly_fields(self, request, obj=None):
        readonly = list(super().get_readonly_fields(request, obj))
        if not request.user.is_superuser:
            readonly+=['is_superuser','is_staff']  # 👈 prevent non-superusers from changing this
        return readonly
    


    
class TaskAdmin(admin.ModelAdmin):
    list_display=['id','title','user','completed','created_at']
    
    def get_queryset(self, request):
        qs=super().get_queryset(request)
        
        if request.user.is_superuser:
            return qs # super user sees everything
        
        return qs.exclude(user__is_superuser=True)
    def has_change_permission(self, request, obj =None):
        if obj:
            if request.user.is_superuser:
                return True
            return not obj.user.is_superuser # staff can't edit superuser's task
        return True
    
    def has_delete_permission(self, request, obj =None):
        if obj:
            if request.user.is_superuser:
                return True
            return not obj.user.is_superuser # staff can't edit superuser's task
        return True
    
admin.site.register(User,CustomUserAdmin)
admin.site.register(Task, TaskAdmin)
