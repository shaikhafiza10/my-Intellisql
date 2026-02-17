import streamlit as st
import os
import sqlite3
from dotenv import load_dotenv
from google import genai
def load_image(local_path, url, width=300):
    if os.path.exists(local_path):
        st.image(local_path, width=width)
    else:
        st.image(url, width=width)

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


st.set_page_config(
    page_title="IntelliSQL",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
body {
    background-color: #0E1117;
    color: white;
}

.big-title {
    font-size: 40px;
    font-weight: bold;
    color: #00FFAA;
}

.sub-title {
    font-size: 18px;
    color: #CCCCCC;
}

.center {
    text-align: center;
}

.sql-box {
    background-color: #1E1E1E;
    padding: 10px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

prompt = """
You are an expert in converting English questions to SQL queries.
The SQL database name is STUDENTS and has columns:
NAME, CLASS, MARKS, COMPANY.

Rules:
- Only return pure SQL query.
- No explanation.
- No extra text.

Example:
How many records are present?
SELECT COUNT(*) FROM STUDENTS;

Example:
Show students in MCom class
SELECT * FROM STUDENTS WHERE CLASS="MCom";
"""


# -------------------- Gemini Response --------------------
def get_response(question):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt + "\nQuestion:\n" + question
    )

    sql = response.text.strip()

    if "```" in sql:
        sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql


# -------------------- SQL Reader --------------------
def read_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return rows


# -------------------- Home Page --------------------
def page_home():

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<p class="big-title">Welcome to IntelliSQL</p>', unsafe_allow_html=True)

        st.markdown("""
        <p class="sub-title">
        Revolutionizing database querying with advanced LLM capabilities.
        </p>
        """, unsafe_allow_html=True)

        st.markdown("""
        ### Wide Range of Offerings
        ✔ Natural Language Queries  
        ✔ Intelligent SQL Generation  
        ✔ Real-time Query Execution  
        ✔ User-friendly Interface  
        ✔ Smart Analytics  
        """)

    with col2:
       load_image("C:/Users/HP/Downloads/home.png","https://www.vecteezy.com/vector-art/66829737-data-warehouse-icon-concept-in-blue-color",width=300)
# -------------------- About Page --------------------
def page_about():

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<p class="big-title">About IntelliSQL</p>', unsafe_allow_html=True)

        st.write("""
        IntelliSQL is an innovative project aimed at revolutionizing database querying using
        advanced Language Model capabilities.

        Powered by cutting-edge LLM architecture, this system offers users an intelligent platform
        for interacting with SQL databases effortlessly and intuitively.
        """)

    with col2:
        load_image("C:/Users/HP/Downloads/about.png","https://en.wikipedia.org/wiki/Oracle_SQL_Developer",width=300)


# -------------------- Intelligent Query Page --------------------
def page_intelligent_query_assistance():

    col1, col2 = st.columns([2, 1])

    with col1:

        st.markdown('<p class="big-title">Intelligent Query Assistance</p>', unsafe_allow_html=True)

        st.markdown("""
        Enter your question in natural language and IntelliSQL will convert it into SQL and execute it.
        """)

        user_input = st.text_input("Enter your Query:", placeholder="Example: Show students working in Infosys")

        if st.button("Get Answer"):

            if user_input:

                try:
                    sql_query = get_response(user_input)

                    st.markdown("### Generated SQL Query")
                    st.code(sql_query, language="sql")

                    data = read_query(sql_query, "data.db")

                    st.markdown("### The Response is:")
                    st.table(data)

                except Exception as e:
                    st.error(f"Error: {e}")

    with col2:
        load_image("C:/Users/HP/Downloads/query.png","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSW_ipAQuQHOXfcI9NeMx22ssQCaJ9WsPbAuPRAVQtK1czQIxlP",width=300)


# -------------------- Sidebar Navigation --------------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "",
    ["Home", "About", "Intelligent Query Assistance"]
)

# -------------------- Page Routing --------------------
if page == "Home":
    page_home()

elif page == "About":
    page_about()

elif page == "Intelligent Query Assistance":
    page_intelligent_query_assistance()
