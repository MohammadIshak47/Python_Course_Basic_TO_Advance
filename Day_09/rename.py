import os 

for i in range(0,100):
    # os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}") ## to rename folder name
    os.rename(f"data/Tutorial{i+1}", f"data/Tutorial {i+1}") ## to give space between folder word

    