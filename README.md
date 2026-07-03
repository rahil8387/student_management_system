# 🎓 Student Management System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange?style=for-the-badge)
![CLI](https://img.shields.io/badge/CLI-Terminal-lightgrey?style=for-the-badge)
![Database](https://img.shields.io/badge/Database-Pickle-green?style=for-the-badge)

</p>

A **Student Management System** built using Python that allows users to manage student records through both a **Command Line Interface (CLI)** and a **Graphical User Interface (GUI)**.

The application helps users **add, search, view, and delete student records** while storing all data locally using Python's **Pickle** module. Both the GUI and CLI share the same database, ensuring data remains synchronized.

---

# 🚀 Features

* ➕ Add new student records
* 📋 View all stored records
* 🔍 Search students using Roll Number
* 🗑️ Delete student records safely
* 💾 Local database using Pickle
* 🖥️ Two interfaces (GUI & CLI)
* ✅ Input validation to prevent errors
* 🔄 Shared database between GUI and CLI

---

# 🛠️ Tech Stack

| Technology   | Purpose                  |
| ------------ | ------------------------ |
| 🐍 Python    | Programming Language     |
| 🖥️ Tkinter  | Graphical User Interface |
| 💻 CLI       | Terminal-based Interface |
| 💾 Pickle    | Local Data Storage       |
| 📁 OS Module | File Management          |

---

# 📂 Project Structure

```text
Student_Management_System/
│
├── students.py        # Student class
├── storage.py         # Database operations
├── menu.py            # Command Line Interface
├── gui.py             # Graphical User Interface
├── stu.pkl            # Local database file
└── README.md
```

---

# ⚙️ How It Works

```text
          User
            │
            ▼
  GUI / Command Line
            │
            ▼
   Input Validation
            │
            ▼
 Database Operations
(Add / Search / Delete)
            │
            ▼
      Pickle Database
            │
            ▼
     Updated Interface
```

---

# 🖥️ Application Preview

```text
+----------------------------------------------------------+
|              Student Management System                   |
+----------------------------------------------------------+
| Student Name :  _________________________                |
| Roll Number :  _________________________                 |
| Marks        :  _________________________                |
+----------------------------------------------------------+
|  Add  |  View  |  Search  |  Delete  |  Exit             |
+----------------------------------------------------------+
|                                                  Output  |
| ------------------------------------------------------   |
| Name : John Doe                                         |
| Roll : 101                                              |
| Marks: 92                                               |
| ------------------------------------------------------   |
+----------------------------------------------------------+
```

---

# 📌 Project Workflow

```text
User Input
     │
     ▼
Input Validation
     │
     ▼
Storage Manager
     │
     ▼
Pickle Database
     │
     ▼
Updated GUI / CLI
```

---

# 🎯 Learning Outcomes

This project helped in understanding:

* Object-Oriented Programming (OOP)
* File Handling
* Pickle Serialization
* GUI Development using Tkinter
* CLI Application Development
* Data Validation
* Modular Programming
* Local Database Management

---

# 🌟 Future Improvements

* 🔐 User Authentication
* 🗄️ MySQL Database Integration
* 📊 Student Performance Dashboard
* 📄 Export Records to Excel/PDF
* 🌐 Web-Based Version
* ☁️ Cloud Database Support

---

# 👨‍💻 Developer

**Rahil Saini**

📧 **Email:** [rahilsaini2003@gmail.com](mailto:rahilsaini2003@gmail.com)

🔗 **LinkedIn:** https://www.linkedin.com/in/rahil-saini/

---

# ⭐ If you found this project useful, don't forget to give it a Star!
