import os

# S3 Configuration - Adjust these according to your environment
S3_BUCKET = os.getenv("S3_BUCKET", "my-background-removal-bucket")
S3_REGION = os.getenv("S3_REGION", "us-east-1")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY", "YOUR_S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY", "YOUR_S3_SECRET_KEY")

# Path to U2NET weights
U2NET_WEIGHTS = os.getenv("U2NET_WEIGHTS", "/app/u2net/u2net.pth")
