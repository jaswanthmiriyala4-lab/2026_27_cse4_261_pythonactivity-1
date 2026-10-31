Progressive Electricity Billing System Using Python
1. Problem Statement
Design and develop a Progressive Electricity Billing System using Python to calculate household electricity bills based on electricity consumption using multiple tariff slabs.

The system should calculate the electricity bill by considering:

Units of electricity consumed.

Different electricity consumption slabs.

Fixed monthly charges.

Additional surcharges.

Rebates or discounts.

Monthly bill comparison.

Identification of unusual increases in electricity bills.

Example Billing Rules (Assumed):

Consumption Slab

Rate per Unit

0–100 units

₹2.00

101–200 units

₹3.00

201–300 units

₹5.00

Above 300 units

₹7.00

Additional charges:

Fixed charge: ₹50 per month.

Surcharge: 5% of energy charges.

Rebate: 5% of energy charges if consumption is below 100 units.

Unusual increase: If the current month's bill increases by more than 30% compared with the previous month.

2. Algorithm
Start the program.

Define electricity slab rates and billing rules.

Input the number of months.

For each month, input electricity consumption in units.

Calculate energy charges based on progressive slabs:

First 100 units at ₹2 per unit.

Next 100 units at ₹3 per unit.

Next 100 units at ₹5 per unit.

Remaining units at ₹7 per unit.

Add the fixed monthly charge.

Calculate the 5% surcharge on energy charges.

Check whether consumption is below 100 units.

If yes, apply a 5% rebate on energy charges.

Calculate the final electricity bill.

Store the monthly bill.

Compare the current month's bill with the previous month's bill.

If the increase is greater than 30%, identify it as an unusual increase.

Display monthly bills and total electricity expenditure.

Stop.

....

flowchart TD

    A([Start]) --> B[Define Slab Rates and Charges]

    B --> C[/Enter Number of Months/]

    C --> D[/Enter Monthly Units Consumed/]

    D --> E{Units Valid?}

    E -- No --> D
    E -- Yes --> F[Calculate Energy Charges]

    F --> G[Add Fixed Charges]

    G --> H[Calculate Surcharge]

    H --> I{Units Below 100?}

    I -- Yes --> J[Apply 5% Rebate]
    I -- No --> K[No Rebate]

    J --> L[Calculate Final Bill]
    K --> L

    L --> M[Store Monthly Bill]

    M --> N{More Months?}

    N -- Yes --> D
    N -- No --> O[Display Monthly Bills]

    O --> P[Compare Consecutive Bills]

    P --> Q{Increase Greater Than 30%?}

    Q -- Yes --> R[Display Unusual Increase Alert]
    Q -- No --> S[Display Normal Bill Variation]

    R --> T[Calculate Total Expenditure]
    S --> T

    T --> U[/Display Final Report/]

    U --> V([End])
The Progressive Electricity Billing System calculates household electricity bills using multiple consumption slabs, fixed charges, surcharges, and rebates.

It also compares electricity bills across different months and identifies unusual increases when the bill rises by more than 30%.

Advantages:

Accurate electricity bill calculation.

Supports progressive tariff slabs.

Automatically applies surcharges and rebates.

Compares monthly electricity expenses.

Detects unusual increases in bills.

Reduces manual calculation errors.
