
sum = 0

with open('py/test.txt', 'r+') as f: #seems like it was defaulting to parent folder so had to add the py/
    for line in f: #with this "with open" approach, the f.readline() was only doing on line.. "for line in f" was the solution
        sum += int(line)

print(sum)
print('hi')