import os 

folders = os.listdir("data") ## to find folder where it is located
print(folders)
print(os.getcwd()) ## to see location
os.chdir("/Users")
print(os.getcwd())

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))