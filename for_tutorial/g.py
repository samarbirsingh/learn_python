transactions = [(456, 'f'), (457, 'f'), (458, 'w'), (459, 'f')]
count=0
for transaction in transactions:
    if transaction[1]!='f':
        count+=1

print(count)