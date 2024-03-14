FROM python:3-slim

# Set working directory
WORKDIR /usr/src/app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy server code
COPY ./server/python/server.py ./server/

# Copy client code
COPY ./client/*.html ./client/

# Set the default command to run your server script
CMD [ "python", "./server/server.py"]
