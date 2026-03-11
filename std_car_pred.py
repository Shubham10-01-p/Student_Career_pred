# Welcome to GitHub Desktop!


import streamlit as st
import requests
from streamlit_lottie import st_lottie
import matplotlib.pyplot as plt

# ---------------- Load Lottie Animations ----------------
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

career_animation = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json") # career choice
study_animation = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_pprxh53t.json")  # studying

st.subheader("📧 Contact Information")
email = st.text_input("Enter your Email ID")
mobile = st.text_input("Enter your Mobile Number")

if st.button("Save Contact Info"):
    if email and mobile:
        st.success(f"✅ Your details have been saved!\n\n📧 Email: {email}\n📱 Mobile: {mobile}")
    if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        st.error("❌ Invalid Email format. Please enter a valid email (e.g. example@mail.com).")
    if mobile and (not mobile.isdigit() or len(mobile) != 10):
        st.error("❌ Invalid Mobile Number. Please enter a 10-digit number.")
    else:
        st.warning("⚠️ Please enter both Email and Mobile Number.")

# ---------------- App Title ----------------
st.set_page_config(page_title="Student Career Counseling", page_icon="🎓", layout="wide")
st.title('🎓 STUDENT CAREER COUNSELING')
st.header('For Science, Arts, Commerce Students')
st.subheader('Welcome!')
st.write("This is a prototype of our career counseling app 🚀")

st.subheader("📝 Aptitude & Interest Questions")

q1 = st.radio("1️⃣ Which activity do you enjoy the most?", 
              ["🔬 Science Projects", "🎨 Arts & Writing", "💼 Business Puzzles", "🌍 History & Cultures"])

q2 = st.radio("2️⃣ Which subject excites you the most?", 
              ["📐 Mathematics", "🧪 Science", "📖 Literature", "📊 Economics"])

q3 = st.radio("3️⃣ If you had to choose a project, which would you prefer?", 
              ["🛠️ Build a Robot/App", "📰 Write/Make a Documentary", "📈 Business Plan", "⚖️ Debate"])

q4 = st.radio("4️⃣ Which career path sounds most appealing to you?",
            ["👨‍🔬 Scientist / Engineer / Doctor","🎭 Artist / Writer / Actor","👔 Entrepreneur / Chartered Accountant / Analyst","👩‍🏫 Teacher / Lawyer / Journalist"])

q5 = st.radio("5️⃣ How do you usually solve problems?",
            ["🔍 Research & Experiment","💡 Creative Thinking","📊 Logical Analysis","🤝 Discuss & Collaborate"])


st.subheader(" Analysis of Your Interests ")
# Show animation at top
st_lottie(career_animation, height=350, key="career")


categories = {"Science/Tech": 0, "Arts/Creative": 0, "Business/Finance": 0, "Social/Humanities": 0}

mapping = {
    "🔬 Science Projects": "Science/Tech",
    "📐 Mathematics": "Science/Tech",
    "🛠️ Build a Robot/App": "Science/Tech",
    "👨‍🔬 Scientist / Engineer / Doctor": "Science/Tech",
    "🔍 Research & Experiment": "Science/Tech",
    
    "🎨 Arts & Writing": "Arts/Creative",
    "📖 Literature": "Arts/Creative",
    "📰 Write/Make a Documentary": "Arts/Creative",
    "🎭 Artist / Writer / Actor": "Arts/Creative",
    "💡 Creative Thinking": "Arts/Creative",
    
    "💼 Business Puzzles": "Business/Finance",
    "📊 Economics": "Business/Finance",
    "📈 Business Plan": "Business/Finance",
    "👔 Entrepreneur / Chartered Accountant / Analyst": "Business/Finance",
    "📊 Logical Analysis": "Business/Finance",
    
    "🌍 History & Cultures": "Social/Humanities",
    "🧪 Science": "Social/Humanities",   # can also be Science, adjust if needed
    "⚖️ Debate": "Social/Humanities",
    "👩‍🏫 Teacher / Lawyer / Journalist": "Social/Humanities",
    "🤝 Discuss & Collaborate": "Social/Humanities"
}

# Count responses
responses = [q1, q2, q3, q4, q5]
for ans in responses:
    if ans in mapping:
        categories[mapping[ans]] += 1

# ---------------- Plot Results ----------------
st.subheader("📊 Your Interest Distribution")

fig, ax = plt.subplots()
ax.bar(categories.keys(), categories.values(), color=["skyblue", "lightgreen", "orange", "violet"])
ax.set_ylabel("Number of Selections")
ax.set_title("Student Interest Analysis")
st.pyplot(fig)

# ---------------- Inputs ----------------
col1, col2 = st.columns(2)

