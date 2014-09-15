fuit = ['apple', 'orange', 'grape', 'kiwi', 'apple', 'orange', 'grape']


def analyze_list(li):1

counts = {}
for item in li:
    if item in counts:
        counts[item] = counts[item] + 1
        else:
            counts[item] = 1
    return counts


counts = analyze_list(fruit)
print counts
