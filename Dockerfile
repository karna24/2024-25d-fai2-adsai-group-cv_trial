# Stage 1: Build stage
FROM python:3.8-slim as builder

WORKDIR /app

# Install system dependencies (required for PyTorch)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install poetry
RUN pip install poetry==1.5.1

# Copy only requirements to cache them in docker layer
COPY pyproject.toml poetry.lock* /app/

# Install dependencies
RUN poetry config virtualenvs.in-project true && \
    poetry install --no-dev --no-interaction --no-ansi

# Stage 2: Runtime stage
FROM python:3.8-slim

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy virtual environment from builder
COPY --from=builder /app/.venv ./.venv
ENV PATH="/app/.venv/bin:$PATH"

# Copy application code
COPY ./app ./app
COPY ./models ./models

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]