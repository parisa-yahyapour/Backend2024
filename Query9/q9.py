from random import randint, choice
from faker import Faker
from account.models import Account
from person.models import Person
import logging
from django.db.models import F,Q
import time
from django.db.models import Sum

def GetCreditInRange():
    begin = time.time()
    logger = logging.getLogger('django')
    query_result = Account.objects.filter(Q(credit__gt = 2000000) | Q(credit__lt = 1000000))
    logger.debug(f'Query Result: {query_result}')
    end = time.time()
    print(end - begin) # without index: 0.017 with index: 0.012