with col1:
    name = st.text_input('✍️ Enter your name')
    class_choice = st.selectbox("📘 Select your class:- ", ['10th','12th'])
    if class_choice == '10th':
        x = st.selectbox('🏫 Select your choice of Stream :- ', ['Science', 'Arts', 'Commers'])
        if x == 'Science':
            st.write("🔬 Science stream is ideal for students interested in subjects like Physics, Chemistry, Biology, and Mathematics. It opens up career paths in Engineering, Medicine, Research, and more." 
                     "Students in this stream develop analytical and problem-solving skills.")
        elif x == 'Arts':
            st.write("🎨 Arts stream is perfect for students passionate about subjects like History, Geography, Political Science, and Literature. It leads to careers in Law, Journalism, Education, and more." 
                     "Students in this stream enhance their critical thinking and communication skills.")
        else:
            st.write("💼 Commerce stream suits students interested in subjects like Economics, Business Studies, and Accountancy. It paves the way for careers in Finance, Marketing, CA, and more." 
                     "Students in this stream gain skills in business management and financial analysis.") 
    if class_choice == '12th':
        stream_choice = st.selectbox('📚 Select your stream of choice:- ', ['Science', 'Arts', 'Commerce'])
        if stream_choice == 'Arts':
            subject = st.selectbox('🎨 Select your interest area:- ', ['History', 'Psychology', 'Law', 'Journalism', 'Literature', 'Sociology'])
        elif stream_choice == 'Science':
            st.write("🔬 Science stream is ideal for students interested in subjects like Physics, Chemistry, Biology, and Mathematics. It opens up career paths in Engineering, Medicine, Research, and more." 
                     "Students in this stream develop analytical and problem-solving skills.")
        else:
            st.write("💼 Commerce stream suits students interested in subjects like Economics, Business Studies, and Accountancy. It paves the way for careers in Finance, Marketing, CA, and more." 
                     "Students in this stream gain skills in business management and financial analysis.")
    
    st.write(f"👤 Your name is {name}, Your Class is {class_choice} and you selected {x} stream")

with col2:
    st_lottie(study_animation, height=200, key="study")

st.write("📌 Enter your marks below:")

marks_col1, marks_col2, marks_col3 = st.columns(3)

st.subheader("🔢 Enter your subject marks (out of 100):")

with marks_col1:
    physics = st.number_input('Physics', min_value=0, max_value=100, step=1)
    chemistry = st.number_input('Chemistry', min_value=0, max_value=100, step=1)

with marks_col2:
    maths = st.number_input('Maths', min_value=0, max_value=100, step=1)
    biology = st.number_input('Biology', min_value=0, max_value=100, step=1)

with marks_col3:
    english = st.number_input('English', min_value=0, max_value=100, step=1)
    cs = st.number_input('Computer Science', min_value=0, max_value=100, step=1)

# ---------------- Science % Calculation ----------------
if x == 'Science':
    science_percentage = (physics + chemistry + maths) / 300 * 100
    st.progress(int(science_percentage))  # progress bar
    st.write(f'📊 Your Science subject percentage is **{science_percentage:.2f}%**')
elif x == 'Arts':
    arts_percentage = (english) / 100 * 100
    st.progress(int(arts_percentage))
    st.write(f'📊 Your Arts subject percentage is **{arts_percentage:.2f}%**')
else: 
    commerce_percentage = (maths + english ) / 200 * 100
    st.progress(int(commerce_percentage))
    st.write(f'📊 Your Commerce subject percentage is **{commerce_percentage:.2f}%**')
st.info('If you are dedicated in your studies you can achieve anything in life no matter what your stream is!!')

# ---------------- Career Suggestion Logic ----------------
def suggest_career():
    if x == 'Science':
        if science_percentage >= 90:
            st.write("🚀 Excellent! You have a strong foundation in Science. And you should defenitely go for Engineering")
            return "🌟 You can go for **Engineering, Medicine, Data Science, Research Scientist, etc.**"
        elif biology >= 80:
            return "🧬 You have a good score in Biology. You can consider **Medicine, Dentistry, Veterinary Science, Biotechnology, etc.**"
        elif science_percentage >= 75:
            return "💡 You can explore **Pharmacy, Nursing, Biotech, Forensic Science, etc.**"
        elif science_percentage >= 40:
            return "📖 Focus on improvement. Try **B.Sc. general, vocational courses, or switch to Arts/Commerce.**"
        else:
            return "⚠️ Better to re-evaluate your interests and explore **Arts/Commerce or skill-based courses.**"
    
    elif x == 'Arts':
        st.selectbox('🎨 Select your interest area:- ', ['History', 'Psychology', 'Law', 'Journalism', 'Literature', 'Sociology'])
        if subject == "History":
            st.subheader("📜 History")
            st.write("History is the study of past events, particularly in human affairs. It helps us understand societies, cultures, and how the world has evolved over time.")

        elif subject == "Psychology":
            st.subheader("🌍Psychology")
            st.write("Psychology is the scientific study of mind and behavior. Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious phenomena, and mental processes such as thoughts, feelings, and motives. ")

        elif subject == "Law":
            st.subheader("🏛️ Law")
            st.write("Law is the study of the rights and duties of citizens, the role of government, and how political systems function in society.")
        return "🎨 Great choice! You can go for **Psychology, Law, Journalism, Literature, Sociology, etc.**"
    
    else:  # Commerce
        return "💼 You can pursue **CA, BBA, B.Com, Business Analyst, Finance, Marketing, etc.**"

# ---------------- Chatbot Interface ----------------
st.subheader("🤖 Career Counseling Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("💬Ask me anything about your career:")

if st.button("Send"):
    if user_input:
        st.session_state.chat_history.append({"role": "user", "text": user_input})
        
        if "marks" in user_input.lower() or "stream" in user_input.lower():
            bot_reply = suggest_career()
        else:
            bot_reply = "✨ I can guide you based on your marks and interests. Try asking: *What can I do with my marks?*"
        
        st.session_state.chat_history.append({"role": "bot", "text": bot_reply})

# Display chat history with styling
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"🧑 **You:** {chat['text']}")
    else:
        st.success(f"🤖 **Bot:** {chat['text']}")

# ---------------- Final Suggestion ----------------
if st.button('🎯 Get Career Suggestion'):
    st.info(suggest_career())

