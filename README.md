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



---

### 🧭 Overview

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

### ⚙️ Tech Stack

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



# ### 2️⃣ Create and activate a virtual environment
# ```bash
# python -m venv venv
# # On Windows
# venv\Scripts\activate
# # On Mac/Linux
# source venv/bin/activate

# ---

# ###  3️⃣ Install dependencies
# ```bash
# pip install -r requirements.txt


# 4️⃣ Apply migrations
# ```bash
# python manage.py migrate


# 5️⃣ (Optionally) Seed sample data
# python manage.py seed


# 6️⃣ Run the server
# python manage.py runserver


# 📡 API Endpoints
# Base URL: http://127.0.0.1:8000/api/

# | Endpoint                               | Method   | Description                                     |
# | -------------------------------------- | -------- | ----------------------------------------------- |
# | `/drones/`                             | **POST** | Register a new drone                            |
# | `/drones/`                             | **GET**  | List all drones                                 |
# | `/drones/<serial_number>/load/`        | **POST** | Load a drone with medication (if battery > 25%) |
# | `/drones/<serial_number>/medications/` | **GET**  | Get medications loaded on a specific drone      |
# | `/drones/available/`                   | **GET**  | List available drones for loading               |
# | `/drones/<serial_number>/battery/`     | **GET**  | Check a drone’s battery level                   |



# 🧪 ### Example Requests
# 📝 ### Register a new drone

# POST ### /api/drones

# ```json
# {
#   "serial_number": "DRN2001",
#   "model": "Lightweight",
#   "weight_limit": 250,
#   "battery_capacity": 90,
#   "state": "IDLE"
# }

# ### Response (201 Created)

# ```json
# {
#   "serial_number": "DRN2001",
#   "model": "Lightweight",
#   "weight_limit": 250,
#   "battery_capacity": 90,
#   "state": "IDLE"
# }


# 📦 ### Load drone with medication

# POST /api/drones/DRN2001/load/

# ```json
# {
#   "medications": [
#     { "name": "Panadol", "weight": 50, "code": "P001" }
#   ]
# }

# ### Response (201 Created)

# ```json
# {
#   "message": "Medication loaded successfully."
# }