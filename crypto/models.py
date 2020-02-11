from django.db import models

class Words(models.Model):
    key = models.PositiveIntegerField(unique=True)
    word = models.CharField(max_length=20)
    hint = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'word'
        verbose_name_plural = 'words'
    
    def __str__(self):
        return str(self.key)