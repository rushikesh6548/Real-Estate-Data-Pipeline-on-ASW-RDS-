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

        # Create a dictionary to store the results
        # results = {}
        #
        # # Loop through the towns and get their latitude and longitude
        # for town in towns:
        #     # Build the query string for the town
        #     query = town + ', Connecticut'
        #
        #     # Geocode the town
        #     response = geocoder.geocode(query)
        #
        #     # Get the latitude and longitude from the response
        #     if len(response) > 0:
        #         lat = response[0]['geometry']['lat']
        #         lng = response[0]['geometry']['lng']
        #         results[town] = (lat, lng)
        #     else:
        #         results[town] = ("no", "no")
        results = {'Ansonia': (41.3429922, -73.0787468), 'Avon': (41.8098209, -72.8306541), 'Barkhamsted': (41.9292629, -72.9139904), 'Beacon Falls': (41.4428745, -73.062608), 'Berlin': (41.621488, -72.7456519), 'Bethel': (41.3712063, -73.4140097), 'Bethlehem': (41.6393626, -73.2080798), 'Bolton': (41.7689878, -72.4334173), 'Branford': (41.2795414, -72.8150989), 'Bristol': (41.6735209, -72.9464859), 'Brookfield': (41.4825947, -73.4095652), 'Burlington': (41.7692648, -72.9645484), 'Canton': (41.8245424, -72.8937122), 'Cheshire': (41.4989861, -72.900658), 'Colchester': (41.5756543, -72.3320269), 'Coventry': (41.7700987, -72.3050803), 'Cromwell': (41.5949942, -72.6455665), 'Danbury': (41.394817, -73.4540111), 'Darien': (41.0787079, -73.4692873), 'Derby': (41.3223611, -73.0890324), 'East Granby': (41.9412081, -72.7273158), 'East Haddam': (41.4529215, -72.4613902), 'East Hartford': (41.7823216, -72.6120346), 'East Haven': (41.2762081, -72.8684337), 'East Lyme': (41.3569909, -72.2258709), 'Easton': (41.2528738, -73.2973394), 'East Windsor': (41.9156316, -72.6130726), 'Enfield': (41.9789387, -72.5755109), 'Essex': (41.3617945, -72.4317473), 'Farmington': (41.7198216, -72.8320435), 'Franklin': (41.6089873, -72.1459112), 'Glastonbury': (41.7123218, -72.608146), 'Goshen': (41.8317624, -73.2251145), 'Granby': (41.9539032, -72.7894272), 'Greenwich': (41.0264862, -73.6284598), 'Griswold': (41.6035026, -71.9622443), 'Groton': (41.3501598, -72.0761998), 'Guilford': (41.2889866, -72.6817616), 'Hartford': (41.764582, -72.6908547), 'Harwinton': (41.7712085, -73.05983), 'Killingly': (41.8430634, -71.8795925), 'Killingworth': (41.3581545, -72.5637023), 'Lebanon': (41.6362097, -72.2125789), 'Lisbon': (41.5866851, -72.0207809), 'Litchfield': (41.767249, -73.2543049), 'Madison': (41.2794282, -72.5983151), 'Manchester': (41.7834017, -72.5231973), 'Mansfield': (41.7782147, -72.2131565), 'Meriden': (41.5381535, -72.8070435), 'Middlebury': (41.5278742, -73.1276107), 'Middletown': (41.5623178, -72.6509061), 'Milford': (41.2222218, -73.0570603), 'Monroe': (41.3325962, -73.2073358), 'Montville': (41.4649811, -72.1538184), 'Naugatuck': (41.4860186, -73.0509432), 'New Britain': (41.6612104, -72.7795419), 'New Canaan': (41.146763, -73.4948446), 'New Fairfield': (41.4664832, -73.4856789), 'New Haven': (41.3082138, -72.9250518), 'New London': (41.3556187, -72.0997804), 'Newtown': (41.4134764, -73.3086445), 'North Canaan': (42.0225, -73.2908333), 'North Haven': (41.3909305, -72.859545), 'Norwalk': (41.1175966, -73.4078968), 'Norwich': (41.5243537, -72.0759008), 'Old Lyme': (41.3159315, -72.3289715), 'Old Saybrook': (41.2917652, -72.3761956), 'Orange': (41.2784304, -73.0256609), 'Plainfield': (41.6764876, -71.915073), 'Plainville': (41.6711395, -72.8672429), 'Plymouth': (41.6720318, -73.0528893), 'Portland': (41.5728924, -72.6406905), 'Preston': (41.5268022, -71.982138), 'Putnam': (41.9153094, -71.9092563), 'Rocky Hill': (41.6648216, -72.6392587), 'Salem': (41.491269, -72.2762084), 'Sharon': (41.8792599, -73.4767897), 'Shelton': (41.3164856, -73.0931641), 'Simsbury': (41.8759152, -72.8012211), 'Southbury': (41.4814848, -73.2131693), 'South Windsor': (41.8489872, -72.5717551), 'Stamford': (41.0534302, -73.5387341), 'Stonington': (41.3359327, -71.9059042), 'Stratford': (41.1845415, -73.1331651), 'Suffield': (41.9816944, -72.6506604), 'Thomaston': (41.6739862, -73.073164), 'Thompson': (41.9587089, -71.8625715), 'Tolland': (41.818446, -72.3562252), 'Torrington': (41.8006523, -73.1212214), 'Trumbull': (41.2428742, -73.2006687), 'Vernon': (41.8382921, -72.4663331), 'Washington': (41.6314845, -73.3106731), 'Waterbury': (41.5538091, -73.0438362), 'Waterford': (41.358659, -72.1519367), 'Watertown': (41.6062078, -73.1181658), 'Westbrook': (41.285377, -72.4475874), 'West Hartford': (41.7620447, -72.7420399), 'Hampton': (41.7839873, -72.0547977), 'Wethersfield': (41.7142665, -72.6525922), 'Willington': (41.874428, -72.2598935), 'Wilton': (41.1953739, -73.4378988), 'Winchester': (41.918742, -73.1045003), 'Ashford': (41.8731532, -72.1214653), 'Windham': (41.8208345, -72.0051201), 'Windsor Locks': (41.9281305, -72.643631), 'Wolcott': (41.6023196, -72.9867718), 'Woodbridge': (41.352597, -73.0084385), 'Woodstock': (41.9484307, -71.9739626), 'Lyme': (41.3910989, -72.3511531), 'Colebrook': (41.9895388, -73.0956646), 'Bozrah': (41.5505962, -72.168238), 'Bloomfield': (41.826488, -72.7300945), 'Bridgeport': (41.1670412, -73.2048348), 'Bethany': (41.4217637, -72.9970496), 'Columbia': (41.7020432, -72.3011917), 'Bridgewater': (41.5350949, -73.3662305), 'Kent': (41.7246894, -73.476921), 'Hebron': (41.6578767, -72.3659161), 'Eastford': (41.902068, -72.0799095), 'Cornwall': (41.8437058, -73.3292848), 'Chaplin': (41.7948205, -72.1272989), 'Canaan': (41.9616667, -73.3083333), 'Andover': (41.7373212, -72.37036), 'Chester': (41.4031547, -72.4509204), 'Hamden': (41.3959287, -72.8968716), 'Clinton': (41.2756115, -72.528532), 'East Hampton': (41.5758442, -72.5024804), 'Hartland': (41.996206, -72.9795488), 'Deep River': (41.3856546, -72.4356422), 'Brooklyn': (41.7881541, -71.9497957), 'Ridgefield': (41.2814842, -73.4981792), 'Redding': (41.3025956, -73.3834532), 'Middlefield': (41.5165161, -72.7120793), 'Morris': (41.6842633, -73.1962245), 'New Hartford': (41.8823187, -72.9770488), 'Sherman': (41.5792607, -73.4956795), 'Norfolk': (41.9939828, -73.2020577), 'Scotland': (41.6981999, -72.082083), 'Sprague': (41.6214071, -72.0663666), 'Roxbury': (41.5568282, -73.3088922), 'Sterling': (41.707599, -71.828682), 'Somers': (41.9853742, -72.4461952), 'Newington': (41.6978777, -72.7237063), 'Windsor': (41.8525984, -72.6437022), 'Weston': (41.2021302, -73.3812743), 'Warren': (41.7428733, -73.3487304), 'Woodbury': (41.5445404, -73.2090025), 'Wallingford': (41.4570418, -72.8231552), 'Union': (41.9909296, -72.1572992), 'Ellington': (41.9039863, -72.4698071), 'Canterbury': (41.6984209, -71.9710811), 'Stafford': (41.9851964, -72.2895812), 'Pomfret': (41.8975977, -71.9625736), 'West Haven': (41.2706527, -72.9470471), 'Westport': (41.1414855, -73.3578955), 'Ledyard': (41.4386053, -72.0175193), 'Oxford': (41.4351795, -73.1172769), 'Southington': (41.6005435, -72.8782941), 'New Milford': (41.5770993, -73.4105803), 'Voluntown': (41.5706544, -71.8703497), 'Fairfield': (41.1412078, -73.2637258), 'Durham': (41.4817647, -72.6812059), 'Seymour': (41.3943578, -73.0741697), 'Salisbury': (41.983426, -73.4212318), 'Marlborough': (41.631488, -72.459808), 'Haddam': (41.4773213, -72.5120333), 'Prospect': (41.5023192, -72.9787163), 'North Branford': (41.3275971, -72.7673198), 'North Stonington': (41.4411845, -71.8812698)}
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

        return ({"fact_table":fact_table,
                 "location_dim":location_dim,
                 "sales_dim":sales_dim,
                 "property_dim":property_dim,
                 "datetime_dim":datetime_dim})





trnf = DataTransformation()
trnf.transform()