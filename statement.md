# 🎯 Project Statement: Simple Library Management System

## ⚠️ Problem Statement
The lack of a structured, digital mechanism to track library inventory and lending status leads to manual errors and delays in determining a book's availability. This project addresses the critical need for a simple, automated inventory and lending status tracker.

---

## 🗺️ Scope of the Project
The scope is strictly limited to **console-based operations** : book creation, book listing, and status updates (checkout/return).

* **In-Scope:** Uses **volatile memory** (a global list) for runtime data storage.
* **Out-of-Scope:** Does **not** include persistent data storage (database/file I/O) or user authentication.

---

## 👤 Target Users
This tool is designed for efficient, small-scale library management:

* 📚 A **Librarian** or **administrator** responsible for maintaining a small catalog.
* 🎓 A **Student** or **individual** needing to manage their personal book collection.

---

## 💡 High-Level Features
The system provides two core capabilities:

1.  **📦 Inventory Management (Add/View)**: The ability to track and list all available books.
2.  **🔄 Status Tracking (Checkout/Return)**: The functionality to quickly update a book's lending status.
