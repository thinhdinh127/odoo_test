# Use official Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libsasl2-dev \
    libldap2-dev \
    libssl-dev \
    python3-dev \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy only poetry files first (to leverage Docker cache)
COPY pyproject.toml poetry.lock* /app/

# Install Poetry
RUN pip install poetry==1.7.1

# Install dependencies (without root package)
RUN poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the app source code
COPY . /app

# Expose port for Odoo
EXPOSE 8069

# Start Odoo with poetry
CMD ["poetry", "run", "python", "odoo-bin", "-c", "odoo.conf"]
