# issue docker build/run commands from the same dir as the Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.6

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# RUN python -m nltk.downloader punkt

# Define environment variable
ENV FLASK_ENV="docker"

EXPOSE 5000

# Run app.py when the container launches
# CMD ["python", "app.py"]
CMD ["gunicorn", "--config=gunicorn.py", "app:app"]

#based on: https://matthewminer.com/2015/01/25/docker-dev-environment-for-web-app.html
#build: docker build --tag=python-tokenizer .
#run: docker run -it --publish=5000:5000 --env="MODE=dev" --volume=$PWD:/app:ro python-tokenizer
      #docker run -it -p 5000:5000 --env="MODE=dev" --volume=$PWD:/app:ro python-tokenizer
