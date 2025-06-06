# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV MODEL_PATH=./app/best_checkpoint_resnet18.model

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y curl
# Install Poetry
RUN pip install poetry




# Copy only the requirements files first to leverage Docker cache
COPY pyproject.toml poetry.lock README.md ./

# Install project dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --only main --no-interaction --no-ansi


# Copy the rest of the application
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "-m", "app.main"]

