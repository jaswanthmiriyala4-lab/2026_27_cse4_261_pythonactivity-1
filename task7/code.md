Retail Billing with Multiple Discount Rules Using Python
1. Problem Statement
Develop a Python program to generate a retail bill for multiple products based on product prices, quantities, category-specific taxes, threshold discounts, and maximum concession limits.

The program should:

Accept multiple product details, including product name, category, price, and quantity.

Calculate the subtotal for each product.

Apply category-specific tax rates.

Apply threshold-based discounts depending on the purchase amount.

Apply a maximum concession limit to prevent discounts from exceeding a specified amount.

Calculate the final payable amount.

Generate an itemized invoice displaying product details, discounts, taxes, and the total bill.
 Algorithm
Start.

Define product categories and their tax rates.

Define threshold-based discount rules.

Define the maximum concession limit.

Read the number of products.

For each product:

Read product name.

Read product category.

Read unit price.

Read quantity.

Calculate the product subtotal.

Calculate the total purchase amount.

Determine the discount percentage based on the purchase threshold.

Calculate the discount amount.

Check the maximum concession limit and adjust the discount if necessary.

Calculate category-specific taxes for each product.

Calculate the final payable amount.

Generate an itemized invoice.

Display the total subtotal, discount, tax, and final bill.

Stop.

flowchart TD
    A([Start]) --> B[Define Tax Rates and Discount Rules]
    B --> C[/Enter Number of Products/]
    C --> D[Initialize Product List and Subtotal]
    D --> E[/Enter Product Details/]
    E --> F[Calculate Product Subtotal]
    F --> G[Add Subtotal to Grand Total]
    G --> H{More Products?}
    H -->|Yes| E
    H -->|No| I[Determine Discount Percentage]
    I --> J[Calculate Discount Amount]
    J --> K{Discount Exceeds Maximum Limit?}
    K -->|Yes| L[Apply Maximum Concession]
    K -->|No| M[Use Calculated Discount]
    L --> N[Calculate Effective Discount Rate]
    M --> N
    N --> O[Calculate Item-wise Discount]
    O --> P[Calculate Category-specific Tax]
    P --> Q[Calculate Final Amount]
    Q --> R[Generate Itemized Invoice]
    R --> S[Display Total Subtotal, Discount and Tax]
    S --> T([Stop])
