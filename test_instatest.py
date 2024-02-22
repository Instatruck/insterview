from collections import Counter
from decimal import Decimal
import pandas as pd

from handlers import jobs


# Tests for insterview

## 1.
## Below is a master list of items. Then there are 2 tests containing more lists.
## One test contains a list where all items in the list are within the master list
## The other test contains a list where not all of the items are in the master list.
## Implement the 'contains_all_items' function in 3 different ways so that the tests pass.
MASTER_LIST = [ 'Cat', 'Dog', 'Apple', 'Bear', 'Goat', 'Fish', 'Elephant',
  'Quokka', 'Unicorn', 'Impala', 'Walrus', 'Yak', 'Giraffe', 'Zebra', 'Narwhal',
  'Rhinceros', 'Vulture', 'Tiger', 'Kangaroo', 'Lion', 'Sloth', 'Jaguar', 'Ostrich']

### Method 1: procedural
def contains_all_items_1(test_list):
    for item in test_list:
        if item not in MASTER_LIST:
            return False
    return True

### Method 2: use built-in all() function --> Preferred
### I think this way is the best because:
### - Has same performance with method 1, and faster than method 3 (computed with bigger input)
### - Leverage all benefits of using built-in functions (improve readability, efficiency,...)
def contains_all_items_2(test_list):
    return all(item in MASTER_LIST for item in test_list)

### Method 3: this way is slower due to the overhead of converting list() to set()
def contains_all_items_3(test_list):
    return set(test_list).issubset(set(MASTER_LIST))

def test_list_contains_multiple_items():
    test_list = ['Apple', 'Jaguar', 'Bear', 'Fish', 'Narwhal']
    assert contains_all_items_1(test_list) == True
    assert contains_all_items_2(test_list) == True
    assert contains_all_items_3(test_list) == True

def test_list_does_not_contains_all_items():
    test_list = ['Apple', 'Jaguar', 'Buffalo', 'Fish', 'Nightingale']
    assert contains_all_items_1(test_list) == False
    assert contains_all_items_2(test_list) == False
    assert contains_all_items_3(test_list) == False


## 2.
## Below is a master list of addresses for a customer from a database
## Implement the 'most_frequent' function to provide the top 3 most frequent addresses in 3 different ways

ADDRESS_LIST = [
 '321 Oak Street, Perth, WA',
 '334 Sunset Avenue, Darwin, NT',
 '654 Cedar Lane, Gold Coast, QLD',
 '789 Maple Drive, Brisbane, QLD',
 '789 Maple Drive, Brisbane, QLD',
 '1122 Beach Road, Cairns, QLD',
 '123 Fake Street, Sydney, NSW',
 '789 Maple Drive, Brisbane, QLD',
 '789 Maple Drive, Brisbane, QLD',
 '334 Sunset Avenue, Darwin, NT',
 '321 Oak Street, Perth, WA',
 '123 Fake Street, Sydney, NSW',
 '654 Cedar Lane, Gold Coast, QLD',
 '654 Cedar Lane, Gold Coast, QLD',
 '321 Oak Street, Perth, WA',
 '1122 Beach Road, Cairns, QLD',
 '654 Cedar Lane, Gold Coast, QLD',
 '789 Maple Drive, Brisbane, QLD',
 '1122 Beach Road, Cairns, QLD',
 '321 Oak Street, Perth, WA',
 '123 Fake Street, Sydney, NSW'
]

### Method 1: use built-in function sorted()
def most_frequent_1(address_list):
    address_frequency_table = dict()
    for address in address_list:
        if address in address_frequency_table:
            address_frequency_table[address] += 1
        else:
            address_frequency_table[address] = 1
    sorted_address_list = sorted(address_frequency_table.items(), key=lambda item: item[1], reverse=True)

    return [
        sorted_address_list[0][0],
        sorted_address_list[1][0],
        sorted_address_list[2][0],
    ]

