from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.documents import urls as wagtaildocs_urls
from activitie.views import InscriptionView, VisualizeEnrolledView, TakeAttendance, AddAttendance, AttendanceRecord
from vehicles.views import VehiclesView, AddVehicleView, DeleteVehicleView, SelectVehicleView
from volunteerings.views import Volunteerings, ViewVolunteering

from search import views as search_views

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path('', include("allauth.urls")),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    path("sitemap.xml", sitemap),
    path("inscripcion/<int:pk>", InscriptionView, name="inscripcion_post"),
    path("vehiculos/", VehiclesView, name="account_vehicle"),
    path("agregarvehiculo/", AddVehicleView, name="add_vehicle"),
    path("eliminarvehiculo/", DeleteVehicleView, name="delete_vehicle"),
    path("seleccionarvehiculo/", SelectVehicleView, name="select_vehicle"),
    path("verinscriptos/", VisualizeEnrolledView, name="ver_inscriptos"),
    path("tomarasistencia/", TakeAttendance, name="tomar_asistencia"),
    path("agregarasistencia/", AddAttendance, name="add_attendance"),
    path("historialasistencia/", AttendanceRecord, name="historial_asistencia"),
    path("voluntariados/", Volunteerings),
    path("voluntariado/", ViewVolunteering, name="ver_voluntariado"),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns = urlpatterns + [
        path('__debug__/', include('debug_toolbar.urls')),
    ] 

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
