# Tests for insterview

## 1.
## Below is a master list of items. Then there are 2 tests containing more lists.
## One test contains a list where all items in the list are within the master list
## The other test contains a list where not all of the items are in the master list.
## Implement the 'contains_all_items' function in 3 different ways so that the tests pass.
MASTER_LIST = [ 'Cat', 'Dog', 'Apple', 'Bear', 'Goat', 'Fish', 'Elephant',
  'Quokka', 'Unicorn', 'Impala', 'Walrus', 'Yak', 'Giraffe', 'Zebra', 'Narwhal',
  'Rhinceros', 'Vulture', 'Tiger', 'Kangaroo', 'Lion', 'Sloth', 'Jaguar', 'Ostrich']

def contains_all_items_1(test_list):
    # Complete this function in 3 different ways
    pass

def contains_all_items_2(test_list):
    # Complete this function in 3 different ways
    pass

def contains_all_items_3(test_list):
    # Complete this function in 3 different ways
    pass

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

def most_frequent_1():
    # Complete this function in 3 different ways
    pass

def most_frequent_2():
    # Complete this function in 3 different ways
    pass

def most_frequent_3():
    # Complete this function in 3 different ways
    pass

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

def job_price_for_truck_type(job_list, truck_type):
    ''' Returns a list of the following structure for trucks matching "truck_type":
        { "id": <int>, "price": <int> }

        where "price" is "(price_cents + surcharge_cents) * (100 + tax_percent)/100" converted to dollars
    '''
    pass

def total_price_by_truck(job_list):
    ''' Returns a list of the following structures:
        { "truck_type": <truck type>, "total_jobs": <int>, "total_price": <int> }

        where "total_jobs" is the total number of jobs for the truck type
        and "total_price" is the total price for the truck type
    '''
    pass

def test_job_price_for_truck_types():
    expected_van_jobs = []  # Add expected data

    assert job_price_for_truck_type_1(DB_OUTPUT, "Van") == expected_van_jobs
    assert job_price_for_truck_type_2(DB_OUTPUT, "Van") == expected_van_jobs

    expected_ute_jobs = []  # Add expected data

    assert job_price_for_truck_type_1(DB_OUTPUT, "Ute") == expected_ute_jobs
    assert job_price_for_truck_type_2(DB_OUTPUT, "Ute") == expected_ute_jobs

    expected_pantech_jobs = []  # Add expected data

    assert job_price_for_truck_type_1(DB_OUTPUT, "Pantech") == expected_pantech_jobs
    assert job_price_for_truck_type_2(DB_OUTPUT, "Pantech") == expected_pantech_jobs

def test_total_price_by_truck():
    expected_list = [
        {"truck_type": "Van", "total_jobs": "4", "total_price": None}, # Add expected total price
        {"truck_type": "Ute", "total_jobs": "4", "total_price": None}, # Add expected total price
        {"truck_type": "Pantech", "total_jobs": "3", "total_price": None}, # Add expected total price
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
        ('N', 'New'), ('M', 'Matched'), ('A', 'Active'), ('F', 'Completed'), ('C', 'Cancelled')
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

class Controller():

    def __init__(self, db):
        self.db = db

    def sync_db(self, job_object):
        # This performs all synchronising of the database. This must be called to perform all the
        # necessary operations on the database/databases it controls.
        # THIS IS A STANDARD INTERFACE AND MUST BE IMPLEMENTED
        pass

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
    job.set_state("A").set_assigned_to("truck1").save()
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
    job.set_state("A").set_assigned_to("truck1").save()
    controller.sync_db(job)
    assert ('/jobs_new/2/', {}) in db.db_commands
    assert ('/jobs_assigned/truck1/jobs/2/', {'id': 2, 'state': 'M'}) in db.db_commands
    assert ('/job_data/2/', {'id': 2, 'state': 'M'}) in db.db_commands

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
    job.set_state("A").set_assigned_to("truck21").save()
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

