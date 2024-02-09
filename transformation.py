def transform(s):
    s = s.split(' ')
    s[1] = s[1][:-5]
    s[4] = s[4][:-5]
    s[7] = s[7][:-7]
    s[10] = s[10][:-6]

    s.remove('R-Squared:')
    s.remove('Squared')
    s.remove('Error:')
    s.remove('Absolute')
    s.remove('Error:')
    s.remove('Absolute')
    s.remove('Error:')
    s.pop()

    res = []
    for el in s:
        res.append(float(el))
    return res
