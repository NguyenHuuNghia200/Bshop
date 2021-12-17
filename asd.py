s='07:05:45PM'
h1 = ord(s[1]) - ord('0')
print(h1,h1 % 10)
h2 = ord(s[0]) - ord('0')
print(h2*10)
hh = (h2 * 10 + h1 % 10)
print(hh)
# If time is in "AM"
if (s[8] == 'A'):
    if (hh == 12):
        print('00', end='')

        for i in range(2, 8):
            print(s[i], end='')

    else:
        for i in range(0, 8):
            print(s[i], end='')

# If time is in "PM"
else:
    if (hh == 12):
        print("12", end='')

        for i in range(2, 8):
            print(s[i], end='')

    else:
        hh = hh + 12;
        print(hh, end='')

        for i in range(2, 8):
            print(s[i], end='')