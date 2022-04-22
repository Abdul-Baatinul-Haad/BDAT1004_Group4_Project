from pymongo import MongoClient
import requests
import pandas as pd


client =MongoClient("mongodb+srv://Abdul-Batin:abdul2001@bball-db.amh5g.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database('Bball_Teams')
records = db['Teams']

r= requests.get('https://www.balldontlie.io/api/v1/teams/1')
data = r.json()
# if r.status_code==200:
    
# #     #print (data)
#     records.insert_one(data)
# else:
#     exit()

team_dets = records.find()
# for team in team_dets:
#     print (team)

teams_df = pd.DataFrame(team_dets)
#print(teams_df)
teams_df.drop(["_id"], axis=1, inplace=True)
# cols = teams_df.columns.values.tolist()
# cols = cols.to_dict()
# print(cols)
division_count = teams_df.groupby('division')['name'].count()

division_count = division_count.to_dict()


# division_count = np.array(list(division_count.items()))
# print(division_count)
