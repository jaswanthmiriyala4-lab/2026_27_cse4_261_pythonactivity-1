Multi-Plan Telecommunications Cost Optimization Using Python
1. Problem Statement
Develop a Python program to evaluate multiple mobile telecommunications plans based on a user's monthly usage, validity requirements, and budget constraints.

The program should:

Accept the user's data usage, call minutes, SMS requirements, validity period, and budget.

Store details of multiple mobile plans, including plan cost, data limit, call limit, SMS limit, and validity.

Calculate excess charges when usage exceeds the plan limits.

Calculate the total cost of each mobile plan.

Check whether each plan satisfies the user's budget and validity requirements.

Identify the most economical eligible mobile plan.

Display a comparison of all plans and recommend the best plan.
Algorithm
Start.

Read the user's requirements:

Required data in GB.

Required call minutes.

Required SMS count.

Required validity in days.

Maximum budget.

Define multiple mobile plans with their prices, data limits, call limits, SMS limits, and validity.

Initialize the minimum cost to infinity.

For each mobile plan:

Calculate extra data usage.

Calculate extra call minutes.

Calculate extra SMS.

Calculate excess charges.

Calculate total cost.

Check whether the plan satisfies the validity requirement.

Check whether the total cost is within the user's budget.

If both conditions are satisfied, mark the plan as eligible.

Compare eligible plans and identify the plan with the lowest total cost.

Display all plan details and excess charges.

Display the most economical eligible plan.

If no plan satisfies the requirements, display an appropriate message.

Stop

flowchart TD
    A([Start]) --> B[/Enter User Requirements/]
    B --> C[Define Mobile Plans and Rates]
    C --> D[Initialize Eligible Plans]
    D --> E[Select Next Mobile Plan]
    E --> F[Calculate Extra Data, Calls and SMS]
    F --> G[Calculate Excess Charges]
    G --> H[Calculate Total Cost]
    H --> I{Validity Satisfied?}
    I -->|No| N[Mark Plan Ineligible]
    I -->|Yes| J{Within Budget?}
    J -->|No| N
    J -->|Yes| K[Add Plan to Eligible List]
    N --> L{More Plans Available?}
    K --> L
    L -->|Yes| E
    L -->|No| M{Eligible Plans Exist?}
    M -->|No| O[Display No Eligible Plan]
    M -->|Yes| P[Find Minimum Total Cost]
    P --> Q[Display Most Economical Plan]
    O --> R([Stop])
    Q --> R

