## UPI Fraud Shield - Backend

This is the backend server for the UPI Fraud Shield project, built with **Flask** and integrated with **Firebase** to provide real-time fraud detection and data storage.

### 🚀 Features

* **Flask Web Server**: Handles API requests for transaction verification.
* **Firebase Integration**: Real-time database management for storing and retrieving transaction logs.
* **Fraud Analysis**: (Add specific logic here, e.g., "Uses machine learning to flag suspicious UPI patterns").

### 🛠️ Tech Stack

* **Language**: Python
* **Framework**: Flask
* **Database**: Firebase (Google Cloud)
* **Version Control**: Git & GitHub

### 📋 Prerequisites

Before running this project, ensure you have:

* Python 3.x installed.
* A Firebase Service Account key (`firebase_key.json`).

### ⚙️ Installation & Setup

1. **Clone the repository**:
```bash
git clone https://github.com/Innovex-04/upi-fraud-shield.git
cd Backend

```


2. **Install dependencies**:
```bash
pip install -r requirements.txt

```


3. **Add your Firebase Key**:
Place your `firebase_key.json` file in the root directory. (Note: This file is ignored by Git for security).
4. **Run the server**:
```bash
python app.py

```

The server will start at `http://127.0.0.1:5000`.
