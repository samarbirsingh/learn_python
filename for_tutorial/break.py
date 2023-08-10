errors=["program 1","program 2","program 3","program 4"]

error_found= "program 4"
for error in errors:
    if error == error_found:
        print("error has been found in", error)
        break
    else:
        print("no errors detected in", error)






