import urllib.request
import pandas as pd
import os.path

def download(stationid, year):
    
    
    print("Data for station with id {} for year {}".format(stationid, year))
    
    
    File_name = "{}_{}_t.csv".format(stationid, year)  #file name for the CSV
    url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="+str(stationid)+"&Year="+str(year)+"&Month=8&Day=1&timeframe=2&submit=Download+Data"

    #downloading the file from the URL, and Saving into CSV file
    if(os.path.exists('../Data_csv/'+File_name)): #download only if the file not Exists
        print("File Exists")
    else:
        print("Downloading in progress ...")
        try:
            urllib.request.urlretrieve(url, '../Data_csv/'+File_name)
        except FileNotFoundError as fnfe:
            print("File not found..")
            print("%s" % fnfe)
            return ""
        except Exception as e:
            print("%s" % e)
            return ""
            
        print("Download Completed...")
        
    
    #extracthing data from CSV file
    data = pd.read_csv('../Data_csv/'+File_name, skiprows=25, sep=",", encoding="ISO-8859-1")
    
    #selecting the necessary columns
    columns = [0,1,2,3,5,7,9]
    df = data[columns]
    
    #Re naming the colums
    data_frame = df.rename(columns={'Max Temp (°C)':'Max_Temp', 'Min Temp (°C)': 'Min_Temp', 'Mean Temp (°C)': 'Mean_Temp'})
    
    #getting cici name from the CSV
    Citi_name = pd.read_csv('../Data_csv/'+File_name, nrows=1)
    return Citi_name, data_frame
    
print("Test successful") 
