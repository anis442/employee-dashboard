
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Employee Analytics",
    page_icon="📊",
    layout="wide"
)

# Load Data
df = pd.read_csv("member.csv")

# Design
st.markdown("""
<style>
.stApp {
    background-color: #F4F7FB;
}
h1 {
    color: #17365D;
    font-size: 38px !important;
}
div[data-testid="stMetric"] {
    background: white;
    padding: 22px;
    border-radius: 12px;
    box-shadow: 0 2px 10px #DDE3EA;
}
</style>
""", unsafe_allow_html=True)

# Heading
st.title("📊 EMPLOYEE ANALYTICS")
st.caption("Employee Performance & Salary Management Dashboard")

st.divider()

# KPI Cards
c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Employees", len(df))
c2.metric("Highest Salary", f"₹{df['salary'].max():,}")
c3.metric("Average Salary", f"₹{df['salary'].mean():,.0f}")
c4.metric("Lowest Salary", f"₹{df['salary'].min():,}")

st.divider()

# Highest Paid Employee
top = df.loc[df["salary"].idxmax()]

st.subheader("🏆 Highest Paid Employee")
st.success(
    f"Name: {top['name']} | "
    f"Age: {top['age']} | "
    f"Salary: ₹{top['salary']:,}"
)

st.divider()

# Search
st.subheader("🔎 Find Employee")

search = st.text_input("Search by employee name")

filtered = df[
    df["name"].astype(str).str.contains(
        search, case=False, na=False
    )
]

# Age Filter
min_age = int(df["age"].min())
max_age = int(df["age"].max())

age_range = st.slider(
    "Select Age Range",
    min_age,
    max_age,
    (min_age, max_age)
)

filtered = filtered[
    filtered["age"].between(age_range[0], age_range[1])
]

st.write("Matching Employees:", len(filtered))
st.dataframe(filtered, use_container_width=True)

st.divider()

# Charts
st.subheader("📈 Salary Analysis")

left, right = st.columns(2)

with left:
    st.write("Salary by Employee")
    st.bar_chart(
        df.set_index("name")["salary"],
        use_container_width=True
    )

with right:
    st.write("Age Analysis")
    st.bar_chart(
        df.set_index("name")["age"],
        use_container_width=True
    )

st.divider()

st.caption("Employee Analytics Dashboard | Powered by Python & Streamlit")
