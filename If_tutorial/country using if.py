India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York", "Chicago", "Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]

user1city=input("Enter your city1:")
user2city=input("Enter your city2:")

if user1city in India and user2city in India:
    print("Both cities are in India")
elif user1city in India and user2city not in India:
    print("They dont belong to same country")
elif user1city in USA and user2city in USA:
    print("Both cities are in USA")
elif user1city in USA and user2city not in USA:
    print("They dont belong to same country")
elif user1city in UK and user2city in UK:
    print("Both cities are in UK")
elif user1city in UK and user2city not in UK:
    print("They dont belong to same country")