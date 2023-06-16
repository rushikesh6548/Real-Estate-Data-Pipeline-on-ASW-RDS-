import os
import pandas as pd
import numpy as np
import opencage.geocoder
from keys import api_key

class Preprocessing():
    def __init__(self):
        self.raw_data_path = os.path.join('all_data','Real_Estate_Sales_2001-2020_GL.csv')
        self.preprocessed_data  = None


    def preprocess_data(self):
        # Reading the data that we got from data extraction process:
        data = pd.read_csv(f'{self.raw_data_path}')
        data = data.drop(["OPM remarks"], axis=1)

        town = ['Ansonia', 'Avon', 'Barkhamsted', 'Beacon Falls', 'Berlin',
                'Bethel', 'Bethlehem', 'Bolton', 'Branford', 'Bristol',
                'Brookfield', 'Burlington', 'Canton', 'Cheshire', 'Colchester',
                'Coventry', 'Cromwell', 'Danbury', 'Darien', 'Derby',
                'East Granby', 'East Haddam', 'East Hartford', 'East Haven',
                'East Lyme', 'Easton', 'East Windsor', 'Enfield', 'Essex',
                'Farmington', 'Franklin', 'Glastonbury', 'Goshen', 'Granby',
                'Greenwich', 'Griswold', 'Groton', 'Guilford', 'Hartford',
                'Harwinton', 'Killingly', 'Killingworth', 'Lebanon', 'Lisbon',
                'Litchfield', 'Madison', 'Manchester', 'Mansfield', 'Meriden',
                'Middlebury', 'Middletown', 'Milford', 'Monroe', 'Montville',
                'Naugatuck', 'New Britain', 'New Canaan', 'New Fairfield',
                'New Haven', 'New London', 'Newtown', 'North Canaan',
                'North Haven', 'Norwalk', 'Norwich', 'Old Lyme', 'Old Saybrook',
                'Orange', 'Plainfield', 'Plainville', 'Plymouth', 'Portland',
                'Preston', 'Putnam', 'Rocky Hill', 'Salem', 'Sharon', 'Shelton',
                'Simsbury', 'Southbury', 'South Windsor', 'Stamford', 'Stonington',
                'Stratford', 'Suffield', 'Thomaston', 'Thompson', 'Tolland',
                'Torrington', 'Trumbull', 'Vernon', 'Washington', 'Waterbury',
                'Waterford', 'Watertown', 'Westbrook', 'West Hartford', 'Hampton',
                'Wethersfield', 'Willington', 'Wilton', 'Winchester', 'Ashford',
                'Windham', 'Windsor Locks', 'Wolcott', 'Woodbridge', 'Woodstock',
                'Lyme', 'Colebrook', 'Bozrah', 'Bloomfield', 'Bridgeport',
                'Bethany', 'Columbia', 'Bridgewater', 'Kent', 'Hebron', 'Eastford',
                'Cornwall', 'Chaplin', 'Canaan', 'Andover', 'Chester', 'Hamden',
                'Clinton', 'East Hampton', 'Hartland', 'Deep River', 'Brooklyn',
                'Ridgefield', 'Redding', 'Middlefield', 'Morris', 'New Hartford',
                'Sherman', 'Norfolk', 'Scotland', 'Sprague', 'Roxbury', 'Sterling',
                'Somers', 'Newington', 'Windsor', 'Weston', 'Warren', 'Woodbury',
                'Wallingford', 'Union', 'Ellington', 'Canterbury', 'Stafford',
                'Pomfret', 'West Haven', 'Westport', 'Ledyard', 'Oxford',
                'Southington', 'New Milford', 'Voluntown', 'Fairfield', 'Durham',
                'Seymour', 'Salisbury', 'Marlborough', 'Haddam', 'Prospect',
                'North Branford', 'North Stonington']

        data['Location'] = pd.to_numeric(data['Location'], errors='coerce')



        # Create an OpenCage geocoder object
        geocoder = opencage.geocoder.OpenCageGeocode(api_key)

        # Define the list of towns
        towns = ['Ansonia', 'Avon', 'Barkhamsted', 'Beacon Falls', 'Berlin',
                 'Bethel', 'Bethlehem', 'Bolton', 'Branford', 'Bristol',
                 'Brookfield', 'Burlington', 'Canton', 'Cheshire', 'Colchester',
                 'Coventry', 'Cromwell', 'Danbury', 'Darien', 'Derby',
                 'East Granby', 'East Haddam', 'East Hartford', 'East Haven',
                 'East Lyme', 'Easton', 'East Windsor', 'Enfield', 'Essex',
                 'Farmington', 'Franklin', 'Glastonbury', 'Goshen', 'Granby',
                 'Greenwich', 'Griswold', 'Groton', 'Guilford', 'Hartford',
                 'Harwinton', 'Killingly', 'Killingworth', 'Lebanon', 'Lisbon',
                 'Litchfield', 'Madison', 'Manchester', 'Mansfield', 'Meriden',
                 'Middlebury', 'Middletown', 'Milford', 'Monroe', 'Montville',
                 'Naugatuck', 'New Britain', 'New Canaan', 'New Fairfield',
                 'New Haven', 'New London', 'Newtown', 'North Canaan',
                 'North Haven', 'Norwalk', 'Norwich', 'Old Lyme', 'Old Saybrook',
                 'Orange', 'Plainfield', 'Plainville', 'Plymouth', 'Portland',
                 'Preston', 'Putnam', 'Rocky Hill', 'Salem', 'Sharon', 'Shelton',
                 'Simsbury', 'Southbury', 'South Windsor', 'Stamford', 'Stonington',
                 'Stratford', 'Suffield', 'Thomaston', 'Thompson', 'Tolland',
                 'Torrington', 'Trumbull', 'Vernon', 'Washington', 'Waterbury',
                 'Waterford', 'Watertown', 'Westbrook', 'West Hartford', 'Hampton',
                 'Wethersfield', 'Willington', 'Wilton', 'Winchester', 'Ashford',
                 'Windham', 'Windsor Locks', 'Wolcott', 'Woodbridge', 'Woodstock',
                 'Lyme', 'Colebrook', 'Bozrah', 'Bloomfield', 'Bridgeport',
                 'Bethany', 'Columbia', 'Bridgewater', 'Kent', 'Hebron', 'Eastford',
                 'Cornwall', 'Chaplin', 'Canaan', 'Andover', 'Chester', 'Hamden',
                 'Clinton', 'East Hampton', 'Hartland', 'Deep River', 'Brooklyn',
                 'Ridgefield', 'Redding', 'Middlefield', 'Morris', 'New Hartford',
                 'Sherman', 'Norfolk', 'Scotland', 'Sprague', 'Roxbury', 'Sterling',
                 'Somers', 'Newington', 'Windsor', 'Weston', 'Warren', 'Woodbury',
                 'Wallingford', 'Union', 'Ellington', 'Canterbury', 'Stafford',
                 'Pomfret', 'West Haven', 'Westport', 'Ledyard', 'Oxford',
                 'Southington', 'New Milford', 'Voluntown', 'Fairfield', 'Durham',
                 'Seymour', 'Salisbury', 'Marlborough', 'Haddam', 'Prospect',
                 'North Branford', 'North Stonington']

        #Creating a dictionary to store the results
        results = {}

        # Loop through the towns and get their latitude and longitude
        for town in towns:
            # Build the query string for the town
            query = town + ', Connecticut'

            # Geocode the town
            response = geocoder.geocode(query)

            # Get the latitude and longitude from the response
            if len(response) > 0:
                lat = response[0]['geometry']['lat']
                lng = response[0]['geometry']['lng']
                results[town] = (lat, lng)
            else:
                results[town] = ("no", "no")
        def get_latitude(town):
            if town in results:
                return results[town][0]
            else:
                return None

        data['latitude'] = data['Town'].apply(get_latitude)

        def get_longitude(town):
            if town in results:
                return results[town][1]
            else:
                return None

        data['longitude'] = data['Town'].apply(get_longitude)

        data = data.dropna(subset=['latitude', 'longitude'])

        data = data.drop(['Location'], axis=1)
        data = data.drop(['Non Use Code'], axis=1)
        data = data.drop(['Assessor Remarks'], axis=1)
        data = data.dropna(subset=['Property Type', 'Residential Type'])
        data['Date Recorded'] = pd.to_datetime(data['Date Recorded'])

        data.to_csv(f"all_data/preprocessed.csv")


        print(data)






