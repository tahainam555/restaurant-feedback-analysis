import pandas as pd
import matplotlib.pyplot as plt

# Load data
df1 = pd.read_csv("my_restaurant_reviews.csv")
df2 = pd.read_csv("competitor_restaurant_reviews.csv")

df1["Restaurant"] = "Your Restaurant"
df2["Restaurant"] = "Competitor Restaurant"

# Combine data
combined = pd.concat([df1, df2], ignore_index=True)

# Function to preprocess DINING TIME and convert to datetime
def preprocess_dining_time(dining_time):
    if "Dined on" in dining_time:  # For format "Dined on December 1, 2024"
        return pd.to_datetime(dining_time.replace("Dined on ", ""), format="%B %d, %Y")
    else:  # For format "2024-12-10"
        return pd.to_datetime(dining_time, format="%Y-%m-%d")

# Apply the preprocessing function to the 'DINING TIME' column
combined["DINING TIME"] = combined["DINING TIME"].apply(preprocess_dining_time)

# Plot using Matplotlib
plt.figure(figsize=(10, 6))

# Plot for Your Restaurant
your_restaurant_data = combined[combined["Restaurant"] == "Your Restaurant"]
plt.plot(your_restaurant_data["DINING TIME"], your_restaurant_data["RATING"], label="Your Restaurant", color='blue', marker='o')

# Plot for Competitor Restaurant
competitor_data = combined[combined["Restaurant"] == "Competitor Restaurant"]
plt.plot(competitor_data["DINING TIME"], competitor_data["RATING"], label="Competitor Restaurant", color='red', marker='x')

# Customize the plot
plt.title("Ratings Over Time")
plt.xlabel("Date")
plt.ylabel("Rating")
plt.legend()
plt.grid(True)

# Show the plot
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout to make sure everything fits
plt.show()
