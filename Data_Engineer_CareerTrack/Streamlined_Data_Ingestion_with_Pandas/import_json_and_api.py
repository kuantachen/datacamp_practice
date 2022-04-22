## JSON (Javascipt Object Notation)
# Common web data format, not tabular, data organized into collections of objects, nested JSON

# Load pandas as pd
import pandas as pd

# Load the daily report to a dataframe
pop_in_shelters = pd.read_json('dhs_daily_report.json')

# View summary stats about pop_in_shelters
print(pop_in_shelters.describe())

# =====================================================

try:
    # Load the JSON without keyword arguments
    df = pd.read_json('dhs_report_reformatted.json')
    
    # Plot total population in shelters over time
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census", 
            y="total_individuals_in_shelter")
    plt.show()
    
except ValueError:
    print("pandas could not parse the JSON.")


try:
    # Load the JSON with orient specified
    df = pd.read_json("dhs_report_reformatted.json",
                      orient='split')
    
    # Plot total population in shelters over time
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census", 
            y="total_individuals_in_shelter")
    plt.show()
    
except ValueError:
    print("pandas could not parse the JSON.")

# =====================================================
## API (Application Programing Interfaces)

# Defines how a application communicates with other programs
# Way to get data from an application without knowing databases details

## Requests
# Send and get data from websites
# Not tied to a particular API
# requests.get() to get data from URL

## requests.get()
# requests.get(url_string) to get data from a URL
# params keyword: takes a dictionary of parameters and values to customize API request
# headers keyword: takes a dictionary, can be used to provide user authentication to API

## Result: a response object, containing data and metadata
# response.json() will return just the JSON data

## response.json() and pandas
# response.json() returns a dictionary
# read_json() expects strings, not dictionaries
# Load the response JSON to a dataframe with pd.DataFrame(), read_json() will give an error!

# =====================================================

api_url = "https://api.yelp.com/v3/businesses/search"

# Get data about NYC cafes from the Yelp API
response = requests.get(api_url, 
                headers=headers, 
                params=params)

# Extract JSON data from the response
data = response.json()

# Load data to a dataframe
cafes = pd.DataFrame(data["businesses"])

# View the data's dtypes
print(cafes.dtypes)

# =====================================================

# Create dictionary to query API for cafes in NYC
parameters = {"term": "cafe",
          	  "location": "NYC"}

# Query the Yelp API with headers and params set
response = requests.get(api_url,
                params=parameters,
                headers=headers)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a dataframe and print head
cafes = pd.DataFrame(data["businesses"])
print(cafes.head())

# =====================================================

## Set request headers

# Many APIs require users provide an API key, 
# obtained by registering for the service. 
# Keys typically are passed in the request header, rather than as parameters.

headers = {"Authorization": "Bearer {}".format(api_key)}

# Query the Yelp API with headers and params set
response = requests.get(api_url, headers=headers, params=params)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a dataframe and print names
cafes = pd.DataFrame(data["businesses"])
print(cafes.name)

# =====================================================

# pandas.io.json submodule has tools for reading and writing JSON, need its own import statement

# json_normalize(): takes a dictionary/list of dictionaries (like pd.DataFrame() does)
# returns a flattened dataframe
# default flattened column name pattern: attribute.nestedattribute
# choose a different separator with the sep argument

# Load json_normalize()
from pandas.io.json import json_normalize

# Isolate the JSON data from the API response
data = response.json()

# Flatten business data into a dataframe, replace separator
cafes = json_normalize(data["businesses"],
             sep='_')

# View data
print(cafes.head())

# =====================================================

# Flatten businesses records and set underscore separators
# Specify record path to get categories data
# Load other business attributes and set meta prefix
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories",
                    		meta=["name", 
                                  "alias",  
                                  "rating",
                          		  ["coordinates", "latitude"], 
                          		  ["coordinates", "longitude"]],
                    		meta_prefix="biz_")

# View the data
print(flat_cafes.head())

# =====================================================

# Add an offset parameter to get cafes 51-100
params = {"term": "cafe", 
          "location": "NYC",
          "sort_by": "rating", 
          "limit": 50,
          "offset": 50}

result = requests.get(api_url, headers=headers, params=params)
next_50_cafes = json_normalize(result.json()["businesses"])

# Append the results, setting ignore_index to renumber rows
cafes = top_50_cafes.append(next_50_cafes, ignore_index=True)

# Print shape of cafes
print(cafes.shape)

# =====================================================

# Merge crosswalk into cafes on their zip code fields
cafes_with_pumas = cafes.merge(crosswalk, left_on='location_zip_code', right_on='zipcode')

# Merge pop_data into cafes_with_pumas on puma field
cafes_with_pop = cafes_with_pumas.merge(pop_data, left_on='puma', right_on='puma')

# View the data
print(cafes_with_pop.head())

# =====================================================

# =====================================================

# =====================================================

# =====================================================

# =====================================================