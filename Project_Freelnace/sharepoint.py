from shareplum import Site, Office365
from shareplum.site import Version

import json, os


# read json file
with open('config.json') as config_file:
    config = json.load(config_file)   
    config = config['share_point']

USERNAME = config['user']
PASSWORD = config['password']
SHAREPOINT_URL = config['url']
SHAREPOINT_SITE = config['site']
SHAREPOINT_DOC = config['doc_library']


def download_file_sharepoint(self,file_name,sub_folder_name):
    login = Office365(SHAREPOINT_URL, username=USERNAME, password=PASSWORD).GetCookies()

    auth_site = Site(SHAREPOINT_SITE, version=Version.v365, authcookie=login)
        
    sharepoint_dir = '\\'.join([SHAREPOINT_DOC, sub_folder_name])
        
    folder = auth_site.Folder(sharepoint_dir) 

    file = folder.get_file(file_name)

    with open(file_name, 'wb') as f:
        f.write(file)
        f.close()
