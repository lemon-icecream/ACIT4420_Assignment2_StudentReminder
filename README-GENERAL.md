# 📘 Study Reminders

The **Study Reminders** package is a Python application that generates, logs, and schedules study reminders for students.  
It reads student data, creates personalized reminder messages, and automatically sends them based on each student’s preferred reminder time.  

---

## 🧩 Overview

This project demonstrates modular software design using Python packages and classes.  
It integrates **logging**, **data management**, **reminder generation**, and **task scheduling** to simulate a simple reminder system.

---

## ⚙️ Features

- Load student data from a JSON file or use built-in test data  
- Generate personalized study reminders  
- Log all system activity with timestamps  
- Send reminders immediately (test mode) or at scheduled times (normal mode)  
- Fully modular and extendable structure  

---

## 📁 Project Structure

```
src/
├── resources/
│   ├── app_log.txt          # Log file (created automatically)
│   ├── requirements.txt     # Project dependencies
│   └── students.json        # Student data file
│
├── study_reminders/
│   ├── logger/
│   │   └── logger.py
│   ├── reminder/
│   │   ├── reminder.py
│   │   └── reminder_generator.py
│   ├── student/
│   │   ├── student.py
│   │   └── student_manager.py
│   ├── student_reminder/
│   │   ├── student_reminder.py
│   │   ├── student_reminder_manager.py
│   │   └── student_reminder_sender.py
│   └── reminder_scheduler.py
│
├── main.py                  # Application entry point
└── setup.py                 # Setup script for packaging
```

---

## ⚙️ Build and run
[View Technical Documentation](README-TECHNICAL.md)

---

## 🧾 Logs

All application activity is logged to:
```
resources/app_log.txt
```

---

## 🧪 Testing

You can run the main test in `test.py`.  
Or run the below command:
```bash
PYTHONPATH=src python3 -m unittest discover -s test
```

Or run the main app in test mode:
```bash
cd src
python3 main.py --test
```

---

## 🧑‍💻 Author

**Mai Vu**