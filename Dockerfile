FROM python:3.9

# Set working directory in Docker image
WORKDIR /app

# Copy current directory from machine into container
COPY . .

# Install the function's dependencies using file requirements.txt
# from your project folder.
RUN  pip3 install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable to use port 80
ENV UVICORN_PORT=80 UVICORN_HOST=0.0.0.0

# Run the application using Uvicorn when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]