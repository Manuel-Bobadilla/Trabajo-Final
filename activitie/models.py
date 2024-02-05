from django.db import models
import datetime

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField

from streams import blocks
from users.models import Volunteer, User
from volunteerings.models import Volunteering

class ActivitieListingPage(Page):
    template = "activitie/activitie_listing_page.html"

    #related_document = models.ForeignKey(
    #    'wagtaildocs.Document', blank=True, null=True,
    #     on_delete=models.SET_NULL, related_name='+'
    #)


    content_panels = Page.content_panels 

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = ActivitieDetailPage.objects.live().public()
        context["current_date"] = datetime.date.today()
        if request.user.id:
            user = User.objects.get(id=request.user.id)
            volunteer = Volunteer.objects.filter(user = user)
            if volunteer[0].validated:
                activities = ActivitieDetailPage.objects.filter(volunteers = volunteer[0])
                vehicles = volunteer[0].vehicles.all()
                context["vehicles"] = vehicles
                context["activities"] = activities
                context["volunteer"] = volunteer[0]
                return context
        
        context["volunteer"] = None
        return context

    class Meta:
        verbose_name = "Página de listado de actividades"
        verbose_name_plural = "Páginas de listado de actividades"

ActivitieListingPage._meta.get_field("title").help_text = "Nombre de la sección, no visto por el público. Para facilitar la organización interna de las páginas"

class ActivitieDetailPage(Page):
    custom_title = models.CharField(max_length=100, blank=False, null=False, help_text="Título de la actividad")
    volunteers = models.ManyToManyField(Volunteer, related_name="activities")
    volunteering = models.ForeignKey(Volunteering, related_name="activities", on_delete=models.SET_NULL, null=True, blank=False)
    activitie_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False, 
        null=True, 
        related_name="+",
        on_delete=models.SET_NULL,
    )

    activity_start_date = models.DateField(blank=False, null=False, help_text="Fecha inicio de vigencia del post de la actividad", default=datetime.date(datetime.date.today().year, 2, 28))
    activity_end_date = models.DateField(blank=False, null=False, help_text="Fecha inicio de vigencia del post de la actividad", default=datetime.date(datetime.date.today().year, 11, 30))

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_rich_text", blocks.RichTextBlock()),
            ("simple_rich_text", blocks.SimpleTextBlock()),
        ],
        null=True, blank=True, use_json_field=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("activitie_image"),
        FieldPanel("volunteering"),
        FieldPanel("activity_start_date"),
        FieldPanel("activity_end_date"),
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"    
    
ActivitieDetailPage._meta.get_field("title").help_text = "Nombre de la sección, no visto por el público. Para facilitar la organización interna de las páginas"


