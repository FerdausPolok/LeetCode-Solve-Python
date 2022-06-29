import collections

cols = collections.defaultdict(set)

cols[0].add(10)
print(cols)
print(type(cols))