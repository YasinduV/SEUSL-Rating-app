import streamlit as st
import pandas as pd

# Set the title and page configuration
st.title("South Eastern University of Sri Lanka")
st.subheader("Techno Exhibition 2023")
#st.set_page_config(layout="centered")

# Create a slider widget to select the rating
st. write("We value your feedback! Please take a moment to rate our stall. Your input helps us improve and provide the best experience for our visitors. Thank you for your participation!")
rating = st.slider("Rate our stall", 1, 5)

# Create a button to submit the rating
submit_button = st.button("Submit Rating")

# Initialize a Pandas DataFrame to store the ratings
#ratings_df = pd.DataFrame(columns=["Rating"])

# Check if the CSV file exists; if not, create it
csv_file = "exhibition_ratings.csv"
try:
    existing_ratings = pd.read_csv(csv_file)
    ratings_df = existing_ratings
except FileNotFoundError:
    ratings_df = pd.DataFrame(columns=["Rating"])
    ratings_df.to_csv(csv_file, index=False)

# Check if the button is clicked and update the CSV file
if submit_button:
    new_rating = {"Rating":rating}
    new_rating= {k:[v] for k,v in new_rating.items()}
    new_rating = pd.DataFrame(new_rating)
    ratings_df1 = pd.concat([ratings_df,new_rating] , ignore_index = True)
    ratings_df1.to_csv(csv_file, index=False)

    st.write(f"You have rated the exhibition stall: {rating} out of 5")

# Calculate and display the average rating
    if not ratings_df1.empty:
        average_rating = ratings_df1["Rating"].mean()
        #st.write(f"Average Rating: {average_rating:.2f}")
        st.write("Average Rating: ", "⭐" * round(average_rating),f"{average_rating:.2f}")
