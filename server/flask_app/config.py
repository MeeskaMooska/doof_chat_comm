import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    GPU_SERVER_HOST = os.environ.get('GPU_SERVER_HOST', 'localhost')
    GPU_SERVER_PORT = int(os.environ.get('GPU_SERVER_PORT', 12345))
