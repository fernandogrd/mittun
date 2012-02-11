from django.db.models.signals import pre_save
from django.db import models
from django.template.defaultfilters import slugify


class Event(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=250, blank=True, help_text="You must include the full url path")
    date = models.DateField()
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    slug = models.SlugField()
    logo = models.ImageField(upload_to='event_logo', blank=True, default='')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return 'event/%s' % self.slug


def generate_slug(instance, *args, **kwargs):
    instance.slug = slugify(instance.name)


pre_save.connect(generate_slug, sender=Event)
