from collections import OrderedDict
# test_dict={"a":1, "b":2, "c":3}
# print(f"test_dict 출력 : {test_dict}")

# test_keys = test_dict.keys()
# print(f"test_keys 출력 : {test_keys}")

# test_values = test_dict.values()
# print(f"test_values 출력 : {test_values}")

# test_items = test_dict.items()
# print(f"test_items 출력 : {test_items}")

# for k,v in test_items :
#     print(f"key 값 : {k}, values 값 : {v}")


def sort_by_key(t) :
    return t[1]


#기본 딕셔너리
# d ={}

# d['x'] = 100
# d['l'] = 500
# d['y'] = 200
# d['z'] = 300

d = OrderedDict()
d['b'] = 10
d['a'] = 2
d['d'] = 7
d['c'] = 6

test_OrderedDict = OrderedDict(sorted(d.items(), key=sort_by_key)).items()

# for k, v in d.items():
#     print(k,v)

for k, v in test_OrderedDict :
    print(f"key : {k}, values : {v}")