### Method 2: use built-in function max()
def most_frequent_2(address_list):
    address_frequency_table = dict()
    for address in address_list:
        if address in address_frequency_table:
            address_frequency_table[address] += 1
        else:
            address_frequency_table[address] = 1
    
    most_frequent_address = max(address_frequency_table.items(), key=lambda item: item[1])[0]

    del address_frequency_table[most_frequent_address]
    second_most_frequent_address = max(address_frequency_table.items(), key=lambda item: item[1])[0]

    del address_frequency_table[second_most_frequent_address]
    third_most_frequent_address = max(address_frequency_table.items(), key=lambda item: item[1])[0]

    return [
        most_frequent_address,
        second_most_frequent_address,
        third_most_frequent_address,
    ]

### Method 3: use Counter.most_common() method --> Preferred
### I think this way is the best because:
### - Significantly faster than method 1 and method 2 when the ADDRESS_LIST is bigger
### - Less code, increase readability
def most_frequent_3(address_list):
    return [item[0] for item in Counter(address_list).most_common(3)]

def test_get_most_frequent():
    expected = ['789 Maple Drive, Brisbane, QLD', '321 Oak Street, Perth, WA', '654 Cedar Lane, Gold Coast, QLD']
    assert most_frequent_1(ADDRESS_LIST) == expected
    assert most_frequent_2(ADDRESS_LIST) == expected
    assert most_frequent_3(ADDRESS_LIST) == expected


## 3.
## Below is a master list of output from a database, of the jobs of a customer.
## The user needs to know the total price information, so the data needs to be transformed.
## There are 2 functions below which need completing. One transforms the information for one truck type.
## The other gives a summary of all truck types.
## Write the tests for the expected output of each function, including any parameters. Then write
## each function in 2 different ways, so the the tests beneath pass.

DB_OUTPUT = [
  { "id": 1, "date": "2022-02-15T08:24:57", "price_cents": 12775, "surcharge_cents": 1000, "tax_percent": 10, "truck_type": "Van"  },
  { "id": 2, "date": "2022-02-10T20:46:29", "price_cents": 6414,  "surcharge_cents": 300,  "tax_percent": 10, "truck_type": "Ute"  },
  { "id": 3, "date": "2022-02-12T17:30:01", "price_cents": 7146,  "surcharge_cents": 300,  "tax_percent": 10, "truck_type": "Pantech" },
  { "id": 4, "date": "2022-02-18T14:18:07", "price_cents": 3771,  "surcharge_cents": 500,  "tax_percent": 10, "truck_type": "Ute"  },
  { "id": 6, "date": "2022-02-08T09:56:42", "price_cents": 11893, "surcharge_cents": 0,    "tax_percent": 10, "truck_type": "Pantech" },
  { "id": 7, "date": "2022-02-21T06:42:52", "price_cents": 5490,  "surcharge_cents": 500,  "tax_percent": 10, "truck_type": "Van" },
  { "id": 8, "date": "2022-02-19T05:37:13", "price_cents": 4542,  "surcharge_cents": 300,  "tax_percent": 10, "truck_type": "Ute" },
  { "id": 9, "date": "2022-02-22T10:15:38", "price_cents": 6305,  "surcharge_cents": 300,  "tax_percent": 10, "truck_type": "Van" },
  { "id": 11,"date": "2022-02-06T19:24:01", "price_cents": 1684,  "surcharge_cents": 500,  "tax_percent": 10, "truck_type": "Pantech" },
  { "id": 13,"date": "2022-02-11T11:52:16", "price_cents": 7628,  "surcharge_cents": 0,    "tax_percent": 10, "truck_type": "Ute" },
  { "id": 14,"date": "2022-02-07T16:39:55", "price_cents": 3942,  "surcharge_cents": 0,    "tax_percent": 10, "truck_type": "Van" }
]

### Utility function
### Use Decimal object for monetary values to maximize the precision
def get_job_price(job):
    price = (Decimal(job["price_cents"]) + Decimal(job["surcharge_cents"])) * ((Decimal(100) + Decimal(job["tax_percent"])) / Decimal(100)) / Decimal(100)
    return price

### Method 1: use built-in functions filter(), map()
### This method is slower than method 2 due to overhead of converting map() to list()
def job_price_for_truck_type_1(job_list, truck_type):
    filtered_job_list = filter(lambda job: job["truck_type"] == truck_type, job_list)
    price_list = list(map(
        lambda job: {
            "id": job["id"],
            "price": get_job_price(job).quantize(Decimal('.01'))
        },
        filtered_job_list
    ))

    return price_list

