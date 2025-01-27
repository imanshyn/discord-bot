# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY requirements.txt ./
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg libopus0
COPY bot.py ./

# Run bot.py when the container launches
CMD ["python", "bot.py"]
