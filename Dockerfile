FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Salin file aplikasi ke dalam container
COPY . /app

# Install dependensi
RUN pip install Flask

# Ekspose port 5000
EXPOSE 5000

# Jalankan aplikasi
CMD ["python", "welcome.py"]
