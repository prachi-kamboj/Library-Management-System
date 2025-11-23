# 📚 Library Management System

## ✨ Overview
* 💻 This is a basic **console application** built in **Python** to simulate core library operations.
* It allows users to add books, view the current inventory, and manage the checkout and return status of books efficiently.

---

## 🔑 Features

* ➕ **Add New Book**: Seamlessly add new books to the inventory.
* 📖 **View Catalog**: See all books with their author, publication year, and current availability status.
* ➡️ **Checkout Book**: Mark an available book's status as **"Checked Out"**.
* ⬅️ **Return Book**: Change a checked-out book's status back to **"Available"**.

---

## 🔧 Technologies/Tools Used

* 🐍 **Python 3** (The primary implementation language)
* 🧱 **Basic Python Data Structures** (Lists and Dictionaries for storage)
* 🚦 **Conditional Statements** (`if`, `elif`, `else` for logic and validation)
* 🔄 **Looping** (`while` loop for the main menu flow)

---

## 🚀 Getting Started

### Steps to Install & Run the Project

1.  ✅ Ensure you have **Python 3** installed on your system.
2.  💾 Save the provided code with a file name (e.g., `lms.py`) and the **`.py`** extension.
3.  🖥️ Open your terminal or command prompt.
4.  📁 Navigate to the directory where you saved the file.
5.  ▶️ Run the application using the command:
    ```bash
    python filename.py
    ```

### ✨ Instructions for Testing 

Use the menu options (**1-4**) to comprehensively test the functionality:

1.  **Add Book :** Try adding a few different books to populate the system.
2.  **View Books :** Verify that all added books appear correctly with the right details.
3.  **Checkout Book :**
    * Test checking out an **available** book (Success case).
    * Test trying to check out an **already checked out** book (Error message test).
4.  **Return Book :** Try returning a previously checked-out book.
