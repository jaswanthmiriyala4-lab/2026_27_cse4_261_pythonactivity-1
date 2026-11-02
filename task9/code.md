
Multi-Currency Travel Budget Analysis Using Python
1. Problem Statement
Develop a Python program to analyze travel expenses in multiple currencies by converting them into a common base currency using supplied exchange rates.

The program should:

Accept the travel budget in the base currency (INR).

Accept multiple travel expense categories such as accommodation, food, transport, shopping, and entertainment.

Read the expense amount and currency for each category.

Convert foreign currency expenses into INR using supplied exchange rates.

Calculate currency conversion fees.

Calculate the total travel expenditure.

Compare total expenditure against the planned travel budget.

Identify the largest expense category.

Display whether the travel expenses are within the budget or exceed it.

Generate a detailed travel expense report.
2. Algorithm
Start.

Define the base currency as INR.

Define exchange rates for different currencies.

Define the currency conversion fee percentage.

Read the total travel budget.

Read the number of expense categories.

For each expense:

Read the expense category.

Read the expense amount.

Read the currency code.

Check whether the currency is supported.

Retrieve the corresponding exchange rate.

Convert the expense amount into INR.

Calculate the conversion fee.

Calculate the total expense including the conversion fee.

Store the converted expense category-wise.

Repeat until all expenses are processed.

Calculate the total travel expenditure.

Compare the expenditure with the planned budget.

Identify the largest expense category.

Display the detailed travel expense report.

Display whether the budget is sufficient.

Stop

flowchart TD
    A([Start]) --> B[Define Exchange Rates and Fee Percentage]
    B --> C[/Enter Travel Budget/]
    C --> D[/Enter Number of Expenses/]
    D --> E[Initialize Expense List and Total]
    E --> F[/Enter Category, Amount and Currency/]
    F --> G{Currency Supported?}
    G -->|No| H[Display Invalid Currency]
    H --> I{More Expenses?}
    G -->|Yes| J[Retrieve Exchange Rate]
    J --> K[Convert Amount into INR]
    K --> L[Calculate Conversion Fee]
    L --> M[Calculate Final Expense]
    M --> N[Store Category-wise Expense]
    N --> O[Update Total Expenditure]
    O --> I
    I -->|Yes| F
    I -->|No| P[Calculate Budget Difference]
    P --> Q[Identify Largest Expense Category]
    Q --> R{Total Expense <= Budget?}
    R -->|Yes| S[Display Within Budget]
    R -->|No| T[Display Budget Exceeded]
    S --> U[Display Travel Expense Report]
    T --> U
    U --> V([Stop])

