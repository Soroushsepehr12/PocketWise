# 🍏 Pocketwise

A modern personal finance management desktop application built with **Python, PyQt6, and SQLite**.

Pocketwise helps users manage their personal finances through a clean, modern interface with tools for tracking income, expenses, transactions, and savings goals.

The goal of Pocketwise is to provide a simple but powerful money management experience while exploring real-world desktop application development.

---

# 🎥 Demo Video

Click the image below to watch the Pocketwise demonstration:

[![Pocketwise Demo](https://img.youtube.com/vi/bDZoxMEuGwM/maxresdefault.jpg)](https://youtu.be/bDZoxMEuGwM)

---

# ✨ Features

## 🖥️ Modern Desktop Interface

Pocketwise uses PyQt6 to create a polished desktop application.

The interface includes:

- Modern dark theme
- Apple-inspired green design
- Custom styled buttons
- Card-based layouts
- Neon glow effects
- Tab-based navigation
- Clean financial dashboard

---

# 📊 Dashboard

The dashboard provides a quick overview of financial information.

Features:

- Personalized user greeting
- Current balance display
- Financial overview section
- Modern card UI

Users can quickly understand their current financial situation.

---

# 💰 Income Tracking

Pocketwise allows users to record income.

Supported information:

- Amount
- Source
- Date
- Description

Examples:

- Salary
- Freelance work
- Bonuses
- Other income sources

When income is added, Pocketwise updates calculations automatically.

---

# 💸 Expense Tracking

Users can record expenses and see their effect on their balance.

Features:

- Add expense amount
- Add expense date
- Live balance preview
- Automatic calculations

The application calculates remaining money after expenses.

---

# 📜 Transaction Management

Pocketwise includes a transaction view for managing financial records.

Current features:

- Transaction table
- IDs
- Amounts
- Dates
- Income records

Future improvements can include:

- Search
- Filtering
- Categories
- Exporting reports

---

# 🎯 Savings Goals

Pocketwise supports saving goals.

Users can create goals with:

- Goal name
- Target amount
- Date

Examples:

- Buying a computer
- Saving for a trip
- Personal projects

---

# 🗄️ Database System

Pocketwise uses SQLite for local data storage.

The database is automatically created when the application runs.

## Database Tables

### users

Stores user information.

Fields:

- ID
- Name
- Creation date

### balance

Stores balance information.

Fields:

- ID
- Balance

### income

Stores income records.

Fields:

- ID
- Amount
- Source
- Date
- Description

### expenses

Stores expense records.

Fields:

- ID
- Amount
- Date

### saving

Stores saving goals.

Fields:

- ID
- Target
- Amount
- Date

---

# 📁 Project Structure
