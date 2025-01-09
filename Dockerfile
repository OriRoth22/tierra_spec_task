# Example Dockerfile
FROM python:3.10-slim


# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your project files
COPY . .

# Specify the command to run your application
CMD ["python", "main.py"]