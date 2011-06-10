#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
#from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    last_code_date = models.DateField(u"date du dernier code obtenu",
                                      null=True)
    birth_date = models.DateField(u"date de naissance", null=True)
    adress = models.CharField(max_length=512, null=True)
    postal_code = models.IntegerField(null=True)
    town = models.CharField(max_length=256, null=True)
    phone_number = models.CharField(max_length=16, null=True)

    class Meta:
        permissions = (
            ("view_customers", "Lister les clients"),
        )
    TYPES = (
        (0, "Guest"),
        (1, "Customer"),
        (2, "Saleman"),
        (3, "Trainer"),
        (4, "Admin"),
    )
    type = models.IntegerField(u"type", choices=TYPES, default=0)

    def __str__(self):
        return "%s's profile" % self.user


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)


class Place(models.Model):
    name = models.CharField(u"nom", max_length=64)
    road = models.CharField(u"rue", max_length=64)
    town = models.CharField(u"ville", max_length=64)
    postal_code = models.CharField(u"code postal", max_length=64)
    agence = models.ForeignKey('self', verbose_name=u"agence",
                               blank=True, null=True)

    TYPES = (
        (0, "Agence"),
        (1, "Circuit"),
        (2, "Plateau"),
        (3, "Centre de formation"),
    )
    type = models.IntegerField(u"type", choices=TYPES)

    class Meta:
        verbose_name = u"lieu"
        ordering = ("id",)

    def __unicode__(self):
        return u"%s %s" % (dict(Place.TYPES)[self.type], self.name)


class Formula(models.Model):
    name = models.CharField(u"nom", max_length=64)
    price = models.IntegerField(u"prix")

    class Meta:
        verbose_name = u"formule"
        ordering = ("id",)

    def __unicode__(self):
        return u"Formule %s (à %s €)" % (self.name, self.price)


class Transaction(models.Model):
    customer = models.ForeignKey(User, verbose_name=u"clients",
                                  related_name=u"transactions_buyed")
    seller = models.ForeignKey(User, verbose_name=u"commercial",
                               related_name=u"transactions_selled")
    formula = models.ForeignKey(Formula, verbose_name=u"formule")
    price = models.IntegerField(u"prix")
    date = models.DateField(u"date", auto_now=True)

    class Meta:
        verbose_name = u"transaction"
        ordering = ("id",)

    @property
    def reduction(self):
        return self.price / self.formula.price * 100

    def __unicode__(self):
        return u"Vente par %s à %s pour %s €" % (self.seller.username,
                                        self.customer.username, self.price)


class Package(models.Model):
    name = models.CharField(u"nom", max_length=64)
    quantity = models.IntegerField(u"quantite")
    formula = models.ForeignKey(Formula, verbose_name=u"formule")

    TYPES = (
        (0, "type 1"),
    )
    type = models.IntegerField(u"type", choices=TYPES)

    class Meta:
        verbose_name = u"forfait"
        ordering = ("id",)

    def __unicode__(self):
        return self.name


class Vehicule(models.Model):
    model = models.CharField(u"modele", max_length=64)
    matriculation = models.CharField(u"immatriculation", max_length=64)
    agence = models.ForeignKey(Place, verbose_name=u"agence")

    TYPES = (
        (0, "Voiture"),
        (1, "Moto"),
    )
    type = models.IntegerField(u"type", choices=TYPES)

    class Meta:
        verbose_name = u"vehicule"
        ordering = ("id",)
        permissions = (
            ("view_vehicules", "Peut lister les vehicules"),
        )

    def __unicode__(self):
        return "%s (%s)" % (self.model, self.id)


class Event(models.Model):
    start = models.DateTimeField(u"debut")
    end = models.DateTimeField(u"fin")

    TYPES = (
        (0, "Maintenance"),
        (1, "Formation"),
        (2, "Disponibilité"),
    )
    type = models.IntegerField("Type", choices=TYPES)

    class Meta:
        verbose_name = u"Evenement"
        ordering = ("id",)

    def __unicode__(self):
        return "de %s à %s" % (self.start, self.end)


class Maintenance(Event):
    vehicule = models.ForeignKey(Vehicule, verbose_name=u"vehicule")

    class Meta:
        verbose_name = u"maintenance"
        ordering = ("id",)

    def __unicode__(self):
        return self.name


class CodeMark(models.Model):
    mark = models.IntegerField("note", )
    date = models.DateTimeField("heure", auto_now=True)
    user = models.ForeignKey(User, verbose_name="utilisateur noté")

    class Meta:
        verbose_name = u"note de code"
        ordering = ("date",)

    def __unicode__(self):
        return "%s de %s le %s" % (self.mark, self.user.username, self.date)


class Formation(Event):
    agence = models.ForeignKey(Place, verbose_name=u"lieu", null=True)
    vehicule = models.ForeignKey(Vehicule, verbose_name=u"vehicule", null=True)
    package = models.ForeignKey(Package, verbose_name=u"forfait", null=True)
    aptitude = models.IntegerField("aptitude relevée",
                                   choices=((i, i) for i in range(11)))

    class Meta:
        verbose_name = u"formation"
        ordering = ("id",)

    def __unicode__(self):
        return "formation du %s a %s" % (self.event.start, self.agence.name)
