from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from app1.views import AboutView, ClubsView, PlayersView, TranferView, LateTransfersView, StatsView, TranferArchiveView, TryoutView, IndexView, CoursesView, CountryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AboutView.as_view(), name="about"),
    path('clubs/', ClubsView.as_view(), name="clubs"),
    path('players/', PlayersView.as_view(), name="players"),
    path('transfers/', TranferView.as_view(), name="transfers"),
    path('stats/', StatsView.as_view(), name="stats"),
    path('late/', LateTransfersView.as_view(), name="latest"),
    path('archive/', TranferArchiveView.as_view(), name="archive"),
    path('tryout/', TryoutView.as_view(), name="tryout"),
    path('cours/', CoursesView.as_view(), name="courses"),
    path('index/', IndexView.as_view(), name="index"),
    path('country/', CountryView.as_view(), name="countrys"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
