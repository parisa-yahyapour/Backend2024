from django.db import models
from django.core.exceptions import ValidationError

def ValidateNationalID(national_id):
    if national_id < 1000000000 or national_id > 9999999999:
        raise ValidationError('Invalid National ID')

class Person(models.Model):
    name = models.CharField(max_length=63, null=True)
    last_name = models.CharField(max_length=63, null=True)
    national_id = models.PositiveBigIntegerField(validators=[ValidateNationalID])
