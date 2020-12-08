from django.db import models
import random
import string
from django.conf import settings


host =  settings.ALLOWED_HOSTS[-1]


# Create your models here.
class Link(models.Model):
    old_link = models.URLField()
    new_link = models.URLField()

    def save(self, *args, **kwargs):
        if not self.new_link:
            self.new_link = self.get_url()
        super(Link, self).save(*args, **kwargs)

    def get_url(self):
        current_codes = list(Link.objects.values_list(
            'new_link', flat=True))
        while True:
            new_link = self.gen_url()
            if new_link not in current_codes:
                break
            else:
                continue
        return new_link

    
    @staticmethod
    def gen_url():
        url = ''
        for i in range(4):
            url += random.choice(string.ascii_lowercase)
        return url

