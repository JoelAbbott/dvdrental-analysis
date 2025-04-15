# 🐍 This script connects to my PostgreSQL database and 
# performs a SQL SEKECT query using psycopg2.

# 📦 Step 1: Import the necessary libraries
import psycopg2 # 🔌Used to connect python to PostgreSQL databases
import pandas as pd  # 🐼 Lets us load query results into a DataFrame (python version of SQL table)
import logging # 📜 Used to log messages to a file

# 🧱 Step 2: Set uo logging to track what the script is doing (stored in logs/query.log)
logging.basicConfig(
    filename = "logs/query.log", # 📂 File to store logs
    level = logging.INFO, # 📊 Set logging level to INFO and above
    format = "%(asctime)s - %(levelname)s - %(message)s" # 📝 Format of the log messages
)

# 🔑 Step 3: Define your database connection settings
# ⚠️ These must match yout PostgreSQL setup from pgAdmin
db_settings = {
    "host": "localhost", # 🏠 Hostname of the PostgreSQL server
    "port": 5432, # 🔌 Port number for PostgreSQL (default is 5432)
    "database": "your_database_name", # 📦 Name of your database
    "user": "your_username", # 👤 Your PostgreSQL username
    "password": "your_password" # 🔑 Your PostgreSQL password
}

try:
    # 🔗 Step 4: Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(**db_settings) # 🏗️ Create a connection object using the settings

    # 📊 Step 5: Define your SQL query
    sql_query = "SELECT * FROM your_table_name;" # 📝 Replace with your SQL query

    # 🐼 Step 6: Load the SQL query results into a pandas DataFrame
    df = pd.read_sql_query(sql_query, connection) # 📊 Execute the query and load results into a DataFrame

    # 🖨️ Step 7: Print the DataFrame to the console
    print(df.head()) # 🖨️ Display the first few rows of the DataFrame

    # 📂 Step 8: Log a success message
    logging.info("✅ SELECT query executed and data loaded successfully.")

except Exception as e:
    # 🛑 If anything goes wrong, log the error
    logging.error(f"❌ Error occurred: {e}") # 🛑 Log the error message
    print("Something went wrong. Please check your logs/query.log.")

finally:
    # 🧹 Step 9: Always close the database connection to avoid resource leaks
    if 'connection' in locals():
        connection.close()
        logging.info("🔒 Database connection closed.")