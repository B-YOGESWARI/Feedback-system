import sys
import os

# ✅ Add current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from auth import routes
from feedback import router as feedback_router  # 👈 Import feedback routes

# ✅ Initialize the app
app = FastAPI()

# ✅ Register your routers
app.include_router(routes.router)
app.include_router(feedback_router)
from feedback import router as feedback_router
app.include_router(feedback_router)