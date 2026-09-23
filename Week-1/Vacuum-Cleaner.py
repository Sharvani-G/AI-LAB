# Vacuum Cleaner Agent

# Initial state of rooms
room_A = input("Enter status of Room A (Dirty/Clean): ").capitalize()
room_B = input("Enter status of Room B (Dirty/Clean): ").capitalize()

# Initial vacuum location
location = input("Enter vacuum location (A/B): ").upper()

print("\nInitial State:")
print("Room A:", room_A)
print("Room B:", room_B)
print("Vacuum Location:", location)

while True:
    # Check current room
    if location == "A":
        if room_A == "Dirty":
            print("\nRoom A is Dirty -> SUCK")
            room_A = "Clean"
        else:
            print("\nRoom A is Clean -> Move to Room B")
            location = "B"

    else:
        if room_B == "Dirty":
            print("\nRoom B is Dirty -> SUCK")
            room_B = "Clean"
        else:
            print("\nRoom B is Clean -> Move to Room A")
            location = "A"

    # Check whether both rooms are clean
    if room_A == "Clean" and room_B == "Clean":
        print("\nBoth rooms are CLEAN.")
        print("Goal Achieved!")
        break

print("\nFinal State:")
print("Room A:", room_A)
print("Room B:", room_B)
print("Vacuum Location:", location)
