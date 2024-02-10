import os

import databases
import sqlalchemy
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@192.168.1.39:5432/complaints"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
