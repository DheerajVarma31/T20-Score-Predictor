import streamlit as st
import pickle
import pandas as pd

# Load the trained pipeline
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Team and city options
teams = [
    'Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa', 'England',
    'West Indies', 'Afghanistan', 'Pakistan', 'Sri Lanka'
]

cities = [
    'Colombo', 'Mirpur', 'Johannesburg', 'Dubai', 'Auckland', 'Cape Town', 'London',
    'Pallekele', 'Barbados', 'Sydney', 'Melbourne', 'Durban', 'St Lucia', 'Wellington',
    'Lauderhill', 'Hamilton', 'Centurion', 'Manchester', 'Abu Dhabi', 'Mumbai',
    'Nottingham', 'Southampton', 'Mount Maunganui', 'Chittagong', 'Kolkata', 'Lahore',
    'Delhi', 'Nagpur', 'Chandigarh', 'Adelaide', 'Bangalore', 'St Kitts', 'Cardiff',
    'Christchurch', 'Trinidad'
]

# Title
st.title('🏏 T20 Cricket Score Predictor')

# Team selection
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

# City selection
city = st.selectbox('Select Venue City', sorted(cities))

# Match progress input
col3, col4, col5 = st.columns(3)
with col3:
    current_score = st.number_input('Current Score', min_value=0, step=1)
with col4:
    overs = st.number_input('Overs Completed (must be > 5)', min_value=5.1, max_value=20.0, step=0.1)
with col5:
    wickets = st.number_input('Wickets Fallen', min_value=0, max_value=10, step=1)

# Recent performance
last_five = st.number_input('Runs Scored in Last 5 Overs', min_value=0, step=1)

# Predict Button
if st.button('🎯 Predict Final Score'):
    try:
        balls_left = int(120 - (overs * 6))
        wickets_left = 10 - wickets
        crr = current_score / overs

        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [city],
            'current_score': [current_score],
            'balls_left': [balls_left],
            'wickets_left': [wickets_left],
            'crr': [crr],
            'last_five': [last_five]
        })

        # Prediction
        predicted_score = pipe.predict(input_df)[0]
        st.header(f"🏆 Predicted Final Score: {int(predicted_score)}")

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
