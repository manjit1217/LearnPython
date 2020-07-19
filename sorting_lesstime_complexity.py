l=[3,5,3,2,32,4,54,6,6]
def min_sorted(values):
        result = []
        while values:
            m = min(values)
            result.append(m)
            values.remove(m)
        return result

print(min_sorted(l))