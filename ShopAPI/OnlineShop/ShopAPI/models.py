from django.db import models

class Token(models.Model):
    token = models.CharField(max_length=36)

    def __str__(self):
        return self.token

class Good(models.Model):

    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()
    
    def save(self, *args, **kwargs):
        if int(self.amount) <= 0:
            raise ValueError("Amount must be more than 0")
        if int(self.price) <= 0:
            raise ValueError("Price must be more than 0")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name