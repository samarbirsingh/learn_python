indian=["samosa","daal","naan"]
chinese=["egg role","pot sticker","fried rice"]
italian=["pizza","pasta","risotto"]

dish=input("Which dish are you having tonight?")

if dish in indian:
    print(f"Umm!! Are you eating indian tonight? I think {dish} is Indian")
elif dish in chinese:
    print(f"Wow,Are you eating {dish}? I love Chinese")
elif dish in italian:
    print(f"Oh!! Is Italian in menu today? Its always a treat to eat {dish} ")
else:
    print("Hey, what kind of dish that is? Never heard of it before.")