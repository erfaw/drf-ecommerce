from django.db import models

class OrderField(models.PositiveIntegerField):
    description = "Ordering number field on a Unique field."

    def __init__(self, unique_for_field=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.unique_for_field = unique_for_field

    def check(self, **kwargs) -> list:
        return [
            *super().check(**kwargs),
            *self._check_for_field(**kwargs),
        ]
    
    def _check_for_field(self):
        pass