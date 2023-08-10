pushups = 0
answer = ""
while True:
    print("Doing push up.")
    pushups += 1
    if pushups == 50:
        print("Congratulations! You made it")
        break

    elif pushups%10 ==0:
        answer = input("Are you tired? (yes/no)")
        if answer[0].lower() == 'y':
            break
        else:
            print(f"{50-pushups} push-ups are remaining today.")



print(f"You did total {pushups} Push-ups today.")
