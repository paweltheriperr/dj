from django.db import models

class Fen(models.Model):
    fen = models.TextField(blank=True, null=False)
    added = models.DateTimeField(auto_now_add=True)