### Method 2: use list comprehensive only --> Preferred
### I think this way is better because:
### - Faster than method 1 because of less overhead
### - Shorter, more readable
def job_price_for_truck_type_2(job_list, truck_type):
    filtered_job_list = [job for job in job_list if job['truck_type'] == truck_type]
    return [{ 'id': job['id'], 'price': get_job_price(job).quantize(Decimal('.01')) } for job in filtered_job_list]

### Method 1: procedural --> Preferred
### In this case, this method is faster than method 2 because of using Python type Decimal()
def total_price_by_truck_1(job_list):
    price_table = dict()
    for job in job_list:
        if job["truck_type"] in price_table:
            price_table[job["truck_type"]]["total_jobs"] += 1
            price_table[job["truck_type"]]["total_price"] += get_job_price(job)
        else:
            price_table[job["truck_type"]] = {
                "total_jobs": 1,
                "total_price": get_job_price(job)
            }
    return [{ "truck_type": k, "total_jobs": v["total_jobs"], "total_price": v["total_price"].quantize(Decimal('.01'))} for k, v in price_table.items()]

### Method 2: use pandas
### - Slower than method 1 because of the overhead of converting to Decimal()
### - Faster than method 1 if do not require Decimal() and with bigger dataset
def total_price_by_truck_2(job_list):
    df = pd.DataFrame(job_list)
    df['total_jobs'] = 0
    df['total_price'] = 0
    df['price_cents'] = df['price_cents'].apply(lambda x: Decimal(x))
    df['surcharge_cents'] = df['surcharge_cents'].apply(lambda x: Decimal(x))
    df['tax_percent'] = df['tax_percent'].apply(lambda x: Decimal(x))
    df['total_price'] = (df['price_cents'] + df['surcharge_cents']) * ((Decimal(100) + df['tax_percent']) / Decimal(100)) / Decimal(100)
    df['total_price'] = df['total_price'].apply(lambda x: x.quantize(Decimal('.01')))
    df_out = df.groupby('truck_type', sort=False).agg({'total_jobs': 'count', 'total_price': 'sum'}).reset_index()
    return df_out.to_dict(orient='records')


def test_job_price_for_truck_types():
    expected_van_jobs = [
        {'id': 1, 'price': Decimal('151.52')},
        {'id': 7, 'price': Decimal('65.89')},
        {'id': 9, 'price': Decimal('72.66')},
        {'id': 14, 'price': Decimal('43.36')}
    ]

    assert job_price_for_truck_type_1(DB_OUTPUT, "Van") == expected_van_jobs
    assert job_price_for_truck_type_2(DB_OUTPUT, "Van") == expected_van_jobs

    expected_ute_jobs = [
        {'id': 2, 'price': Decimal('73.85')},
        {'id': 4, 'price': Decimal('46.98')},
        {'id': 8, 'price': Decimal('53.26')},
        {'id': 13, 'price': Decimal('83.91')}
    ]

    assert job_price_for_truck_type_1(DB_OUTPUT, "Ute") == expected_ute_jobs
    assert job_price_for_truck_type_2(DB_OUTPUT, "Ute") == expected_ute_jobs

    expected_pantech_jobs = [
        {'id': 3, 'price': Decimal('81.91')},
        {'id': 6, 'price': Decimal('130.82')},
        {'id': 11, 'price': Decimal('24.02')}
    ]

    assert job_price_for_truck_type_1(DB_OUTPUT, "Pantech") == expected_pantech_jobs
    assert job_price_for_truck_type_2(DB_OUTPUT, "Pantech") == expected_pantech_jobs

def test_total_price_by_truck():
    expected_list = [
        {'truck_type': 'Van', 'total_jobs': 4, 'total_price': Decimal('333.43')},
        {'truck_type': 'Ute', 'total_jobs': 4, 'total_price': Decimal('258.00')},
        {'truck_type': 'Pantech', 'total_jobs': 3, 'total_price': Decimal('236.75')}
    ]

    assert total_price_by_truck_1(DB_OUTPUT) == expected_list
    assert total_price_by_truck_2(DB_OUTPUT) == expected_list


