import subprocess
import time
import os
import json
import mysql.connector
from ftplib import FTP
from dotenv import load_dotenv
from ftplib import FTP
from datetime import datetime

load_dotenv()
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Start the exe file
subprocess.Popen(r"G:\brainstable\Site\Brainstable.Gsk.Centura.Site")
print("The Brainstable.Gsk.Centura.Site.exe file has been started.")

# Wait for 5 minutes
time.sleep(300)
print("5 minutes have passed. Checking if the JSON file exists...")

# FTP update reestrs
try:
    ftp = FTP()
    ftp.connect(os.environ['FTP_HOST'], int(os.environ['FTP_PORT']))
    ftp.login(os.environ['FTP_USERNAME'], os.environ['FTP_PASSWORD'])
    with open('logs.txt', 'a') as log_file:
            log_file.write(f"{current_time} - FTP connection - success\n")
except Exception as e:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('logs.txt', 'a') as log_file:
        log_file.write(f"{current_time} - FTP connection - {str(e)}\n")

ftp.cwd('www')
ftp.cwd('gossortrf.ru')
ftp.cwd('upload')
ftp.cwd('import')
#need to put file here 
for file_name in ['sorts1.json', 'sorts2.json', 'sorts3.json']:
    if os.path.exists(f'files/{file_name}'):
        with open(f'files/{file_name}', 'rb') as file:
            try:
                ftp.storbinary(f'STOR {file_name}', file)
                with open('logs.txt', 'a') as log_file:
                    log_file.write(f"{file_name} - success\n")
            except Exception as e:
                with open('logs.txt', 'a') as log_file:
                    log_file.write(f"{file_name} - {str(e)}\n")
    else:
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"{file_name} - file not found\n")


file_list = ftp.nlst()
print(file_list)

ftp.quit()

# Convert JSON to MySQL
json_file_path = r"files\nopatents.json"
if not os.path.exists(json_file_path):
    # Create a text file with a message indicating that the file was not found
    with open('logs.txt', 'a') as log_file:
        log_file.write(f"{json_file_path} - file not found\n")

    # Print a message to the console indicating that the file was not found and the text file was created
    print('The JSON file "nopatents.json" was not found.')
    with open('logs.txt', 'a') as log_file:
        log_file.write(f"------------------------------\n")
else:
    with open(json_file_path, encoding='utf-8') as json_file:
        data = json.load(json_file)
    varieties = data["Varieties"]
      
    # Connect to MySQL
    try:
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"Sql connection - success\n")
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_DATABASE')
        )
        
        cursor = conn.cursor()

        # Truncate the table to remove existing data
        cursor.execute("TRUNCATE TABLE mytable")

        # Create the table if it does not exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mytable (
                Kind VARCHAR(255),
                Name VARCHAR(255),
                Patent VARCHAR(255),
                Closed VARCHAR(255),
                Owners VARCHAR(255),
                PRIMARY KEY (Patent)
            )
        """)

        # Insert data into the table
        for item in varieties:
            print(item)
            try:
                cursor.execute("INSERT INTO mytable (Kind, Name, Patent, Closed, Owners) VALUES (%s, %s, %s, %s, %s)", 
                            (item['Kind'], item['Name'], item['Patent'], item['Closed'], item['Owners']))
            except mysql.connector.Error as err:
                print(f"Error occurred while inserting data: {err}")

        conn.commit()

    except mysql.connector.Error as err:
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"Sql connection - error\n")

    finally:
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"------------------------------\n")
        # Close the MySQL connection
        if 'conn' in locals() or 'conn' in globals():
            conn.close()