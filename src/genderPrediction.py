import pandas as pd
from os import getcwd, listdir
from gender_predictor import GenderPredictor

# Get the Student Data
data_path = getcwd() + "/data"
listdir(data_path)

df = pd.read_csv(f"{data_path}/{listdir(data_path)[0]}")

# Instantiate the Class
gp = GenderPredictor()

# Train the Model
gp.train_and_test()

# Get List of Students' First Names
student_names = [name.split(" ")[0] for name in df['Student Name'].tolist()]

# Get Predictions
gender_preds = [gp.classify(name) for name in student_names]


# Add Gender Column to the Data Frame
df['Gender'] = gender_preds

# Save New Data
df.to_csv(f"{data_path}/{listdir(data_path)[0]}", index=False)

df['Gender']
