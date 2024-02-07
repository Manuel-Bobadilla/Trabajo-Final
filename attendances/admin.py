from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Attendance


class UserAdmin(ModelAdmin):
    model = Attendance
    menu_label = "Asistencias"
    menu_icon = "placeholder"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("Voluntario", "Actividad", "Fecha",)
    search_fields = ("volunteer__user__last_name", "volunteer__user__first_name", "date",)
    
    def Voluntario(self,obj):
        return obj.volunteer
    
    def Actividad(self,obj):
        if obj.activity:
            return obj.activity
        else:
            return obj.activity_title
    
    def Fecha(self,obj):
        return obj.date

modeladmin_register(UserAdmin)
