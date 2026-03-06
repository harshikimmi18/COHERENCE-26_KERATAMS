import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Clinical Trial Eligibility Engine", layout="wide")

# Sidebar
st.sidebar.title("Clinical Trial AI System")
menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Patient Analysis", "Trial Recommendations", "Explainable AI", "Reports"]
)

# -------------------- DASHBOARD --------------------

if menu == "Dashboard":

    st.title("Clinical Trial Eligibility Decision Engine")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Patients Analyzed", "1248")
    col2.metric("Eligible Patients", "342")
    col3.metric("Active Trials", "97")
    col4.metric("AI Accuracy", "92%")

    st.subheader("Eligibility Distribution")

    data = pd.DataFrame({
        "Status": ["Eligible", "Not Eligible"],
        "Count": [342, 906]
    })

    fig = px.pie(data, names="Status", values="Count")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Recent Patient Evaluations")

    table = pd.DataFrame({
        "Patient ID": ["P1023", "P1056", "P1078"],
        "Disease": ["Lung Cancer", "Breast Cancer", "Leukemia"],
        "Eligibility": ["Eligible", "Not Eligible", "Eligible"],
        "Score": [0.87, 0.31, 0.79],
        "Recommended Trials": [3, 1, 2]
    })

    st.dataframe(table)


# -------------------- PATIENT ANALYSIS --------------------

elif menu == "Patient Analysis":

    st.title("Patient Analysis")

    patient_id = st.text_input("Enter Patient ID")

    if st.button("Analyze Patient"):

        st.subheader("Patient Information")

        col1, col2 = st.columns(2)

        with col1:
            st.write("Patient ID:", "P2024-21")
            st.write("Age:", 52)
            st.write("Gender:", "Male")
            st.write("Diagnosis:", "Lung Cancer")

        with col2:
            st.write("Condition:", "Hypertension")
            st.write("Medication:", "Cisplatin")
            st.write("Smoking History:", "Yes")

        st.subheader("AI Extracted Features")

        st.success("✔ Disease: Lung Cancer")
        st.success("✔ Stage: II")
        st.success("✔ Medication: Cisplatin")
        st.success("✔ No Exclusion Conditions")

        st.subheader("Eligibility Score")

        st.progress(87)
        st.write("Status: **Eligible**")
        st.write("Confidence Score: **0.87**")


# -------------------- TRIAL RECOMMENDATIONS --------------------

elif menu == "Trial Recommendations":

    st.title("Clinical Trial Recommendations")

    trials = pd.DataFrame({
        "Trial ID": ["NCT04321", "NCT05310", "NCT06399"],
        "Disease": ["Lung Cancer", "Lung Cancer", "Lung Cancer"],
        "Match Score": ["87%", "82%", "79%"],
        "Sponsor": ["Pfizer", "NIH", "AstraZeneca"],
        "Location": ["USA", "UK", "Germany"]
    })

    st.table(trials)

    trial = st.selectbox("Select Trial to View Details", trials["Trial ID"])

    if trial:
        st.subheader("Trial Details")

        st.write("Trial ID:", trial)
        st.write("Disease:", "Lung Cancer")
        st.write("Age Requirement:", "18–65")
        st.write("Exclusion:", "Diabetes")
        st.write("Sponsor:", "Pfizer")
        st.write("Location:", "USA")


# -------------------- EXPLAINABLE AI --------------------

elif menu == "Explainable AI":

    st.title("Explainable AI Decision")

    st.subheader("Final Decision")

    st.success("Eligible")
    st.write("Confidence Score: **0.87**")

    st.subheader("Feature Contribution")

    explanation = pd.DataFrame({
        "Feature": ["Cancer Diagnosis Match", "Age within Range", "No Exclusion Condition"],
        "Impact": [0.41, 0.28, 0.19]
    })

    fig = px.bar(explanation, x="Feature", y="Impact")
    st.plotly_chart(fig)

    st.subheader("Rule Evaluation")

    st.success("✔ Age ≥ 18")
    st.success("✔ Age ≤ 65")
    st.success("✔ Lung Cancer Diagnosis")
    st.error("✘ Diabetes Restriction")


# -------------------- REPORTS --------------------

elif menu == "Reports":

    st.title("System Reports")

    st.write("Download Reports")

    st.download_button(
        label="Download Eligibility Summary",
        data="Sample Report Data",
        file_name="eligibility_report.txt"
    )

    st.download_button(
        label="Download Trial Match Report",
        data="Sample Trial Report",
        file_name="trial_report.txt"
    )

    st.subheader("AI Accuracy Trend")

    trend = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr"],
        "Accuracy": [85, 88, 90, 92]
    })

    fig = px.line(trend, x="Month", y="Accuracy")
    st.plotly_chart(fig)