import requests

# 1. Applicant details
data = {
    "name": "Hariom Mandloi",
    "regNo": "0827CD221033",
    "email": "hariommandloi220532@acropolis.in"
}

# 2. Generate webhook and access token
url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
response = requests.post(url, json=data)
response_data = response.json()

# Extract access token and webhook URL
access_token = response_data["accessToken"]
webhook_url = response_data["webhook"]
print("Access Token and Webhook URL fetched successfully.")

# 3. Final SQL query (based on Question 1 — REG number ends with odd digit)
final_query = """
SELECT 
    p.AMOUNT AS SALARY,
    CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,
    FLOOR(DATEDIFF(CURDATE(), e.DOB) / 365) AS AGE,
    d.DEPARTMENT_NAME
FROM PAYMENTS p
JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
WHERE DAY(p.PAYMENT_TIME) != 1
ORDER BY p.AMOUNT DESC
LIMIT 1;
"""

# 4. Submit final SQL query
headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}
payload = {
    "finalQuery": final_query.strip()
}
submit_url = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"
submit_response = requests.post(submit_url, headers=headers, json=payload)

# 5. Result
if submit_response.status_code == 200:
    print("SQL query submitted successfully!")
else:
    print(f"Submission failed. Status code: {submit_response.status_code}")
    print(submit_response.text)
