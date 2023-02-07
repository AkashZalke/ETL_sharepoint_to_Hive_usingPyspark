from shareplum import Site, Office365
from shareplum.site import Version

import json, os

# Give root directory of the file (config)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
config_path = '\\'.join([ROOT_DIR, 'config.json'])

# read json file
with open(config_path) as config_file:
    config = json.load(config_file)   
    config = config['share_point']

USERNAME = config['user']
PASSWORD = config['password']
SHAREPOINT_URL = config['url']
SHAREPOINT_SITE = config['site']
SHAREPOINT_DOC = config['doc_library']

class SharePoint:
    def auth(self):
        print(Version , "HEREPARPAMF")
        self.authcookie = Office365(SHAREPOINT_URL, username=USERNAME, password=PASSWORD).GetCookies()
        self.site = Site(SHAREPOINT_SITE, version=Version.v365, authcookie=self.authcookie)
        return self.site

    
    def connect_folder(self, folder_name):
        
        # SHAREPOINT_DOC = config_json['doc_library'] + project.py(folder.name)

        self.auth_site = self.auth()

        
        self.folder = self.auth_site.Folder(self.sharepoint_dir)

        return self.folder

    def download_file(self, file_name, folder_name):
        self._folder = self.connect_folder(folder_name)
        return self._folder.get_file(file_name)

    def get_file(self,file_name,sub_folder_name):
    
        login = Office365(SHAREPOINT_URL, username=USERNAME, password=PASSWORD).GetCookies()
        
        auth_site = Site(SHAREPOINT_SITE, version=Version.v365, authcookie=login)
        
        sharepoint_dir = '\\'.join([SHAREPOINT_DOC, sub_folder_name])
        
        folder = auth_site.Folder(sharepoint_dir) 

        return folder.get_file(file_name)