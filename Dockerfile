FROM python:3.10-slim

# Set a descriptive working directory (matches your app name)
WORKDIR /trackerApp

# Copy files (will land in /trackerApp inside the container)
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (adjust if your app uses a different port)
EXPOSE 5000

# Run the app (ensure 'app.py' is in /trackerApp)
CMD ["python", "trackerApp.py"]