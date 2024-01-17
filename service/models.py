from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='service/images/')

    class Meta:
        verbose_name_plural ='Service' # eita database a j num auto plural hoye extra s add hoye jay oita singular form a niye ashe
        