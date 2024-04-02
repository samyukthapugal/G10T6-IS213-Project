FROM python:3-slim

# Set working directory
WORKDIR /usr/src/app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy server, client HTML and CSS files, and .env file
COPY ./server/python/server.py ./server/
# COPY ./client/html/*.html ./client/
# COPY ./client/html/css/*.css ./client/css/
COPY .env .

# Set the default command to run your server script
CMD [ "python", "./server/server.py"]
