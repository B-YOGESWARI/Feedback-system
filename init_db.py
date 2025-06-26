# init_db.py

from database import engine
from models import Base

# Create all tables defined in models.py
Base.metadata.create_all(bind=engine)

print("✅ Tables created successfully!")
