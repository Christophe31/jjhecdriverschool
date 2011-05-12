#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

class Place(models.Model):
    name = models.CharField(u"nom", max_length=64)
    road = models.CharField(u"rue", max_length=64)
    town = models.CharField(u"ville", max_length=64)
    postal_code = models.CharField(u"code postal", max_length=64)
    agence = models.ForeignKey('self', verbose_name=u"agence",blank=True, null=True)

    TYPES = (
        (0, "Agence"),
        (1, "Circuit"),
        (2, "Plateau"),
    )
    type = models.IntegerField(u"type", choices=TYPES)

    class Meta:
        verbose_name = u"lieu"
        ordering = ("id",)

    def __unicode__(self):
        return u"%s %s"%(Place.TYPES[self.type], self.name)


class Formula(models.Model):
    name = models.CharField(u"nom", max_length=64)
    price = models.IntegerField(u"prix")
    custommers = models.ManyToManyField(User, verbose_name=u"clients")
    
    class Meta:
        verbose_name = u"formule"
        ordering = ("id",)

    def __unicode__(self):
        return u"Formule %s (à %s €)"%(self.name, self.price)


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
        return "%s (%s)"%(self.model, self.id)


class Event(models.Model):
    name = models.CharField(u"nom", max_length=64)
    comment = models.TextField(u"description", max_length=512)

    start = models.DateTimeField(u"debut")
    end = models.DateTimeField(u"fin")

    TYPES = (
        (0, "Revision"),
        (1, "Immobilisation"),
        (2, "Formation"),
    )
    type = models.IntegerField("Type", choices=TYPES)
    class Meta:
        verbose_name = u"Evenement"
        ordering = ("id",)

    def __unicode__(self):
        return self.name


class Formation(models.Model):
    agence = models.ForeignKey(Place, verbose_name=u"lieu", null=True)
    vehicule = models.ForeignKey(Vehicule, verbose_name=u"vehicule", null=True)
    event = models.OneToOneField(Event, verbose_name=u"evenement", null=True)
    package = models.ForeignKey(Package, verbose_name=u"forfait", null=True)

    class Meta:
        verbose_name = u"formation"
        ordering = ("id",)

    def __unicode__(self):
        return "formation du %s a %s"%(self.event.start, self.agence.name) 

# vim:set et sts=4 ts=4 tw=80:
