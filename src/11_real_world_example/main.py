# Tasks 1: Retrieve a list of all device that have been active over the last 30 days by customer

from datetime import datetime, timedelta
import json
import config
from falconpy import Hosts

# initialize Hosts service collection
falcon = Hosts(client_id= config.FALCON_CLIENT_ID,
              client_secret = config.FALCON_CLIENT_SECRET)

# date 30 days ago from today 
last_30_days = (datetime.today() - timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")

# String w/ date for File Naming: <old date>--<today>
hosts_from_dates = (f'{(datetime.today() - timedelta(days=30)).strftime("%Y_%m_%d")}--{datetime.today().strftime("%Y_%m_%d_T%H-%M-%SZ")}')

# Retrieve a list of active hosts in the last 30 days 
hosts_search_result = falcon.query_devices_by_filter(filter=f"last_seen:>='{last_30_days}'",limit=5000)

# Isolate the device_ids into a list
host_list = hosts_search_result['body']['resources']

# Pull device details on each host_list device_id
dev_details = falcon.get_device_details(ids=host_list)

# Organize Device IDs with CIDs into dictionary
resources = dev_details['body']['resources']
cid_dict = {}
for i in range(len(resources)):
    cid = resources[i]['cid']
    device = resources[i]['device_id']
    if cid not in cid_dict.keys():
        cid_dict[cid] = []
    if device not in cid_dict[cid]:
        cid_dict[cid].append(device)

# Write the cid_dict to a file in json format
cid_device = open(f'CID_DEV_{hosts_from_dates}.json','w')
cid_device.write(json.dumps(cid_dict,indent=2))
cid_device.close

# There is now a file with the format 'CID_DEV_<old date>--<today's date>.json'