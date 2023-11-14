from django.db import models

class Word(models.Model):
    foreign_word = models.CharField(max_length=70, unique=True)
    translation = models.CharField(max_length=70)
    def __str__(self):
            return f"{self.foreign_word} - {self.translation}"