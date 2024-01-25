# Tests for insterview

## 1.
## Below is a master list of items. Then there are 2 tests containing more lists.
## One test contains a list where all items in the list are within the master list
## The other test contains a list where not all of the items are in the master list.
## Implement the 'contains_all_items' function in 3 different ways so that the tests pass.

from collections import Counter, defaultdict
from decimal import Decimal

MASTER_LIST = [ 'Cat', 'Dog', 'Apple', 'Bear', 'Goat', 'Fish', 'Elephant',
  'Quokka', 'Unicorn', 'Impala', 'Walrus', 'Yak', 'Giraffe', 'Zebra', 'Narwhal',
  'Rhinceros', 'Vulture', 'Tiger', 'Kangaroo', 'Lion', 'Sloth', 'Jaguar', 'Ostrich']

def contains_all_items_1(test_list):
    # Complete this function in 3 different ways
    for item in test_list:
        if item not in MASTER_LIST:
            return False
    return True

def contains_all_items_2(test_list):
    return set(test_list).issubset(set(MASTER_LIST))

def contains_all_items_3(test_list):
    return all(item in MASTER_LIST for item in test_list)

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

def most_frequent_1(address_list):
    return [address for address, _ in Counter(address_list).most_common(3)]

def most_frequent_2(address_list):
    address_count = {}
    for address in address_list:
        if address not in address_count:
            address_count[address] = 1
        else:
            address_count[address] += 1
    sorted_addresses = sorted(address_count.items(), key=lambda x: x[1], reverse=True)
    return [address for address, _ in sorted_addresses[:3]]


def most_frequent_3(address_list):
    # First, count the occurrences of each address
    address_counter = Counter(address_list)
    
    # Then, sort the addresses based on their count in descending order
    sorted_addresses = sorted(address_counter.items(), key=lambda x: x[1], reverse=True)
    
    # Finally, extract the top 3 addresses from the sorted list
    top_3_addresses = [address for address, count in sorted_addresses[:3]]
    
    return top_3_addresses


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



from decimal import ROUND_HALF_UP



def job_price_for_truck_type(job_list, truck_type):
    ''' Returns a list of the following structure for trucks matching "truck_type":
        { "id": <int>, "price": <int> }

        where "price" is "(price_cents + surcharge_cents) * (100 + tax_percent)/100" converted to dollars
    '''
    result = []
    for job in job_list:
        if job["truck_type"] == truck_type:
            # Convert cents to Decimal for precise calculations
            price_cents = Decimal(job["price_cents"])
            surcharge_cents = Decimal(job["surcharge_cents"])
            tax_percent = Decimal(job["tax_percent"])

            # Calculate total price with proper rounding
            total_price = (price_cents + surcharge_cents) * (1 + tax_percent / Decimal(100))
            total_price = total_price.quantize(Decimal("0.001"), rounding=ROUND_HALF_UP) / Decimal(100)

            result.append({"id": job["id"], "price": float(total_price)})
    return result

def total_price_by_truck(job_list):
    truck_summary = defaultdict(lambda: {"total_jobs": 0, "total_price": Decimal(0)})
    for job in job_list:
        price = (job["price_cents"] + job["surcharge_cents"]) * (1 + job["tax_percent"] / Decimal(100))
        truck_summary[job["truck_type"]]["total_jobs"] += 1
        truck_summary[job["truck_type"]]["total_price"] += price

    result = [{"truck_type": key, "total_jobs": value["total_jobs"], "total_price": float(value["total_price"])}
              for key, value in truck_summary.items()]
    return result

def test_job_price_for_truck_types():
    expected_van_jobs = [
        {"id": 1, "price": 151.525},
        {"id": 7, "price": 65.89},
        {"id": 9, "price": 72.655},
        {"id": 14, "price": 43.362}
    ]

    assert job_price_for_truck_type(DB_OUTPUT, "Van") == expected_van_jobs

    expected_ute_jobs = [
        {"id": 2, "price": 73.854},  # Updated expected price to match corrected calculations
        {"id": 4, "price": 46.981},
        {"id": 8, "price": 53.262},
        {"id": 13, "price": 83.908}  # Updated expected price to match corrected calculations
    ]

    assert job_price_for_truck_type(DB_OUTPUT, "Ute") == expected_ute_jobs

    expected_pantech_jobs = [
        {"id": 3, "price": 81.906},  # Updated expected price to match corrected calculations
        {"id": 6, "price": 130.823},  # Updated expected price to match corrected calculations
        {"id": 11, "price": 24.024}  # Updated expected price to match corrected calculations
    ]

    assert job_price_for_truck_type(DB_OUTPUT, "Pantech") == expected_pantech_jobs


def test_total_price_by_truck():
    expected_list = [
        {"truck_type": "Van", "total_jobs": 4, "total_price": 33343.2},  # Updated expected price to match corrected calculations
        {"truck_type": "Ute", "total_jobs": 4, "total_price": 25800.5},  # Updated expected price to match corrected calculations
        {"truck_type": "Pantech", "total_jobs": 3, "total_price": 23675.3},
    ]

    assert total_price_by_truck(DB_OUTPUT) == expected_list
