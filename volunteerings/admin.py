from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.admin.panels import FieldPanel
from .models import Volunteering

class CustomVolunteeringPanel(FieldPanel):
    def on_form_bound(self):
        super().on_form_bound()
        if self.instance:
            # Si el objeto ya existe (no es nuevo), oculta el campo en el formulario de edición
            self.form.fields[self.field_name].widget.can_add_related = False
            self.form.fields[self.field_name].widget.can_change_related = False
            self.form.fields[self.field_name].widget.can_delete_related = False

class VolunteeringAdmin(ModelAdmin):
    model = Volunteering
    menu_label = "Voluntariados"
    menu_icon = "placeholder"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name",)
    search_fields = ("name",)

    panels = [
        CustomVolunteeringPanel('name'),
        CustomVolunteeringPanel('description'),
        CustomVolunteeringPanel('image'),
    ]

modeladmin_register(VolunteeringAdmin)
