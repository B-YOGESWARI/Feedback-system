# 1. Use official Python image
FROM python:3.11

# 2. Set the working directory
WORKDIR /app

# 3. Copy project files into the container
COPY . .

# 4. Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 5. Expose port to access FastAPI
EXPOSE 8000

# 6. Run FastAPI using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]