## 4. Advanced design concepts
## Below is a class like a Django Model which supports multiple states.
##
## The system architecture means that clients can listen to an external NoSQL database path
## in order to get real-time updates. For example, truck drivers listen to:
##    `/jobs_assigned/<truck_id>/jobs/` (according to their truck ID)
## Operations staff listen to
##    `/jobs_new/`
## All clients can also listen to:
##    `/job_data/<job_id>/`
##
## You must provide a solution so that a change in state writes the data from a JobModel object
## to the correct queue. For example:
## A new job is:
##    written to both `/jobs_new/<job_id>/` and `/job_data/<job_id>/`
## A job assigned to a truck is:
##    removed from `/jobs_new/` and added to `/jobs_assigned/<truck_id>/jobs/<job_id>/`
## A job that is cancelled is:
##    removed from all lists it is a part of (this depends on its state)
##
## Provide a solution which is flexible, and allows us to add more queues or states easily in the future.
## You can write any new functions, classes, data structures, or modify the classes below, but NOT
## the existing methods in the classes. They have already been written to support many other functions
## and requirements in the system

## "Database"
JOBS_DB = dict()

## JobModel: Cannot be modified
class JobModel(object):

    STATES = (
        # Typical sequence is New -> Matched (to truck) -> Active -> Completed
        ('N', 'New'), ('M', 'Matched'), ('A', 'Active'), ('F', 'Completed'), ('C', 'Cancelled'), ('S', 'Suspended')
    )

    def __init__(self, id):
        self.state = 'N'
        self.id = id
        self.truck_id = None

    def set_state(self, new_state):
        supported_states = map(lambda x: x[0], self.STATES)
        if new_state not in supported_states:
            raise RuntimeError("Unsupported state requested")

        self.state = new_state
        return self

    def set_assigned_to(self, truck_id):
        self.truck_id = truck_id
        return self

    def clear_truck(self):
        self.truck_id = None
        return self

    def save(self):
        # Emulate saving to a database
        JOBS_DB[self.id] = self

## Local database for storing queues information of jobs
## Sample data: { 1: { 'queues': { 'New': { 'path': '/jobs_new/1/' } } } }
LOCAL_DB = dict()

class Controller():

    def __init__(self, db):
        self.db = db

    def sync_db(self, job_object):
        # This performs all synchronising of the database. This must be called to perform all the
        # necessary operations on the database/databases it controls.
        # THIS IS A STANDARD INTERFACE AND MUST BE IMPLEMENTED

        job_handler = getattr(jobs, f'JobHandler{job_object.state}')(job_object, self.db, LOCAL_DB)
        job_handler.sync_db()


class DBWriter(object):

    def __init__(self):
        self.db_commands = []

    def reset(self):
        self.db_commands = []

    def write_object_to_path(self, path, obj):
        # This would write to a third-party database service. For simplicity it stores a command to
        # write the correct contents to the command list.
        self.db_commands.append((path, {'id': obj.id, 'state': obj.state}))

    def remove_object_from_path(self, path, obj):
        # This would write to a third-party database service. For simplicity it stores a command to
        # write an empty dict to the command list.
        self.db_commands.append((path, {}))



def test_single_job_standard_lifecycle():

    # DB Writer and controller
    db = DBWriter()
    controller = Controller(db)

    # A new job
    job = JobModel(1)
    job.save()
    controller.sync_db(job)
    assert ('/jobs_new/1/', {'id': 1, 'state': 'N'}) in db.db_commands
    assert ('/job_data/1/', {'id': 1, 'state': 'N'}) in db.db_commands

    # A job is matched
    db.reset()
    job.set_state("M").set_assigned_to("truck1").save()  # I think it must be "M", hope I am right...
    controller.sync_db(job)
    assert ('/jobs_new/1/', {}) in db.db_commands
    assert ('/jobs_assigned/truck1/jobs/1/', {'id': 1, 'state': 'M'}) in db.db_commands
    assert ('/job_data/1/', {'id': 1, 'state': 'M'}) in db.db_commands

    # A job becomes active (from being matched)
    db.reset()
    job.set_state('A').save()
    controller.sync_db(job)
    assert ('/jobs_assigned/truck1/jobs/1/', {'id': 1, 'state': 'A'}) in db.db_commands
    assert ('/job_data/1/', {'id': 1, 'state': 'A'}) in db.db_commands

    # A job is completed. This removes it from all lists.
    db.reset()
    job.set_state('F').save()
    controller.sync_db(job)
    assert ('/job_data/1/', {}) in db.db_commands
    assert ('/jobs_assigned/truck1/jobs/1/', {}) in db.db_commands

