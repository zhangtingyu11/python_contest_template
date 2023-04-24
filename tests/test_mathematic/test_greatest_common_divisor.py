from mathematic.greatest_common_divisor import *

def test_calculate_sub_array_gcd():
    nums = [2, 6, 3, 4]
    assert(calculate_sub_array_gcd(nums)==[1, 2, 2, 2])