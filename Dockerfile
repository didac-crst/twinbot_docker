FROM python:3.10

# Install expect
RUN apt-get update && apt-get install -y expect

# Set the working directory
WORKDIR /app

# Copy the content of the local src directory to the working directory
COPY ./ /app/

# Install dependencies
RUN pip install -r requirements.txt

# Install cryptobot_core
RUN /bin/bash -c "pip install git+https://github.com/didac-crst/ollama_telegrambot_api.git"

# Set the environment variable for the Python buffer
ENV PYTHONUNBUFFERED=1

# Start the server
CMD ["unbuffer", "python", "src/twinbot_agent.py"]