def test_single_job_rejected_and_cancelled():

    # DB Writer and controller
    db = DBWriter()
    controller = Controller(db)

    # A new job
    job = JobModel(2)
    job.save()
    controller.sync_db(job)
    assert ('/jobs_new/2/', {'id': 2, 'state': 'N'}) in db.db_commands
    assert ('/job_data/2/', {'id': 2, 'state': 'N'}) in db.db_commands

    # A job is matched
    db.reset()
    job.set_state("M").set_assigned_to("truck1").save()
    controller.sync_db(job)
    assert ('/jobs_new/2/', {}) in db.db_commands
    assert ('/jobs_assigned/truck1/jobs/2/', {'id': 2, 'state': 'M'}) in db.db_commands
    assert ('/job_data/2/', {'id': 2, 'state': 'M'}) in db.db_commands

    '''I got trouble with this case because I can't get the truck_id (in this case is truck1) after '''
    '''clear_truck() and save().'''
    # The job is rejected by a driver -> Back to 'new'
    db.reset()
    job.set_state("N").clear_truck().save()
    controller.sync_db(job)
    assert ('/jobs_assigned/truck1/jobs/2/', {}) in db.db_commands
    assert ('/jobs_new/2/', {'id': 2, 'state': 'N'}) in db.db_commands
    assert ('/job_data/2/', {'id': 2, 'state': 'N'}) in db.db_commands

    # The job is cancelled
    db.reset()
    job.set_state("C").save()
    controller.sync_db(job)
    assert ('/jobs_new/2/', {}) in db.db_commands
    assert ('/job_data/2/', {}) in db.db_commands

# Imagine if a new state was added to the model: ('S', 'Suspended'). This is a job which was active but
# has a problem with the delivery, and needs attention by Operations.
# Operations need to listen to a list for suspended jobs '/jobs_suspended/<job_id>/'
# The job is still considered to be active (so in the '/jobs_active/' list) and also in the `/job_data/`
# list, but these lists must be updated.
# Modify the JobModel to have an extra state, so that the following tests pass. The design you
# implemented for the previous tests should mean that this amount of new code is small.
def test_single_job_suspended_and_cancelled():

    # DB Writer and controller
    db = DBWriter()
    controller = Controller(db)

    # A new job
    job = JobModel(3)
    job.save()
    controller.sync_db(job)
    assert ('/jobs_new/3/', {'id': 3, 'state': 'N'}) in db.db_commands
    assert ('/job_data/3/', {'id': 3, 'state': 'N'}) in db.db_commands

    # A job is matched
    db.reset()
    job.set_state("M").set_assigned_to("truck21").save()
    controller.sync_db(job)
    assert ('/jobs_new/3/', {}) in db.db_commands
    assert ('/jobs_assigned/truck21/jobs/3/', {'id': 3, 'state': 'M'}) in db.db_commands
    assert ('/job_data/3/', {'id': 3, 'state': 'M'}) in db.db_commands

    # A job becomes active (from being matched)
    db.reset()
    job.set_state('A').save()
    controller.sync_db(job)
    assert ('/jobs_assigned/truck21/jobs/3/', {'id': 3, 'state': 'A'}) in db.db_commands
    assert ('/job_data/3/', {'id': 3, 'state': 'A'}) in db.db_commands

    # The job is suspended
    db.reset()
    job.set_state('S').save()
    controller.sync_db(job)
    assert ('/jobs_assigned/truck21/jobs/3/', {'id': 3, 'state': 'S'}) in db.db_commands
    assert ('/jobs_suspended/3/', {'id': 3, 'state': 'S'}) in db.db_commands
    assert ('/job_data/3/', {'id': 3, 'state': 'S'}) in db.db_commands

    # The job is cancelled because of a big problem. It is cleared from all queues.
    db.reset()
    job.set_state('C').save()
    controller.sync_db(job)
    assert ('/jobs_assigned/truck21/jobs/3/', {}) in db.db_commands
    assert ('/jobs_suspended/3/', {}) in db.db_commands
    assert ('/job_data/3/', {}) in db.db_commands

