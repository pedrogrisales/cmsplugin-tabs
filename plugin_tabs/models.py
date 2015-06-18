import datetime
from django.db import models
from cms.models.fields import PlaceholderField
from cms.models.pluginmodel import CMSPlugin
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models import permalink
from django.template import defaultfilters



TEMPLATE_CHOICES = getattr(settings, 'TABSPLUGIN_TEMPLATES', (
    ('plugin_tabs/tabs.html', 'Tabs'),
    ('plugin_tabs/accordion.html', 'Accordion'),
))

DEFAULT_TEMPLATE = TEMPLATE_CHOICES[0][0]


class TabsList(CMSPlugin):
    plantilla = models.CharField('Plantilla',  max_length=255, choices=TEMPLATE_CHOICES, default=DEFAULT_TEMPLATE)

    def copy_relations(self, instances):
        super(TabsList, self).copy_relations(instances)
        for tab in instances.tabs.all().iterator():
            tab.pk = None
            tab.plugin = self
            tab.save()

    def get_template(self):
        return self.plantilla or DEFAULT_TEMPLATE


class Tab(models.Model):
    plugin = models.ForeignKey(TabsList, related_name='tabs')
    titulo = models.CharField('titulo', max_length=255)
    contenido = models.TextField(blank=False, null=True)
    orden = models.PositiveIntegerField('orden', default=1, db_index=True)

    class Meta:
        ordering = ['orden']
        verbose_name = 'Tab'
        verbose_name_plural = 'Tabs'

    def __unicode__(self):
        return unicode(self.titulo)

    def get_html_id(self):
        return 'cmsplugin_tabs_%s' % self.pk