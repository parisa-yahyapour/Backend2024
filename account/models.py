from django.db import models

class Account(models.Model):
    owner = models.ForeignKey(to="person.Person", on_delete=models.CASCADE, null=True, related_name='accounts')
    account_id = models.PositiveBigIntegerField(null=True)
    credit = models.PositiveBigIntegerField(null=True, db_index=True)
