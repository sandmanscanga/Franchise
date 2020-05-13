from django.db import models


class Division(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=10)
    fullname = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
    sortkey = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Team(models.Model):
    uid = models.CharField(max_length=20)
    logo = models.CharField(max_length=40)

    ## Foreign Keys : Division, Region
    division = models.ForeignKey(
        Division,
        on_delete=models.CASCADE
    )
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.uid


class Record(models.Model):
    win = models.IntegerField()
    loss = models.IntegerField()
    draw = models.IntegerField()

    ## One to One : Team
    team = models.OneToOneField(
        Team,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return f"{self.win}-{self.loss}-{self.draw}"


class Profile(models.Model):
    abbr = models.CharField(max_length=10)
    location = models.CharField(max_length=40)
    name = models.CharField(max_length=20)
    fullname = models.CharField(max_length=60)
    divrank = models.IntegerField()

    ## One to One : Team
    team = models.OneToOneField(
        Team,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return self.fullname


class Color(models.Model):
    main = models.CharField(max_length=10)
    alt = models.CharField(max_length=10)

    ## One to One : Team
    team = models.OneToOneField(
        Team,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return f"#{self.main}, #{self.alt}"


class TeamNav(models.Model):
    home = models.CharField(max_length=80)
    stats = models.CharField(max_length=80)
    schedule = models.CharField(max_length=80)
    roster = models.CharField(max_length=80)
    depthchart = models.CharField(max_length=80)
    injuries = models.CharField(max_length=80)
    transactions = models.CharField(max_length=80)
    blog = models.CharField(max_length=80)
    logo = models.CharField(max_length=80)

    ## One to One : Team
    team = models.OneToOneField(
        Team,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return self.home


class Player(models.Model):
    uid = models.CharField(max_length=40)
    guid = models.CharField(max_length=60)
    headshot = models.CharField(max_length=80)
    shortname = models.CharField(max_length=40)
    fullname = models.CharField(max_length=60)

    ## Foreign Keys : Position, Team
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.fullname} - {self.position.name}"


class PlayerNav(models.Model):
    home = models.CharField(max_length=80)
    headshot = models.CharField(max_length=80)

    ## One to One : Player
    player = models.OneToOneField(
        Player,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return self.home


class Stat(models.Model):
    abbr = models.CharField(max_length=10)
    name = models.CharField(max_length=40)
    shortdesc = models.TextField()
    fulldesc = models.TextField()

    ## Foreign Key : Category
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.abbr


class TeamStat(models.Model):
    value = models.FloatField()
    string = models.CharField(max_length=10)

    ## Foreign Keys : Stat, Team
    stat = models.ForeignKey(
        Stat,
        on_delete=models.CASCADE
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.string


class OppStat(models.Model):
    value = models.FloatField()
    string = models.CharField(max_length=10)

    ## One to One : TeamStat
    teamstat = models.OneToOneField(
        TeamStat,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return self.string


class PlayerStat(models.Model):
    value = models.FloatField()
    string = models.CharField(max_length=10)

    ## Foreign Keys : Stat, Player, Team
    stat = models.ForeignKey(
        Stat,
        on_delete=models.CASCADE
    )
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.string
