# docker build -t blk-hacking-ind-vinayak-kumar .
FROM python:3.12-slim
# Selection criteria: The 'slim' variant of the Python image uses a Linux Debian-based distribution. 
# It is selected because it provides a lightweight footprint (reducing container size) 
# while maintaining full compatibility with the required C-extensions for FastAPI.

# Set working directory
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY main.py .

# Requirement: Expose the specified port
EXPOSE 5477

# Requirement: Run on port 5477 inside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5477"]