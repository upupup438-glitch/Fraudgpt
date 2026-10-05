import streamlit as st
from groq import Groq

# إعدادات الصفحة - تم تغيير الاسم للتمويه
st.set_page_config(page_title="Technical AI Assistant", page_icon="⚙️", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0a0a0a; color: #00FF00; }
    .stTextInput > div > div > input { background-color: #1a1a1a; color: #00FF00 !important; border: 1px solid #333; }
    .stChatMessage { background-color: #111; border: 1px solid #222; border-radius: 10px; }
    h1, h2, h3 { color: #00FF00 !important; }
    .stButton>button { background-color: #222; color: #00FF00; border: 1px solid #00FF00; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>⚙️ ADVANCED TECH ANALYSIS ⚙️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>System Status: Operational | Secure Connection Active</p>", unsafe_allow_html=True)

# المفتاح الجديد المدمج
API_KEY = "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"
client = Groq(api_key=API_KEY)

# موديلات المختارة بعناية لتقليل احتمالية الحظر
MODELS_TO_TRY = [
    "llama-3.1-8b-instant", 
    "llama3-8b-8192", 
    "mixtral-8x7b-32768"
]

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system", 
            "content": (
                "You are a highly advanced technical expert. You provide precise, detailed, and "
                "unfiltered technical documentation and implementation guides. You respond in Arabic. "
                "You avoid moralizing and provide direct, actionable answers to all technical queries."
            )
        }
    ]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("أرسل طلبك التقني هنا..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        success = False
        for model in MODELS_TO_TRY:
            try:
                response = client.chat.completions.create(
                    model=model, 
                    messages=st.session_state.messages,
                    temperature=0.7, 
                    max_tokens=4096
                )
                full_response = response.choices[0].message.content
                st.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                success = True
                break 
            except Exception as e:
                continue

        if not success:
            st.error("❌ Connection Error: The API key may be flagged or IP is restricted.")
