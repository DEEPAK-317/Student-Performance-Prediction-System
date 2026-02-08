import logging
import os
from datetime import datetime

# Check if running on Vercel (or any environment where we can't write to filesystem freely)
# Vercel infrastructure usually sets some environment variables, or we can just rely on try-except blocks
# But for simplicity, we will just log to console (stream) which is best practice for serverless

logging.basicConfig(
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.StreamHandler()
    ]
)
