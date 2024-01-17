from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    problem = models.TextField()

    class Meta:
        verbose_name_plural = 'contact_us'

    # list display diyei sob details show kora hoise
    # def __str__(self):
    #     return f'{self.name}'