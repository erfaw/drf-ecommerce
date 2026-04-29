from django.db import models
from django.core import checks
from django.core.exceptions import ObjectDoesNotExist
from typing import Any, List


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
        elif self.unique_for_field not in [field.name for field in self.model._meta.get_fields()]:
            return [
                checks.Error("'unique_for_field' does not match any existing model field.")
            ]
        else: 
            return []
        
    def pre_save(self, model_instance: models.Model, add: bool) -> Any:
        if getattr(model_instance, self.attname) == None:
            try: 
                qs = self.model.objects.all() # ProductLine 
                query = {
                    self.unique_for_field: getattr(model_instance, self.unique_for_field),
                }
                qs = qs.filter(**query) 
                latest = qs.latest(self.attname)
                value = getattr(latest, self.attname) + 1                
            except ObjectDoesNotExist: 
                value = 1
            return value
        else: 
            return super().pre_save(model_instance, add)