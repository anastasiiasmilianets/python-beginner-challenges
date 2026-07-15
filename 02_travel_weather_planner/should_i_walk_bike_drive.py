print("🚦 Should I Walk, Bike, or Drive? ")

while True:
    distance_mi = float(input("Distance in miles: "))
    is_raining = input("Is it raining? (yes/no): ").lower() == "yes"
    has_bike = input("Do you have a bike? (yes/no): ").lower() == "yes"
    has_car = input("Do you have a car? (yes/no): ").lower() == "yes"
    has_ride_share_app = input(
        "Rideshare available? (yes/no): ").lower() == "yes"

    if distance_mi == 0:
        print("You're already there!")
    elif distance_mi <= 1:
        if not is_raining:
            print("Walk there!")
        else:
            print("Too wet to walk — find another way.")
    elif distance_mi > 1 and distance_mi <= 6:
        if has_bike and not is_raining:
            print("Bike there!")
        elif has_car or has_ride_share_app:
            print("Take a car or rideshare.")
        else:
            print("Bike isn't an option right now.")
    elif distance_mi > 6:
        if has_car or has_ride_share_app:
            print("Take a car or rideshare.")
        else:
            print("You'll need to find transport.")

    print("")

    again = input("Check another route? (yes/no)")
    if again.lower() == "yes":
        continue
    else:
        break
