# 🏦 Python Bank Management System (CLI-Based)

A robust, feature-rich, and interactive **Command-Line Interface (CLI) Bank Management System** built entirely in **Python**. This project demonstrates the practical application of **Object-Oriented Programming (OOP)** principles, data structures, and modular function design to simulate real-world core banking operations.

---

## 🚀 Key Features

*   **Customer Lifecycle Management**: Register new customers with unique IDs, validate phone numbers (strict 10-digit checks), restrict accounts for minors, and view or delete customer profiles.
*   **Diverse Account Tiers**: 
    *   **Savings Account**: Includes automated interest calculation and balance updates.
    *   **Premium Savings Account**: Adds minimum balance tracking and tier status validation.
    *   **Current Account**: Features built-in **overdraft limit handling** for flexible withdrawals.
*   **Core Banking Transactions**: Secure deposits, dynamic withdrawals with insufficient balance checks, and real-time balance inquiries.
*   **Financial Services & Calculators**: 
    *   **Loan Calculation**: Computes interest and total payable amounts based on principal, rate, and tenure.
    *   **Insurance Calculation**: Estimates insurance premiums based on insured amounts and tenure.
*   **Persistent In-Memory Storage**: Utilizes global Python dictionaries (`customers` and `accounts`) for fast, efficient lookups and state management during runtime.

---

## 🛠️ Object-Oriented Programming (OOP) Architecture

The application is structured around clean OOP design paradigms:

1.  **Encapsulation**: Encapsulates data and behaviors into distinct classes (`Customer`, `Bank_Account`, `Loan`, `Insurance`).
2.  **Inheritance**: 
    *   `SavingAccount` and `CurrentAccount` inherit core properties and methods from the base `Bank_Account` class.
    *   `PremiumSavingAccount` extends `SavingAccount` to handle specialized tier checks.
3.  **Multiple Inheritance**: The `Bank_Services` class inherits simultaneously from both `Loan` and `Insurance` classes to bundle diverse financial utilities.
4.  **Polymorphism (Method Overriding)**: The `display_account()` method is dynamically overridden across account sub-classes to output specialized details relevant to each account type.

---

## 📋 System Menu Options

The interactive CLI provides a user-friendly menu with 15 operations:
1. **Add Customer** – Register a new customer with validation checks.
2. **Display Customer** – View specific customer details and age category.
3. **Search Customer** – Look up customer records by ID.
4. **Delete Customer** – Remove customer profiles from the system.
5. **Create Savings Account** – Open a new savings account for registered customers.
6. **Deposit Money** – Add funds to an existing account.
7. **Withdraw Money** – Safely withdraw funds with balance checks.
8. **Check Balance** – View current account balances.
9. **Add Interest** – Apply interest rates to savings accounts.
10. **Create Current Account** – Open a current account with custom overdraft limits.
11. **Check Overdraft** – Process flexible withdrawals against overdraft limits.
12. **Loan Calculation** – Compute loan repayment totals.
13. **Insurance Calculation** – Estimate insurance policy premiums.
14. **Display All Customers** – View a directory of all registered customers.
15. **Exit** – Terminate the application session safely.

---

## 💻 Tech Stack & Requirements

*   **Language**: Python 3.x
*   **Built-in Modules**: `random` (for generating unique 5-digit account numbers)

---

## 🚀 How to Run the Project

1. Clone the repository or download the script file:
   ```bash
   git clone [https://github.com/your-username/python-bank-management-system.git](https://github.com/your-username/python-bank-management-system.git)
