 Manufacturing Cost and Profitability Analysis Using Python
1. Problem Statement
Develop a Python program to calculate the total manufacturing cost and analyze the profitability of a product based on material costs, labour charges, wastage, machine costs, and selling price.

The program should:

Accept product name and production quantity.

Calculate the total raw material cost.

Calculate labour charges based on production quantity.

Calculate material wastage cost.

Calculate machine operating costs.

Calculate the total manufacturing cost.

Determine the cost per unit.

Calculate the total selling revenue.

Calculate profit or loss.

Compare the actual profit percentage with the specified profit target.

Display whether the production meets the required profit target.

Algorithm
Start.

Read product name.

Read production quantity.

Read material cost per unit.

Read labour cost per unit.

Read wastage percentage.

Read machine operating cost.

Read selling price per unit.

Read required profit target percentage.

Calculate total material cost.

Calculate total labour cost.

Calculate material wastage cost.

Calculate total manufacturing cost.

Calculate total sales revenue.

Calculate profit or loss.

Calculate profit percentage.

Compare actual profit percentage with the target percentage.

If actual profit percentage is greater than or equal to the target, display "Profit Target Achieved".

Otherwise, display "Profit Target Not Achieved".

Display the complete manufacturing cost and profitability statement.

Stop.

flowchart TD
    A([Start]) --> B[/Enter Product Details/]
    B --> C[/Enter Quantity, Material and Labour Costs/]
    C --> D[/Enter Wastage Rate and Machine Cost/]
    D --> E[/Enter Selling Price and Profit Target/]
    E --> F[Calculate Total Material Cost]
    F --> G[Calculate Total Labour Cost]
    G --> H[Calculate Wastage Cost]
    H --> I[Calculate Total Manufacturing Cost]
    I --> J[Calculate Cost Per Unit]
    J --> K[Calculate Total Sales Revenue]
    K --> L[Calculate Profit or Loss]
    L --> M[Calculate Profit Percentage]
    M --> N{Profit Percentage >= Target?}
    N -->|Yes| O[Display Profit Target Achieved]
    N -->|No| P[Display Profit Target Not Achieved]
    O --> Q[Display Manufacturing Report]
    P --> Q
    Q --> R([Stop])





