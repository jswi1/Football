from django.db import models
class Clubs(models.Model):
    nom = models.CharField(max_length=120)
    rasm = models.FileField
    president = models.CharField(max_length=120)
    coach  = models.CharField(max_length=130)
    year = models.DateField()
    max_purchase = models.SmallIntegerField()
    max_sell = models.SmallIntegerField()
    davlat = models.CharField(max_length=50)


class Players(models.Model):
    ism = models.CharField(max_length=120)
    yosh  = models.SmallIntegerField()
    davlat = models.CharField(max_length=130)
    position  = models.CharField(max_length=120)
    narxi = models.PositiveIntegerField()
    transfer_real = models.SmallIntegerField(null=True)
    transfer_pre = models.SmallIntegerField()
    club = models.ForeignKey(Clubs , on_delete=models.CASCADE)


class Transfer(models.Model):
    name = models.CharField(max_length=150)
    club_from = models.ForeignKey(Clubs , on_delete=models.CASCADE)
    club_to = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    fee_pre = models.SmallIntegerField()
    fee_real = models.SmallIntegerField()
    season = models.CharField(max_length=200)
    player = models.ForeignKey(Players, on_delete=models.CASCADE)





