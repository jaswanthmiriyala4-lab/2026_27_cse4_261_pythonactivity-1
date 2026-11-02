
Railway Fare and Reservation Calculator Using Python
1. Problem Statement
Develop a Python program to calculate railway ticket fares for multiple passengers based on distance slabs, travel classes, age-based concessions, reservation fees, and cancellation penalties.

The program should:

Accept the number of passengers and their details.

Read the passenger's name, age, travel distance, and travel class.

Calculate the basic fare based on distance slabs.

Apply different fare rates for different travel classes.

Apply age-based concessions for eligible passengers.

Add reservation charges to the ticket fare.

Calculate the total fare for all passengers.

Calculate cancellation penalties when tickets are cancelled.

Display a detailed railway fare statement.
2. Algorithm
Start.

Define distance slabs and fare rates.

Define travel classes and their multipliers.

Define age-based concession percentages.

Read the number of passengers.

For each passenger:

Read passenger name and age.

Read travel distance.

Read travel class.

Read whether the ticket is cancelled.

Calculate the basic fare according to the distance slab.

Apply the travel class multiplier.

Check passenger age and calculate eligible concession.

Calculate reservation charges.

Calculate the final ticket fare.

If the ticket is cancelled:

Calculate the cancellation penalty.

Calculate the refund amount.

Otherwise, display the payable ticket fare.

Calculate the total amount for all passengers.

Display the railway fare statement.

Stop

flowchart TD
    A([Start]) --> B[Define Distance Slabs and Fare Rates]
    B --> C[Define Classes and Concessions]
    C --> D[/Enter Number of Passengers/]
    D --> E[Initialize Total Booking and Refund]
    E --> F[/Enter Passenger Details/]
    F --> G[Calculate Basic Fare]
    G --> H[Apply Class Multiplier]
    H --> I[Calculate Age Concession]
    I --> J[Calculate Reservation Fee]
    J --> K[Calculate Final Ticket Fare]
    K --> L{Ticket Cancelled?}
    L -->|Yes| M[Calculate Cancellation Penalty]
    M --> N[Calculate Refund Amount]
    L -->|No| O[Add Fare to Booking Total]
    N --> P{More Passengers?}
    O --> P
    P -->|Yes| F
    P -->|No| Q[Display Final Booking Summary]
    Q --> R([Stop])
