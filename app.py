import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="MajorFit", layout="centered")

st.sidebar.markdown(
    "<h2 style='color:white;'>Choose a page</h2>",
    unsafe_allow_html=True
)

page = st.sidebar.radio(
    " ",
    ["Home", "Prediction"],
    label_visibility="collapsed"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0F172A, #111827);
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1E1B4B, #312E81);
    border-right: 1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

section[data-testid="stSidebar"] .stRadio label {
    background-color: rgba(255,255,255,0.08);
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
    transition: 0.3s;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    background-color: rgba(255,255,255,0.18);
}

/* Main Cards */

.main-card {
    background: linear-gradient(135deg, #4F46E5, #7C3AED, #9333EA);
    padding: 35px;
    border-radius: 28px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0px 15px 35px rgba(124, 58, 237, 0.35);
}

.main-card h1 {
    font-size: 42px;
    margin-bottom: 12px;
}

.main-card p {
    font-size: 18px;
    color: #F3E8FF;
}

/* Result Cards */

.result-card {
    background: linear-gradient(135deg, #1E293B, #334155);
    padding: 32px;
    border-radius: 24px;
    text-align: center;
    color: white;
    box-shadow: 0px 12px 30px rgba(0,0,0,0.35);
    border: 1px solid rgba(255,255,255,0.12);
    margin-top: 28px;
}

.result-card h3 {
    color: #C4B5FD;
    letter-spacing: 1px;
    font-size: 20px;
}

.result-card h1 {
    font-size: 50px;
    color: #FFFFFF;
}

.result-card p {
    color: #D1D5DB;
    font-size: 17px;
}

</style>
""", unsafe_allow_html=True)

df = pd.read_csv("MajorFit (1).csv")
df.columns = df.columns.str.strip()

X = df.drop("target", axis=1)
y = df["target"]

model = RandomForestClassifier()
model.fit(X, y)

if page == "Home":

    st.markdown("""
    <div class="main-card">
        <h1>MajorFit Prediction System</h1>
        <p>Predict whether a student's personality matches their major</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="result-card">
        <h3>About MajorFit</h3>
        <p>
        MajorFit is a simple machine learning web application that helps predict
        whether a student's personality matches their academic major.
        </p>
        <p>
        Answer the questions in the Prediction page to get the result.
        </p>
    </div>
    """, unsafe_allow_html=True)

if page == "Prediction":

    st.markdown("""
    <div class="main-card">
        <h1>Prediction Page</h1>
        <p>Answer the questions below to get your prediction result</p>
    </div>
    """, unsafe_allow_html=True)

    field_of_study = st.selectbox(
        "What is your field of study?",
        ["Health", "Technology", "Business/Management", "Humanities", "Other"]
    )

    academic_year = st.selectbox(
        "What is your academic year?",
        ["First year", "Second year", "Third year", "Fourth year or above"]
    )

    personality = st.selectbox(
        "How would you describe yourself?",
        ["Organized and structured", "Creative and spontaneous", "Analytical and logical", "Social and collaborative"]
    )

    work_preference = st.selectbox(
        "Do you prefer working:",
        ["Individually", "In a team", "Both equally"]
    )

    problem_solving = st.selectbox(
        "How do you usually deal with problems?",
        ["Analyze and solve calmly", "Ask for help", "Feel stressed quickly", "Avoid the problem"]
    )

    learning_method = st.selectbox(
        "What is your preferred learning method?",
        ["Reading and understanding", "Memorization and repetition", "Practical/application-based learning", "Watching videos"]
    )

    major_interest = st.selectbox(
        "Do you find your major interesting?",
        ["Always", "Often", "Sometimes", "Rarely"]
    )

    academic_performance = st.selectbox(
        "How do you rate your performance in your major?",
        ["Excellent", "Very good", "Good", "Weak"]
    )

    major_choice = st.selectbox(
        "Did you choose your major by your own choice?",
        ["Yes", "Somewhat", "No"]
    )

    future_field = st.selectbox(
        "Do you see yourself working in this field in the future?",
        ["Yes", "Maybe", "No"]
    )

    field_of_study_map = {
        "Health": 0,
        "Technology": 1,
        "Business/Management": 2,
        "Humanities": 3,
        "Other": 4
    }

    academic_year_map = {
        "First year": 0,
        "Second year": 1,
        "Third year": 2,
        "Fourth year or above": 3
    }

    personality_map = {
        "Organized and structured": 0,
        "Creative and spontaneous": 1,
        "Analytical and logical": 2,
        "Social and collaborative": 3
    }

    work_preference_map = {
        "Individually": 0,
        "In a team": 1,
        "Both equally": 2
    }

    problem_solving_map = {
        "Analyze and solve calmly": 0,
        "Ask for help": 1,
        "Feel stressed quickly": 2,
        "Avoid the problem": 3
    }

    learning_method_map = {
        "Reading and understanding": 0,
        "Memorization and repetition": 1,
        "Practical/application-based learning": 2,
        "Watching videos": 3
    }

    major_interest_map = {
        "Always": 0,
        "Often": 1,
        "Sometimes": 2,
        "Rarely": 3
    }

    academic_performance_map = {
        "Excellent": 0,
        "Very good": 1,
        "Good": 2,
        "Weak": 3
    }

    major_choice_map = {
        "Yes": 0,
        "Somewhat": 1,
        "No": 2
    }

    future_field_map = {
        "Yes": 0,
        "Maybe": 1,
        "No": 2
    }

    result_map = {
        0: "Suitable",
        1: "Neutral",
        2: "Not Suitable"
    }

    if st.button("Predict"):

        input_data = pd.DataFrame([[
            field_of_study_map[field_of_study],
            academic_year_map[academic_year],
            personality_map[personality],
            work_preference_map[work_preference],
            problem_solving_map[problem_solving],
            learning_method_map[learning_method],
            major_interest_map[major_interest],
            academic_performance_map[academic_performance],
            major_choice_map[major_choice],
            future_field_map[future_field]
        ]], columns=X.columns)

        prediction = model.predict(input_data)[0]
        result = result_map[prediction]

        st.markdown(f"""
        <div class="result-card">
            <h3>Prediction Result</h3>
            <h1>{result}</h1>
            <p>
            Based on the student's responses, the model predicts the compatibility
            level between personality and major.
            </p>
        </div>
        """, unsafe_allow_html=True)