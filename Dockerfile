# Dockerfile, Image, Container

FROM python:3.12.5

# Copy the Python script into the container
COPY rps.py .

# Set the command to run the script
CMD ["python", "rps.py"]

#commands I used:
#USE the "docker run -i -t python.rps" command in order to run interactive mode so user input won't break
#tag image :docker tag python.rps levivanberkel/python.rps:latest
#push image docker push levivanberkel/python.rps:latest

