import streamlit as st
from openai import OpenAI

# =========================
# Page Title
# =========================
st.set_page_config(
    page_title="Nexora Hub AI",
    page_icon="💬",
    layout="centered"
)

# =========================
# Main Title
# =========================
st.title("💬 Nexora Hub AI")

st.write(
    "AI chatbot for blockchain financial analysis and research project support."
)

# =========================
# OpenAI Key from Secrets
# =========================
openai_api_key = st.secrets["OPENAI_API_KEY"]

# Create OpenAI client
client = OpenAI(api_key=openai_api_key)

# =========================
# Session State
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# Display old messages
# =========================
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =========================
# Chat Input
# =========================
if prompt := st.chat_input("Ask anything..."):

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # ====================================
    # Net Profit Analysis
    # ====================================
    if "net profit" in prompt.lower() or "صافي الربح" in prompt:

        with st.chat_message("assistant"):

            st.image("Screenshot 2026-04-26 043008.png")

            st.write("""
يوضح تحليل صافي الربح وجود تحسن ملحوظ نتيجة تحسين كفاءة المعاملات باستخدام تقنية البلوك تشين.
""")

        st.stop()

    # ====================================
    # Assets Analysis
    # ====================================
    if "assets" in prompt.lower() or "الأصول" in prompt or "إجمالي الأصول" in prompt:

        with st.chat_message("assistant"):

            st.image("Screenshot 2026-04-26 045020.png")

            st.write("""
يوضح تحليل إجمالي الأصول وجود نمو تدريجي في قيمة الأصول نتيجة التوسع في استخدام التكنولوجيا المالية.
""")

        st.stop()

    # ====================================
    # ROA Analysis
    # ====================================
    if "roa" in prompt.lower() or "العائد على الأصول" in prompt:

        with st.chat_message("assistant"):

            st.image("Screenshot 2026-04-26 050316.png")

            st.write("""
يوضح تحليل العائد على الأصول تحسن كفاءة استخدام الأصول في تحقيق الأرباح.
""")

        st.stop()

    # ====================================
    # ROE Analysis
    # ====================================
    if "roe" in prompt.lower() or "العائد على حقوق الملكية" in prompt:

        with st.chat_message("assistant"):

            st.image("Screenshot 2026-04-26 053321.png")

            st.write("""
يوضح تحليل العائد على حقوق الملكية تحسن العوائد للمساهمين نتيجة تطوير الأداء المالي.
""")

        st.stop()

    # ====================================
    # OpenAI Normal Response
    # ====================================
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": m["role"],
                "content": m["content"]
            }
            for m in st.session_state.messages
        ],
        stream=True,
    )

    # Show AI response
    with st.chat_message("assistant"):
        response = st.write_stream(stream)

    # Save AI response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
