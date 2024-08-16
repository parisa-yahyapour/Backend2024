from random import randint, choice
from faker import Faker
from account.models import Account
from person.models import Person
import logging
from django.db.models import F,Q
import time
from django.db.models import Sum

def GetNationalIdGreaterThanCredit():
    logger = logging.getLogger('django')
    query_result = Account.objects.filter(owner__national_id__gt = F('credit'))
    logger.debug(f'Query Result: {query_result}')




