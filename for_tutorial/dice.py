count=0
dice_result  = [5,6,6,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
for i in range(len(dice_result)):
    if dice_result[i]==6 and dice_result[i+1]==6:
        count=count+1
print(count)