from django.shortcuts import render, redirect
from django.views import View
from .models import *

class AboutView(View):
    def get(self, request):
        data = {
            "clubs" : Clubs.objects.all()
        }
        return render(request, "about.html", data)



class ClubsView(View):
    def get(self, request):
        data = {
            "clublar" : Clubs.objects.all()
        }
        return render(request, "clubs.html", data)

class PlayersView(View):
    def get(self, request, pk):
        data = {
            "players" : Players.objects.get(id=pk).club_player
        }
        return render(request, "players.html", data)


class TranferView(View):
    def get(self, request, pk):
        data = {
            "transfer": Transfer.objects.get(id=pk).players_transfers.all()
        }
        return render(request, "transfer-archive.html", data)


class U_20View(View):
    def get(self, request):
        return render("U-20players.html")


class LateTransfersView(View):
    def get(self, request):
        return render("latest-transfers.html")


class StatsView(View):
    def get(self, request):
        return render("stats.html")


class TranferArchiveView(View):
    def get(self, request):
        return render("transfer-archive.html")


class TryoutView(View):
    def get(self, request):
        return render("tryout.html")


class IndexView(View):
    def get(self, request):
        return render("index.html")


class CoursesView(View):
    def get(self, request):
        return render("courses.html")


class CountryView(View):
    def get(self, request):
        return render("country-clubs.html")




