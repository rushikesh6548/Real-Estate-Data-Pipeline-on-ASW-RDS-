import mysql.connector
import pandas
from src.keys import db_pass,db_endpoint,db_username
from src.transform import DataTransformation




class DataLoader():
    def __init__(self):
        # Making a connection to our Database on AWS RDS everytime this object is called :



        conn = mysql.connector.connect(
            user=db_username,
            password=db_pass,
            host=db_endpoint,
            port=3306,
        )
        print("Successfully connected to the database!")


        # Also let us get the transformed data here :
        trn_obj = DataTransformation()
        self.fact_table ,self.datetime_dim, self.location_dim , self.property_dim,self.sales_dim = trn_obj.transform()

        print(self.fact_table,self.property_dim,self.datetime_dim,self.sales_dim,self.location_dim)

    def create_database(self):
        try:
            conn = mysql.connector.connect(
                user=db_username,
                password=db_pass,
                host=db_endpoint,
                port=3306
            )
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS realestatedb")
            print("Successfully created database!")
        except mysql.connector.Error as e:
            print(f"Error creating database: {e}")

    def create_tables(self):
        try:
            conn = mysql.connector.connect(
                user=db_username,
                password=db_pass,
                host=db_endpoint,
                database="realestatedb",
                port=3306
            )
            print("Successfully connected to the database!")
        except mysql.connector.Error as e:
            print(f"Error connecting to the database: {e}")

        # Create a new table in the database
        try:
            # First creating all the dimension tables :
            # Property dimension :
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS property_dim (
                    property_id INT PRIMARY KEY ,
                    property_type VARCHAR(100) 
                    
                )
            """)
            print("Successfully created table : Property_dim}")

            conn.commit()
        except mysql.connector.Error as e:
            print(f"Error creating table: {e}")


        # Crearing the Datetime Dimension table :
        try:
            # First creating all the dimension tables :
            # Property dimension :
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS datetime_dim (
                    datetime_id INT PRIMARY KEY,
                    sales_datetime DATETIME NOT NULL,
                    sales_hour INT NOT NULL,
                    sales_day INT NOT NULL,
                    sales_month INT NOT NULL,
                    sales_year INT NOT NULL,
                    sales_weekday INT NOT NULL,
                    list_year INT NOT NULL

                )
            """)
            print("Successfully created table : Datetime_dim")
            conn.commit()
        except mysql.connector.Error as e:
            print(f"Error creating table: {e}")


        try:
            # Creating the sales dimension table
            cursor = conn.cursor()
            cursor.execute("""
                            CREATE TABLE IF NOT EXISTS sales_dim (
                                sales_id INT PRIMARY KEY,
                                sales_amount FLOAT, 
                                sales_ratio FLOAT

                            )
                        """)
            print("Successfully created table : Sales_dim")
            conn.commit()
        except mysql.connector.Error as e:
            print(f"Error creating table: {e}")


        # Creating the location_dim table
        try:

            cursor = conn.cursor()
            cursor.execute("""
                            CREATE TABLE IF NOT EXISTS location_dim (
                                location_id INT PRIMARY KEY,
                                property_town VARCHAR(255),
                                property_address VARCHAR(255),
                                property_longitude FLOAT,
                                property_latitude FLOAT

                            )
                        """)
            print("Successfully created table : location_dim ")
            conn.commit()
        except mysql.connector.Error as e:
            print(f"Error creating table: {e}")


        # Creating the fact table :
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sales (
                    sales_serial_number INT PRIMARY KEY,
                    sales_id_fact INT NOT NULL,
                    assessed_value INT NOT NULL,
                    sales_id INT NOT NULL,
                    location_id INT,
                    datetime_id INT,
                    property_id INT,
                    FOREIGN KEY (sales_id) REFERENCES sales_dim(sales_id),
                    FOREIGN KEY (location_id) REFERENCES location_dim(location_id),
                    FOREIGN KEY (datetime_id) REFERENCES datetime_dim(datetime_id),
                    FOREIGN KEY (property_id) REFERENCES property_dim(property_id)
                )
            """)
            print("Successfully created table!")
        except mysql.connector.Error as e:
            print(f"Error creating table: {e}")


    def fill_table_values(self):
        # We fill all the tables with out transformed values :
        # First filling the sales_dim :
        try:
            conn = mysql.connector.connect(
                user=db_username,
                password=db_pass,
                host=db_endpoint,
                database="realestatedb",
                port=3306
            )
            print("Successfully connected to the database!")
        except mysql.connector.Error as e:
            print(f"Error connecting to the database: {e}")

        try:
            for i, row in self.sales_dim.iterrows():

                cursor = conn.cursor()
                cursor.execute(f"""INSERT INTO realestatedb.sales_dim(sales_amount , sales_id , sales_ratio)
                                    VALUES
                                    ({row[0]},{row[1]},{row[2]})
                            """)

            conn.commit()
            cursor.execute("SELECT * FROM sales_dim")
            cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error : {e}")







obj_dataloader = DataLoader()
obj_dataloader.fill_table_values()