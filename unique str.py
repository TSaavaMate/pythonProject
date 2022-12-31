def find_uniq(arr):
    arr1 = [''.join(sorted(set(i.lower().replace(' ', '')))) for i in arr]
    print(arr1)

print(find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]))#BbBb
print(find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]))#foo
#undone