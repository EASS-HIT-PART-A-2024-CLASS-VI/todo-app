# השתמש בתמונה בסיסית של Python
FROM python:3.9-slim

# הגדרת תיקיית העבודה בתוך הקונטיינר
WORKDIR /app

# העתקת requirements.txt ותקנת החבילות
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# העתקת כל הקבצים
COPY . /app

# הגדרת הפורט של Streamlit
EXPOSE 8501

# הרצת Streamlit
CMD ["streamlit", "run", "app.py"]
