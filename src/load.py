import mysql.connector
import pandas
from src.transform import DataTransformation




class DataLoader():
    def __init__(self):
        # Making a connection to our Database on AWS RDS everytime this object is called :

