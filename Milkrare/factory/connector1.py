import pandas as pd
import os


def milking(request_json):
    try:
        #df = pd.read_csv(r"C:\Users\satishkumar.s\Desktop\Milkrare\factory\Haptikdata.csv",encoding='latin-1')
        #df = pd.read_csv('Haptik_API-main/Milkrare/factory/Haptikdata.csv')
        df = pd.read_csv(r"https://github.com/wazsee/Haptik_API-final/blob/main/Haptik_API-main%20(3)/Haptik_API-main/Milkrare/factory/Haptik_finaldata.csv?raw=true",encoding= 'unicode_escape')
        #df = pd.read_csv(url)

        #df = pd.read_csv('Milkrare/factory/Haptikdata.csv')
        #df = pd.read_csv('https://github.com/wazsee/Haptik_API/blob/8ae1f0c3d8313c965d3de47b6b71f5bae53a0988/Milkrare/factory/Haptikdata.csv')
        print("df")
        

        #request_json['Milk1_Dry2'] = 1 if request_json['Milk1_Dry2'] == "milk" else 2

        response_values = df.loc[
            (df['MobileNumber']==request_json['MobileNumber'])
            ]
        print(df.head())

        
        response = {}
        response['FarmerName'] = response_values['FarmerName'].values[0]
        response['RegionName'] = response_values['RegionName'].values[0]
        response['PlantCode'] = int(response_values['PlantCode'].values[0])
        response['PlantName'] = response_values['PlantName'].values[0] 
        response['MCCCode'] = int(response_values['MCCCode'].values[0])
        response['MCCName'] =response_values['MCCName'].values[0]
        
        
        

        return response
    except Exception as e:
        return str(e)
    
