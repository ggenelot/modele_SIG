import json
import requests
from pathlib import Path

#---INSERT CODE TO COLLECT ITEM IDS HERE----

# Or use this test set of ids that have small files (To use, delete the '#' in the next line)
item_ids = [17714843,153788]

#Set the base URL
BASE_URL = 'https://api.figshare.com/v2'

file_info = [] #a blank list to hold all the file metadata

for i in item_ids:
    r = requests.get(BASE_URL + '/articles/' + str(i) + '/files')
    file_metadata = json.loads(r.text)
    for j in file_metadata: #add the item id to each file record- this is used later to name a folder to save the file to
        j['item_id'] = i
        file_info.append(j) #Add the file metadata to the list

#Download each file to a subfolder named for the article id and save with the file name
for k in file_info:
    response = requests.get(BASE_URL + '/file/download/' + str(k['id']), headers=api_call_headers)
    Path(str(k['item_id'])).mkdir(exist_ok=True)
    open(str(k['item_id']) + '/' + k['name'], 'wb').write(response.content)
    
print('All done. If using Colab you will find the files in the little folder icon to the left.')