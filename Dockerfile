# Use the official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8080

# Run using Gunicorn (production WSGI server)
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080"]
