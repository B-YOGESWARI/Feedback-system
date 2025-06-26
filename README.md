 ## Employee Feedback System – FastAPI Project

Hi! I'm B. Yogeswari, and this is a simple **Employee Feedback System** I built using **FastAPI**. The goal of this project is to allow managers to give feedback to employees based on their performance.

It’s designed to be simple, fast, and easy to use – perfect for learning and demo purposes!

## What You Can Do with This App

1. Sign up and log in as a user (either a manager or employee)  
2. Managers can submit feedback like strengths, areas to improve, and overall sentiment  
3. View all feedbacks in a structured format  
4. All data is stored safely in a local database using SQLAlchemy and SQLite  

## Tech I Used

- **FastAPI** – backend framework  
- **SQLite** – lightweight local database  
- **SQLAlchemy** – ORM to interact with the database  
- **Uvicorn** – to run the FastAPI server  
- **Pydantic** – for data validation and schema management  

## Project Structure
feedback-system/
│
├── main.py # Entry point of the app
├── models.py # Database tables
├── database.py # DB connection setup
├── requirements.txt # Python packages
├── README.md # You’re reading it now!
│
├── auth/ # User login/signup
│ ├── routes.py
│ ├── schemas.py
│ └── utils.py
│
└── feedback.py # Feedback submission & viewing

## How to Run the Project

### Step 1: Clone the project or download the folder  
git clone <your-repo-url>
cd feedback-system
## Step 2: Create a virtual environment
python -m venv venv
venv\Scripts\activate  # For Windows
## Step 3: Install the required packages
pip install -r requirements.txt
## Step 4: Start the app
uvicorn main:app --reload
Then, open your browser and go to: http://127.0.0.1:8000/docs

**API Routes**
POST /signup → Register a new user

POST /login → Login and receive token

POST /feedback → Submit feedback

GET /feedback → View all feedback

## A Note from Me
This project helped me understand backend development, routing, and working with databases.
I’m continuing to improve it and hope it’s useful as a learning demo!

Thanks for checking it out! 😊
Feel free to connect with me for suggestions or collaboration.

B. Yogeswari
🔗 LinkedIn: https://www.linkedin.com/in/yogeswari-boreddi-2161022a7/