class DataTransformation():
    def __init__(self):
        preprocessing_obj = Preprocessing()
        self.preprocessed_data = preprocessing_obj.preprocess_data()

    def transform(self):
        data = self.preprocessed_data
        data = data.drop(['Unnamed: 0'], axis=1)
        data = data.drop_duplicates().reset_index(drop=True)
        datetime_dim = data['Date Recorded'].reset_index(drop=True)
        datetime_dim = np.array(datetime_dim)
        datetime_dim = pd.DataFrame(datetime_dim, columns=['sales_datetime'])
        datetime_dim['sales_datetime'] = pd.to_datetime(datetime_dim['sales_datetime'])
        datetime_dim['sales_hour'] = datetime_dim['sales_datetime'].dt.hour
        datetime_dim['sales_day'] = datetime_dim['sales_datetime'].dt.day
        datetime_dim['sales_month'] = datetime_dim['sales_datetime'].dt.month
        datetime_dim['sales_year'] = datetime_dim['sales_datetime'].dt.year
        datetime_dim['sales_weekday'] = datetime_dim['sales_datetime'].dt.weekday
        datetime_dim['list_year'] = data['List Year']
        datetime_dim['datetime_id'] = datetime_dim.index


        property_dim = data['Property Type'].reset_index(drop = True)
        property_dim = np.array(property_dim)
        property_dim = pd.DataFrame(property_dim)
        property_dim['residental_type'] = data['Residential Type']
        property_dim['property_id'] = property_dim.index



        # location dimnesion table :
        location_dim = data['Town'].reset_index(drop = True)
        location_dim = np.array(location_dim)
        location_dim = pd.DataFrame(location_dim,columns=['property_town'])
        location_dim['property_address'] = data['Address']
        location_dim['property_longitude'] = data['longitude']
        location_dim['property_latitude'] = data['latitude']
        location_dim['location_id'] = location_dim.index


        # Sales dimension table :
        sales_dim = data['Sale Amount'].reset_index(drop=True)
        sales_dim = np.array(sales_dim)
        sales_dim = pd.DataFrame(sales_dim, columns=['sales_amount'])
        sales_dim['sales_id'] = sales_dim.index
        sales_dim['sales_ratio'] = data['Sales Ratio']

        # Fact table dim:
        fact_table = data['Serial Number'].reset_index(drop=True)
        fact_table = np.array(fact_table)
        fact_table = pd.DataFrame(fact_table, columns=['sales_serial_number'])
        fact_table['sales_id_fact'] = fact_table.index
        fact_table['assessed_value'] = data['Assessed Value']
        fact_table['saled_dim_id'] = sales_dim['sales_id']
        fact_table['location_dim_id'] = location_dim['location_id']
        fact_table['datetime_id'] = datetime_dim['datetime_id']
        fact_table['property_id']= property_dim['property_id']


        fact_table.to_csv("fact_table.csv")
        datetime_dim.to_csv("datetime_dim.csv")
        location_dim.to_csv("location_dim.csv")
        property_dim.to_csv("property_dim.csv")
        sales_dim.to_csv("sales_dim.csv")




        return (fact_table,datetime_dim,location_dim,property_dim,sales_dim)





trnf = DataTransformation()
trnf.transform()