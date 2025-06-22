import streamlit as st
import pandas as pd
from utils import get_people_in_space, get_iss_location

def main():
    st.title("List of The Current Astronauts in Space at this Moment")
    st.markdown("This application displays the total number of people and their names, that are currently in space in the ISS.")

    people = get_people_in_space()
    st.write(f"Total number of people in space: {len(people)}")
    st.write("Names of people in space:")
    for person in people:
        st.write(f"- {person['name']}")

    iss_location = get_iss_location()
    if iss_location:
        st.markdown("### Current Location of the International Space Station (ISS)")
        st.markdown("Below is a map showing the real-time position of the ISS as it orbits the Earth.")
        st.write(f"Latitude: {iss_location['latitude']}, Longitude: {iss_location['longitude']}")
        #DataFrame for st.map
        iss_df = pd.DataFrame(
    [[float(iss_location['latitude']), float(iss_location['longitude'])]],
    columns=['lat', 'lon']
)
        st.map(iss_df)

if __name__ == "__main__":
    main()