# 🏥 Bajaj Finserv Health – Python Challenge Submission

Welcome! 👋 This repository contains the solution to the **Qualifier 1 Python Task** from **Bajaj Finserv Health**. The task involves interacting with a remote API, solving a SQL-based data query problem, and submitting the answer via an authenticated webhook.

---

## 🚀 What This Project Does

On startup, the Python script:
1. Sends a POST request to generate a webhook.
2. Receives a `webhook` URL and an `accessToken`.
3. Solves the assigned **SQL Query Problem** using mock employee and payment data.
4. Submits the final SQL query to the webhook with proper authentication.

---

## 🧠 SQL Problem Solved

We were tasked to:
- Identify the **highest salary** credited **not on the 1st of any month**
- Display the **employee name**, **age**, and **department** who received it

The final SQL query calculates age using `DATEDIFF` and filters out `PAYMENT_TIME` entries occurring on the 1st day.

---

## 🛠️ How to Run This Project

### Prerequisites
- Python 3.8+
- `pip` package manager
- Internet connection

### Steps
```bash
# Clone the repo
git clone https://github.com/your-username/bfh-python-project.git
cd bfh-python-project

# Install dependencies
pip install requests

# Run the script
python main.py

#thank for giving me the opportunity
