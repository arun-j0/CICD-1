# Use a lightweight Python 3.11 image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port that the application will run on
EXPOSE 8080

# Set environment variable for the port
ENV PORT=8080

# Run the FastAPI application with Uvicorn, binding to the specified port
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
