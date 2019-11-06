
s = "abcde"
result = list(s)

start = 0
end = len(s) - 1

while start < end:
    result[start], result[end] = s[end], s[start]
    start += 1
    end -= 1

print('hi')