from django.db import models

class OrderField(models.PositiveIntegerField):
    description = "Ordering number field on a Unique field."
    