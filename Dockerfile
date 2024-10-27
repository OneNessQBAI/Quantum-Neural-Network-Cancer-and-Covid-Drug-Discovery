# Use NVIDIA CUDA base image for GPU acceleration
FROM nvidia/cuda:11.8.0-runtime-ubuntu22.04

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Install medical databases and tools
RUN pip3 install --no-cache-dir \
    pydicom \
    nibabel \
    biopython \
    rdkit \
    pubchempy \
    chembl_webresource_client

# Copy application code
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV CUDA_VISIBLE_DEVICES=0
ENV QNN_MODE=production

# Expose ports
EXPOSE 8000
EXPOSE 8501

# Run the application
CMD ["python3", "quantum_medical_system.py"]
