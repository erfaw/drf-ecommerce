from django.db import models

class OrderField(models.PositiveIntegerField):
    description = "Ordering number field on a Unique field."

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)