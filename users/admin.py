from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Volunteer


class UserAdmin(ModelAdmin):
    model = Volunteer
    menu_label = "Voluntarios"
    menu_icon = "placeholder"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("Voluntario", "Direccion", "Telefono", "Universidad", "Legajo", "validated", "coordinador")
    search_fields = ("user__last_name", "user__first_name", "university", "university_file", "dni")

    def Voluntario(self,obj):
        return obj
    
    def Direccion(self,obj):
        return obj.address
    
    def Telefono(self,obj):
        return obj.phone
    
    def Universidad(self,obj):
        return obj.university
    
    def Legajo(self,obj):
        return obj.university_file

    def Validado(self,obj):
        return obj.validated

    def Coordinador(self,obj):
        return obj.coordinador

modeladmin_register(UserAdmin)