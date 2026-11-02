
# Railway Fare and Reservation Calculator

# Distance-based fare rates
def get_distance_rate(distance):
    if distance <= 100:
        return 1.00
    elif distance <= 300:
        return 1.20
    elif distance <= 500:
        return 1.50
    else:
        return 1.80


# Travel class multipliers
class_multiplier = {
    "SL": 1.0,
    "3A": 2.0,
    "2A": 3.0,
    "1A": 4.0
}

# Reservation fees
reservation_fee = {
    "SL": 20,
    "3A": 40,
    "2A": 50,
    "1A": 60
}


# Age-based concession
def get_concession(age):
    if age < 5:
        return 100
    elif age >= 60:
        return 40
    else:
        return 0


# Cancellation penalty
def get_cancellation_penalty(fare):
    if fare <= 200:
        return 20
    elif fare <= 500:
        return 50
    else:
        return fare * 0.10


# Input number of passengers
n = int(input("Enter number of passengers: "))

total_booking = 0
total_refund = 0
total_penalty = 0

print("\n========== RAILWAY FARE DETAILS ==========")

# Process each passenger
for i in range(n):

    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter travel distance (KM): "))

    print("Classes: SL, 3A, 2A, 1A")
    travel_class = input("Enter travel class: ").upper()

    if travel_class not in class_multiplier:
        print("Invalid class. Passenger skipped.")
        continue

    cancelled = input(
        "Is ticket cancelled? (yes/no): "
    ).lower()

    # Calculate distance-based fare
    rate = get_distance_rate(distance)

    basic_fare = distance * rate

    # Apply class multiplier
    class_fare = (
        basic_fare * class_multiplier[travel_class]
    )

    # Calculate age concession
    concession = get_concession(age)

    discount = class_fare * concession / 100

    # Calculate reservation fee
    reservation = reservation_fee[travel_class]

    # Calculate final ticket fare
    final_fare = class_fare - discount + reservation

    print("\n---------- PASSENGER STATEMENT ----------")
    print("Passenger Name     :", name)
    print("Age                :", age)
    print("Distance           :", distance, "KM")
    print("Travel Class       :", travel_class)
    print("Basic Fare         : Rs.", round(basic_fare, 2))
    print("Class Fare         : Rs.", round(class_fare, 2))
    print("Age Concession     :", concession, "%")
    print("Discount           : Rs.", round(discount, 2))
    print("Reservation Fee    : Rs.", reservation)
    print("Final Ticket Fare  : Rs.", round(final_fare, 2))

    # Check cancellation
    if cancelled == "yes":

        penalty = get_cancellation_penalty(final_fare)
        refund = final_fare - penalty

        total_penalty += penalty
        total_refund += refund

        print("Cancellation Penalty: Rs.", round(penalty, 2))
        print("Refund Amount       : Rs.", round(refund, 2))

    else:

        total_booking += final_fare

        print("Ticket Status       : Confirmed")
        print("Amount Payable      : Rs.", round(final_fare, 2))

    print("-----------------------------------------")

# Final summary
print("\n========== FINAL BOOKING SUMMARY ==========")

print("Total Confirmed Booking : Rs.",
      round(total_booking, 2))

print("Total Cancellation Penalty : Rs.",
      round(total_penalty, 2))

print("Total Refund Amount : Rs.",
      round(total_refund, 2))

print("Total Passengers Processed :", n)

print("===========================================")

