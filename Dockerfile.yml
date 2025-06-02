# Use official Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

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

# Copy project files
COPY . .

# Install Poetry
RUN pip install poetry==1.7.1

# Install dependencies
RUN poetry install --no-root

# Expose port for Odoo
EXPOSE 8069

# Start Odoo (you may need to change the command based on your app structure)
CMD ["poetry", "run", "python", "odoo-bin", "-c", "odoo.conf"]
