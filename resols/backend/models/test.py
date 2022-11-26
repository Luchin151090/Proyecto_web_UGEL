import os.path
directory = 'D:/Luchin/myweb/resols/backend/archivos/'
filename = "file.txt"
file_path = os.path.join(directory, filename)
if not os.path.isdir(directory):
    os.mkdir(directory)
