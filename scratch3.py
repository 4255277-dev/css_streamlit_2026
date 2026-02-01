import streamlit as st
import plotly.express as px

# Set page title
st.set_page_config(page_title="Researcher Profile", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")

menu_item_1 = "Profile"
menu_item_2 = "Education"
menu_item_3 = "Work Experience"
menu_item_4 = "Skills"
menu_item_5 = "Hobbies"
menu_item_6 = "Contact"

menu_sidebar_list = [menu_item_1, menu_item_2, menu_item_3, menu_item_4, menu_item_5, menu_item_6]

menu = st.sidebar.radio(
    "Go to:",
    menu_sidebar_list,
)

# Sections based on menu selection
if menu == menu_item_1:
    st.title(f"{menu_item_1}")
    st.sidebar.header(f"{menu_item_1} Options")

    # Collect basic information
    name = "Moegamat Anees Petersen"
    level = "Master of Science (MSc)"
    field = "Material Science / Renewable Energy"
    institution = "University of the Western Cape (UWC)"

    message = "Moegamat Anees Petersen has striven through tough times and has always kept a smile on his dial. He has been fortunate enough however to complete a Standard Educatory Comprehension having gone through the Public Schooling System, firstly through Cypress Primary School from years 2010 through 2016, secondly through the Belgravia Secondary School from years 2017 through 2021, and currently Studying as a First Year at the University of the Western Cape. He has working experience of the voluntary sort for both Athlone City Parks Depot and Abdurahman Day Hospital, both for the year 2020. He entered the University with the wrong degree choice but believes that he will change his choice and career."

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Level:** {level}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")

    image_url_link = "https://as2.ftcdn.net/v2/jpg/07/54/47/57/1000_F_754475766_IFsiMAfL3W2EAdyeBubbe7FZNEAb6JKB.jpg"
    image_caption = "A CFD Simulation Image"
    
    st.image(
    image_url_link,
    caption=image_caption
    )

    msg = st.write(f"**Message:** {message}")

elif menu == menu_item_2:
    st.title(f"{menu_item_2}")
    st.sidebar.header(f"{menu_item_2} Options")

    primary_school_name = "Cypress Primary School"
    primary_school_start_year = 2010
    primary_school_end_year = 2016

    primary_achieve_1 = "First School Leaving Certificate (FSLC)"
    primary_achieve_2 = "Top Achiever Awards (Grades 2,4,5,6,7)"
    primary_achieve_3 = "Junior Biologist Course (Grade 6)"

    high_school_name = "Belgravia High School"
    high_school_start_year = 2017
    high_school_end_year = 2021

    high_achieve_1 = "National Senior Certificate (NSC)"
    high_achieve_2 = "Top 10 Positions (Grades 8 - 12)"
    high_achieve_3 = "Top 3 Position (Grade 12)"

    uni_school_name = "University of the Western Cape"
    uni_school_start_year = 2022
    uni_school_end_year = 2026

    uni_achieve_1 = "BSc, Hons and MSc in Physics"
    uni_achieve_2 = "Deans Merit List Award for APM 123 module"
    uni_achieve_3 = "BSc Cum Laude, Hons ~80% w.a. (effective Magna Cum Laude), MSc pursuing"

    st.header(f"**Primary School:** {primary_school_name}")
    st.write(f"({primary_school_start_year} - {primary_school_end_year})")
    st.write(f"\t * {primary_achieve_1} \n \t * {primary_achieve_2} \n \t * {primary_achieve_3}")

    st.header(f"**Secondary School:** {high_school_name}")
    st.write(f"({high_school_start_year} - {high_school_end_year})")
    st.write(f"\t * {high_achieve_1} \n \t * {high_achieve_2} \n \t * {high_achieve_3}")

    st.header(f"**Tertiary School:** {uni_school_name}")
    st.write(f"({uni_school_start_year} - {uni_school_end_year})")
    st.write(f"\t * {uni_achieve_1} \n \t * {uni_achieve_2} \n \t * {uni_achieve_3}")

elif menu == menu_item_3:
    st.title(f"{menu_item_3}")
    st.sidebar.header(f"{menu_item_3} Options")

    experience_name_1 = "Abdurahman Day Hospital Volunteer"
    experience_start_year_1 = 2020
    experience_end_year_1 = 2020

    experience_atr_1_1 = "Filing of patients folders into the Filing Cabinets"
    experience_atr_1_2 = "Logging of patients folders into the Database"

    experience_name_2 = "Athlone City Parks Depot Volunteer"
    experience_start_year_2 = 2020
    experience_end_year_2 = 2020

    experience_atr_2_1 = "Cleaning of dirt-infested areas of the Nantes Park"
    experience_atr_2_2 = "Observation for uncompliant Nantes Park Visitors"

    experience_name_3 = "Math Tuition Tutor"
    experience_start_year_3 = 2021
    experience_end_year_3 = 2025

    experience_atr_3_1 = "Wednesday tuition from 17:00 – 19:00 (Grades 8 - 12)"
    experience_atr_3_2 = "Saturday Tuition from 09:00 – 13:00 (Grades 3 - 12)"

    experience_name_4 = "PHY 151 Tutor"
    experience_start_year_4 = 2025
    experience_end_year_4 = 2025

    experience_atr_4_1 = "Preparation of Memo for Weekly Group Task Assignments and/or Sessions"
    experience_atr_4_2 = "Assisting Student during Weekly Group Task Sessions and Marking Group Task Assignments"

    st.header(f"**{experience_name_1}**")
    st.write(f"({experience_start_year_1} - {experience_end_year_1})")
    st.write(f"\t * {experience_atr_1_1} \n \t * {experience_atr_1_2}")
    
    st.header(f"**{experience_name_2}**")
    st.write(f"({experience_start_year_2} - {experience_end_year_2})")
    st.write(f"\t * {experience_atr_2_1} \n \t * {experience_atr_2_2}")
    
    st.header(f"**{experience_name_3}**")
    st.write(f"({experience_start_year_3} - {experience_end_year_3})")
    st.write(f"\t * {experience_atr_3_1} \n \t * {experience_atr_3_2}")

    st.header(f"**{experience_name_4}**")
    st.write(f"({experience_start_year_4} - {experience_end_year_4})")
    st.write(f"\t * {experience_atr_4_1} \n \t * {experience_atr_4_2}")

# elif menu == menu_item_4:
#     st.title(f"{menu_item_4}")
#     st.sidebar.header(f"{menu_item_4} Options")

#     label_1 = "Leadership"
#     label_2 = "Communication"
#     label_3 = "Professionalism"
#     label_4 = "Teamwork"
#     label_5 = "Critical Thinking"

#     size_1 = 20
#     size_2 = 21
#     size_3 = 18
#     size_4 = 22
#     size_5 = 19

#     explode_1 = 0
#     explode_2 = 0
#     explode_3 = 0
#     explode_4 = 0
#     explode_5 = 0

#     labels = [label_1, label_2, label_3, label_4, label_5]
#     sizes = [size_1, size_2, size_3, size_4, size_5]
#     explode = [explode_1, explode_2, explode_3, explode_4, explode_5]

#     fig_1, ax_1 = plt.subplots()
#     ax_1.pie(sizes, explode=explode, labels=labels, autopct = '%1.1f%%', shadow=True, startangle=90)
#     ax_1.axis('equal')

#     st.pyplot(fig_1)

elif menu == menu_item_4:
    st.title(f"{menu_item_4}")
    st.sidebar.header(f"{menu_item_4} Options")

    labels = [
        "Leadership",
        "Communication",
        "Professionalism",
        "Teamwork",
        "Critical Thinking"
    ]

    sizes = [20, 21, 18, 22, 19]

    fig_1 = px.pie(
        names=labels,
        values=sizes,
        hole=0,                     # set to >0 for donut chart
    )

    fig_1.update_traces(
        textinfo="percent+label",
        pull=[0, 0, 0, 0, 0]         # equivalent to explode
    )

    fig_1.update_layout(
        showlegend=True
    )

    st.plotly_chart(fig_1, use_container_width=True)

elif menu ==  menu_item_5:
    st.title(f"{menu_item_5}")
    st.sidebar.header(f"{menu_item_5} Options")

    hobby_1 = "Playing Chess"
    hobby_2 = "Reading Books"
    hobby_3 = "Listening to Music"
    hobby_4 = "Learning Languages"

    st.write(f"* {hobby_1}")
    st.write(f"* {hobby_2}")
    st.write(f"* {hobby_3}")
    st.write(f"* {hobby_4}")

elif menu == menu_item_6:
    st.title(f"{menu_item_6}")
    st.sidebar.header(f"{menu_item_6} Options")

    phone_number = "079-669-1963"
    personal_email = "anees.petersen333@gmail.com"
    university_email = "4255277@myuwc.ac.za"

    st.write(f"**Phone:** {phone_number}")
    st.write(f"**Personal Email:** {personal_email}")
    st.write(f"**University Email** {university_email}")

else:
    st.write("An invalid menu_item has been selected!")

















