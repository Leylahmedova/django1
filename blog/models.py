from django.db import models

# Create your models here.

class Blog(models.Model):
    name=models.CharField(max_length=300)
    description=models.TextField()
    price=models.FloatField()
    discount=models.FloatField(blank=True,null=True)
    
    def __str__(self):
        return self.name