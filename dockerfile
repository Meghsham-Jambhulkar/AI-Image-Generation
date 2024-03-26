# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python files into the container
COPY app.py StableDiffusionWrapper.py requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Streamlit port
EXPOSE 8501

# Define the command to run your Streamlit application
CMD ["streamlit", "run", "app.py"]
