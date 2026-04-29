from django.db import models
from django.core import checks
from typing import List

class OrderField(models.PositiveIntegerField):
    description = "Ordering number field on a Unique field."

    def __init__(self, unique_for_field=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.unique_for_field = unique_for_field

    def check(self, **kwargs) -> list:
        return [
            *super().check(**kwargs),
            *self._check_for_field_attribute(**kwargs),
        ]
    
    def _check_for_field_attribute(self, **kwargs) -> List[checks.Error]:
        if self.unique_for_field is None:
            return [
                checks.Error("OrderField must define a 'unique_for_field' attribute.")
            ]
        else: 
            return []