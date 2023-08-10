def calculate(expenses):
    total=0
    for expense in expenses:
        total=total+expense
    return total

expenses_samar= [34, 36, 99, 56]
expenses_sameer= [545, 66, 919, 526]

total=calculate(expenses_samar)
print(total)

total=calculate(expenses_sameer)
print(total)
