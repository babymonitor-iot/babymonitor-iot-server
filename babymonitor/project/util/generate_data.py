from project.service.bm_service import BabyMonitorService
from project import db
import random

max_repeat = random.randint(5, 10)

def define_type(function):
    def wrapped(type):
        global max_repeat

        if type == "fine":
            wrapped.calls = 0
            max_repeat = random.randint(5,10)
            return function('fine')

        if type == 'new':
            wrapped.calls += 1
            if wrapped.calls > max_repeat or wrapped.calls == 1:
                return function('repeat')
            else: 
                return function('new')

        if type == 'repeat':
            wrapped.calls += 1
            return function('repeat')

    wrapped.calls = 0
    return wrapped

@define_type
def generate_data(type):
    data = {}
    if type == 'fine':
        data = {
            'breathing': True,
            'sleeping': True,
            'crying': False,
            'time_no_breathing': 0
        }

    elif type == 'repeat': 
        data = BabyMonitorService(db).last_record()
        data.pop('id')
        if not data['breathing']: 
            data['time_no_breathing'] += 1
        return data

    elif type == 'new': 
        breathing = random.choices([True, False], [0.2, 0.8], k=1)
        sleeping = random.choices([True, False], None, k=1)
        crying = False if breathing else random.choices([True, False], [0.2, 0.8], k=1)
        data = {
            'breathing': breathing,
            'sleeping': sleeping,
            'crying': crying,
            'time_no_breathing': 0
        }

    BabyMonitorService(db).insert_data(data)
