from datetime import datetime
from django.db import models
from django.utils import timezone
from datetime import date

class Driver(models.Model):
    icon = models.ImageField(null=True, blank=True, upload_to='statsviewers\static\statsviewers\media\img\drivers')
    en_name = models.CharField(max_length=64, blank=True, null=True)
    fr_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.en_name} ({self.fr_name})"

class Body(models.Model):
    icon = models.ImageField(null=True, blank=True, upload_to='statsviewers\static\statsviewers\media\img\drivers')
    en_name = models.CharField(max_length=64, blank=True, null=True)
    fr_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.en_name} ({self.fr_name})"

class Tire(models.Model):
    icon = models.ImageField(null=True, blank=True, upload_to='statsviewers\static\statsviewers\media\img\drivers')
    en_name = models.CharField(max_length=64, blank=True, null=True)
    fr_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.en_name} ({self.fr_name})"

class Glider(models.Model):
    icon = models.ImageField(null=True, blank=True, upload_to='statsviewers\static\statsviewers\media\img\drivers')
    en_name = models.CharField(max_length=64, blank=True, null=True)
    fr_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.en_name} ({self.fr_name})"


class Build(models.Model):
    name = models.CharField(max_length=64)
    driver = models.ManyToManyField(Driver, blank=True, null=True)
    body = models.ManyToManyField(Body, blank=True, null=True)
    tire = models.ManyToManyField(Tire, blank=True, null=True)
    glider = models.ManyToManyField(Glider, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"

    def getDriver(self):
        return str(self.driver)

class Gametype(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.name}"

class Cup(models.Model):
    icon = models.ImageField(null=True, blank=True, upload_to='statsviewers\static\statsviewers\media\img\cup')
    en_name = models.CharField(max_length=64, blank=True, null=True)
    fr_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.en_name} ({self.fr_name})"

    def tracklist(self) -> list:
        return self.track_set.all()

    def imgLink(self) -> str:
        return str(self.icon)[20:]

class Track(models.Model):
    en_name = models.CharField(max_length=64, blank=True, null=True)
    fr_name = models.CharField(max_length=64, blank=True, null=True)
    icon = models.ImageField(null=True, blank=True, upload_to='statsviewers\static\statsviewers\media\img\circuit')
    cup = models.ManyToManyField(Cup, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.en_name} ({self.fr_name})"
    def imgLink(self) -> str:
        return str(self.icon)[20:]


class Courses(models.Model):
    resultat = models.IntegerField(default=1, blank=True, null=True)
    deco = models.BooleanField(default=False, blank=True, null=True)
    number_of_bots = models.IntegerField(default=0, blank=True, null=True)
    circuit = models.ManyToManyField(Track, blank=True, null=True)
    build = models.ManyToManyField(Build, blank=True, null=True)
    gametype = models.ManyToManyField(Gametype, blank=True, null=True)
    date_course = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.date_course} - {self.resultat}th"