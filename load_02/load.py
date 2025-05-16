import sys
import os
from dotenv import load_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ingest_01 import ingest
from sqlalchemy import create_engine

# looks for .env in the main directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../config/.env'))  

# Load environment variables
db_user = os.getenv("db_user")
db_pass = os.getenv("db_pass")

# Check if environment variables are loaded
engine = create_engine(
    f"postgresql://{db_user}:{db_pass}@localhost:5432/postgres"
)

# Check if the engine is created successfully
print(ingest.df.head())
print(f"Number of rows: {len(ingest.df)}")

# Check if the DataFrame is not empty
try:
    ingest.df.to_sql("spotify_plays", engine, if_exists="append", index=False)
    print("Data written to database.")
# Check if the data is written successfully
except Exception as e:
    print("Error writing to database:", e)
