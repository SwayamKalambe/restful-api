from database import engine
from models import Base
import time
from sqlalchemy.exc import OperationalError

def create_tables(retries=5, delay=2):
    """Attempts to create database tables with retry logic."""
    for attempt in range(retries):
        try:
            print("Attempting to create tables...")  # Log the attempt
            Base.metadata.create_all(bind=engine)
            print("Tables created successfully.")  # Success message
            return  # Exit function if successful
        except OperationalError as e:
            print(f"Database error: {e}")
            if attempt == retries - 1:
                print("Max retries reached. Exiting.")
                raise  # Re-raise the exception after max retries
            print(f"Retrying in {delay} seconds... (Attempt {attempt + 1}/{retries})")
            time.sleep(delay)

if __name__ == "__main__":
    create_tables()