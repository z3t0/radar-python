from django.db import models


class Society(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Societies"


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.TextField()
    society = models.ForeignKey(
        Society,
        on_delete=models.CASCADE,
        related_name='events'
    )

    def __unicode__(self):
        return '%s' % (self.name, )
