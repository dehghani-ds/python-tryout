from collections import Counter

my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(3)
my_set.add(3)
my_set.add(3)
my_set.add(1)

print(Counter(my_set).most_common())

from collections import namedtuple
import datetime

named_tuple_mine = namedtuple(
    'named_tuple_mine',['field_one', 'field_two', 'field_three']
)
print(named_tuple_mine)

sample_named = named_tuple_mine(field_one=1, field_two=2, field_three=3)
print(sample_named)
print(sample_named.field_one)
print(sample_named[1])

from collections import defaultdict

default_cid = defaultdict(lambda : 'odd' if datetime.datetime.now().minute % 2 == 0 else 'even')
default_cid['name'] = 'yunus'

print(default_cid.items())
print(default_cid['name'])
print(default_cid['family'])

print(datetime.date.today())

import math

print(math.inf)
print(math.e)
print(math.ceil(math.e))
print(round(math.log2(8)))