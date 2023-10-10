from django.db import models
import datetime

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField

from streams import blocks
from users.models import Volunteer, User
from volunteerings.models import Volunteering

class ActivitieListingPage(Page):
    custom_title = models.CharField(max_length=100, blank=False, null=False, help_text="overwrites the default title")
    
    template = "activitie/activitie_listing_page.html"

    related_document = models.ForeignKey(
        'wagtaildocs.Document', blank=True, null=True,
         on_delete=models.SET_NULL, related_name='+'
    )


    content_panels = Page.content_panels + [
            FieldPanel("custom_title"),
            FieldPanel("related_document"),
        ]

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


class ActivitieDetailPage(Page):
    custom_title = models.CharField(max_length=100, blank=False, null=False, help_text="overwrites the default title")
    volunteers = models.ManyToManyField(Volunteer, related_name="activities")
    volunteering = models.ForeignKey(Volunteering, related_name="activities", on_delete=models.SET_NULL, null=True)
    activitie_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False, 
        null=True, 
        related_name="+",
        on_delete=models.SET_NULL,
    )

    activity_start_date = models.DateField(blank=True, null=True, help_text="fecha inicio de vigencia del post de la actividad")
    activity_end_date = models.DateField(blank=True, null=True, help_text="fecha inicio de vigencia del post de la actividad")

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_rich_text", blocks.RichTextBlock()),
            ("simple_rich_text", blocks.SimpleTextBlock()),
            ("meeting_point", blocks.MeetingPoint()),
            ("material_publication", blocks.MaterialPublication()),
            ("raffle", blocks.Raffle()),
            ("contacts", blocks.Contacts()),
            ("images", blocks.ImagePost()),
            ("bulletins", blocks.Bulletin()),
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
    


