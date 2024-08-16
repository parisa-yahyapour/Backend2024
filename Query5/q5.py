from random import randint, choice
from faker import Faker
from account.models import Account
from person.models import Person
import logging
from django.db.models import F,Q
import time
from django.db.models import Sum

def TransferMoney(sender_id, reciever_id, amount):
    logger = logging.getLogger('django')
    sender_account = Account.objects.get(account_id = sender_id)
    reciever_account = Account.objects.get(account_id = reciever_id)
    query_result = Account.objects.filter(account_id = sender_id).values('owner__name', 'credit')
    logger.debug(f'Query Result: {query_result}')
    query_result = Account.objects.filter(account_id = reciever_id).values('owner__name', 'credit')
    logger.debug(f'Query Result: {query_result}')
    sender_account.credit -= amount
    reciever_account.credit += amount
    sender_account.save()
    reciever_account.save()
    query_result = Account.objects.filter(account_id = sender_id).values('credit')
    logger.debug(f'Query Result: {query_result}')