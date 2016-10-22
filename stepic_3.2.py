
def update_dictionary(d, key, value):
    if key in d.keys():
        d[key] += [value]
    else:
        key *= 2
        if key in d.keys():
            d[key] += [value]
        else:
            d[key] = [value]







d = {1:[3]}
print(d)
update_dictionary(d, 'a', 1)
print(d)


