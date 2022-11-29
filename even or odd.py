def find_outlier(integers):
    even = 0
    odd = 0
    for i in integers:
        if i % 2 == 0:
            even += 1
        if i % 2 == 1:
            odd += 1
    if even == 1:
        for i in integers:
            if i % 2 == 0:
                return i
    if odd == 1:
        for i in integers:
            if i % 2 == 1:
                return i


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))  # luwebis luwi/kenti raod jami kent
print(find_outlier([160, 3, 1719, 19, 11, 13, -21, 5]))  # kentebis luwi raod   jami kenti
find_outlier([160, 3, 1719, 19, 11, 13, -21])  # kentebis kenti raod   jami luwi //
