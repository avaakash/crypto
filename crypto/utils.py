import random
import datetime
from .models import Words

def random_number_generator():
    random.seed(datetime.datetime.now())
    return random.randint(1,3)

def random_word_display():
    key = random_number_generator()
    qs = Words.objects.get(key=key)
    if not qs.is_active:
        return random_word_display()
    else:
        qs.is_active = False
        qs.save()
        return qs