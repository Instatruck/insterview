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
