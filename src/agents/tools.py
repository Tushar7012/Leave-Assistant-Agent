import os

# Fix OpenMP library conflict
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.tools import tool

# --- 1. Fake Database ---
# Standard company emails for managers and HR
MANAGER_EMAIL = "arjun.verma@example.com"  # Arjun Verma - Senior Engineer/Team Lead
HR_EMAIL = "priya.singh@example.com"  # Priya Singh - HR Manager

MOCK_DB = {
    "EMP001": {"name": "Raj Sharma", "role": "Engineer", "email": "raj.sharma@example.com", "dept": "IT", "salary": 50000, "hire_date": "2020-01-15", "leaves": {"sick": 8, "casual": 7, "annual": 12}},
    "EMP002": {"name": "Priya Singh", "role": "HR Manager", "email": "priya.singh@example.com", "dept": "HR", "salary": 45000, "hire_date": "2019-03-22", "leaves": {"sick": 10, "casual": 9, "annual": 15}},
    "EMP003": {"name": "Arjun Verma", "role": "Senior Engineer", "email": "arjun.verma@example.com", "dept": "IT", "salary": 55000, "hire_date": "2021-06-01", "leaves": {"sick": 6, "casual": 8, "annual": 10}},
    "EMP004": {"name": "Suman Patel", "role": "Finance Manager", "email": "suman.patel@example.com", "dept": "Finance", "salary": 60000, "hire_date": "2018-07-30", "leaves": {"sick": 12, "casual": 11, "annual": 18}},
    "EMP005": {"name": "Kavita Rao", "role": "HR Executive", "email": "kavita.rao@example.com", "dept": "HR", "salary": 47000, "hire_date": "2020-11-10", "leaves": {"sick": 7, "casual": 6, "annual": 11}},
    "EMP006": {"name": "Amit Gupta", "role": "Marketing Manager", "email": "amit.gupta@example.com", "dept": "Marketing", "salary": 52000, "hire_date": "2020-09-25", "leaves": {"sick": 9, "casual": 10, "annual": 13}},
    "EMP007": {"name": "Neha Desai", "role": "Software Engineer", "email": "neha.desai@example.com", "dept": "IT", "salary": 48000, "hire_date": "2019-05-18", "leaves": {"sick": 11, "casual": 8, "annual": 14}},
    "EMP008": {"name": "Rahul Kumar", "role": "Senior Engineer", "email": "rahul.kumar@example.com", "dept": "IT", "salary": 53000, "hire_date": "2021-02-14", "leaves": {"sick": 5, "casual": 9, "annual": 9}},
    "EMP009": {"name": "Anjali Mehta", "role": "Finance Analyst", "email": "anjali.mehta@example.com", "dept": "Finance", "salary": 61000, "hire_date": "2018-12-03", "leaves": {"sick": 12, "casual": 12, "annual": 17}},
    "EMP010": {"name": "Vijay Nair", "role": "Marketing Executive", "email": "vijay.nair@example.com", "dept": "Marketing", "salary": 50000, "hire_date": "2020-04-19", "leaves": {"sick": 8, "casual": 10, "annual": 12}},
}

@tool
def fetch_employee_data(employee_id: str) -> dict:
    """Fetch employee details and leave balance by Employee ID."""
    employee = MOCK_DB.get(employee_id)
    if not employee:
        return {"error": "Employee not found."}
    return employee

# --- 2. Policy RAG Tool ---
# Initialize Vector Store (Lazy load pattern or global init)
_vectorstore = None

def get_vectorstore():
    global _vectorstore
    if _vectorstore is None:
        policy_path = os.path.join(os.path.dirname(__file__), '../../documents/Employee_Leave_Policy.txt')
        loader = TextLoader(policy_path)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)
        # Using FakeEmbeddings to avoid TensorFlow issues
        # For production, replace with proper embeddings after fixing TensorFlow
        embeddings = FakeEmbeddings(size=384)
        _vectorstore = FAISS.from_documents(docs, embeddings)
    return _vectorstore

@tool
def policy_search_tool(query: str) -> str:
    """Search the company leave policy document to answer questions."""
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever()
    docs = retriever.invoke(query)
    return "\n\n".join([d.page_content for d in docs])

# --- 3. Email Tool ---
@tool
def send_email_tool(recipient: str, subject: str, body: str) -> str:
    """Send an email to an employee. Returns a success message."""
    # In a real app, use SMTP or an API like SendGrid
    email_content = f"--- SENDING EMAIL ---\nTo: {recipient}\nSubject: {subject}\nBody:\n{body}\n-----------------------"
    return f"Email sent successfully. Details:\n{email_content}"
