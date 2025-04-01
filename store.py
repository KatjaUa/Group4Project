import pandas as pd

# Load the dataset
file_path = "Health_Sleep_Statistics.csv"  # Update with actual path
df = pd.read_csv(file_path)

# Convert Bedtime & Wake-up Time to datetime
for col in ["Bedtime", "Wake-up Time"]:
    df[col] = pd.to_datetime(df[col], format='%H:%M').dt.time

# Normalize categorical values
df["Physical Activity Level"] = df["Physical Activity Level"].str.lower()
df["Dietary Habits"] = df["Dietary Habits"].str.lower()

def analyze_sleep():
    print("Basic Statistics:\n", df.describe())
    print("\nMissing Values:\n", df.isnull().sum())
    
    # Average Sleep Quality per Activity Level
    sleep_by_activity = df.groupby("Physical Activity Level")["Sleep Quality"].mean()
    print("\nAverage Sleep Quality by Activity Level:\n", sleep_by_activity)
    
    # Count of Sleep Disorders
    sleep_disorder_counts = df["Sleep Disorders"].value_counts()
    print("\nSleep Disorder Counts:\n", sleep_disorder_counts)
    
    # Average Calories Burned per Dietary Habit
    avg_calories = df.groupby("Dietary Habits")["Calories Burned"].mean()
    print("\nAverage Calories Burned by Dietary Habit:\n", avg_calories)

if __name__ == "__main__":
    analyze_sleep()
