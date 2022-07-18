import csv
import pandas as pd


with open('datasets/COCO_Text.json') as input, open('datasets/COCO_Text.json', 'w', newline='') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)

df = pd.read_csv('datasets/objects.json', header=None)
df.rename(columns={0: 'f1', 1: 'f2', 2: 'f3', 3: 'f4', 4: 'char_code'}, inplace=True)
df.to_csv('datasets/objects.json', index=False)  # save to new csv file