# 🚁 Drone Medication Delivery API

This project is a **Django REST Framework** backend for managing drones and their medications.  
It was built as part of an internship backend assessment, focusing on API design, validation, and clean backend architecture.

---

## 🧭 Overview

The system allows administrators to:

- Register new drones  
- Load drones with medications (if battery > 25%)  
- Check which medications are loaded on a specific drone  
- View available drones for loading  
- Check a drone’s battery level  

It also includes validation logic to ensure that:
- No drone exceeds its weight limit (max 500 g)
- Drones with less than 25% battery cannot be loaded
- Drone serial numbers are unique
- Each medication has a name, weight, code, and optional image

---

## ⚙️ Tech Stack

- **Language:** Python 3.11+
- **Framework:** Django 5 + Django REST Framework
- **Database:** SQLite (default)
- **Testing:** Pytest + DRF Test Client
- **Media Handling:** Django media upload (local)

---

## 🚀 Getting Started


### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/drone-medication-api.git
cd drone-medication-api


### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate


###  3️⃣ Install dependencies
```bash
pip install -r requirements.txt