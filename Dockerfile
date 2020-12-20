FROM python:3.8.6-buster

# Install system dependencies for application.
RUN apt-get update
# For opencv-contrib-python:
RUN apt-get install -y libgl1-mesa-glx

# Create non-root user.
RUN mkdir -p /home/vfa
RUN useradd -r -g users -u 1000 vfa
RUN mkdir -p /home/vfa
RUN chown -R vfa:users /home/vfa

# Drop into non-root user.
USER vfa
WORKDIR /home/vfa

# Set up pipenv.
ENV PATH=/home/vfa/.local/bin:$PATH
RUN pip install --upgrade pip
RUN pip install pipx
RUN pipx install pipenv

# Copy application and install dependencies.
WORKDIR /home/vfa/app
COPY . /home/vfa/app
RUN pipenv install --deploy

# Run application.
CMD [ "pipenv", "run", "python", "vfa.py" ]
