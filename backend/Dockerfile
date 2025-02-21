# בחר תמונה בסיסית מ-Docker Hub
FROM python:3.9-slim

# הגדרת תיקיית העבודה בתוך הקונטיינר
WORKDIR /app

# העתקת קובץ requirements.txt
COPY requirements.txt /app/

# התקנת התלויות
RUN pip install --no-cache-dir -r requirements.txt

# העתקת יתר הקבצים
COPY . /app/

# הפעלת היישום שלך (למשל, FastAPI)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
