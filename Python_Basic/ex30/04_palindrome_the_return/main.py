from collections import Counter

def can_be_poly(st: str) -> bool:
    return len(list(filter(lambda x: x % 2, Counter(st).values()))) <= 2


print(can_be_poly('abbbba'))
print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))