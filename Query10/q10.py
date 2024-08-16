from random import randint, choice
from faker import Faker
from account.models import Account
from person.models import Person
import logging
from django.db.models import F,Q
import time
from django.db.models import Sum

def GetSumCredit():
    logger = logging.getLogger('django')
    query_result = Person.objects.annotate(total=Sum('accounts__credit'))
    logger.debug(f'Query Result: {query_result}')
