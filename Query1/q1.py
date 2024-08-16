from random import randint, choice
from faker import Faker
from account.models import Account
from person.models import Person
import logging
from django.db.models import F,Q
import time
from django.db.models import Sum

def CreateSamplePerson(num):
    logger = logging.getLogger('django')
    peaple = []
    for i in range(num):
        random_first_name = Faker().first_name()
        random_last_name = Faker().last_name()
        random_national_id = randint(1000000000,10000000000)
        peaple.append(Person(name = random_first_name, last_name = random_last_name, national_id = random_national_id))
    query_result = Person.objects.bulk_create(peaple)
    logger.debug(f'Query Result: {query_result}')

def InsertAccounts(num):
    logger = logging.getLogger('django')
    peaple_list = Person.objects.all()
    accounts = []
    for i in range(num):
        random_owner = choice(peaple_list)
        random_id = randint(0,9999999999999)
        random_credit = randint(0,9999999999999)
        accounts.append(Account(owner = random_owner, account_id = random_id, credit = random_credit))
    query_result = Account.objects.bulk_create(accounts)
    logger.debug(f'Query Result: {query_result}')