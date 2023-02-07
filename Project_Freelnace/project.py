from sharepoint import SharePoint

# set file name
file_name = 'test_sharepoint.csv'

# set the folder name
folder_name = 'test-folder'

# get file
file  = SharePoint().get_file(file_name, folder_name)

# save file
with open(file_name, 'wb') as f:
    f.write(file)
    f.close()