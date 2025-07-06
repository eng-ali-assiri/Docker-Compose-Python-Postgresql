# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Install any needed dependencies specified in requirements.txt
RUN pip install psycopg2 && pip install psycopg2-binary

# Copy the current directory contents into the container at /app
COPY . .

# Make port 8080 available to the world outside this container
#EXPOSE 5000

# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["python", "habittrackerapp.py"]
