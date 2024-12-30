# Use a smaller, but still secure, official Python runtime as a parent image
FROM python:3.10-slim

# Create a non-root user called 'Jovic' and a group 'jovicgroup'
RUN addgroup --system jovicgroup && adduser --system --ingroup jovicgroup jovic

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Change to the non-root user 'Jovic'
USER jovic

# Define the command to run your app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
