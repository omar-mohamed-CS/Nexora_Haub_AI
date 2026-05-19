import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("💬 Nexora Hub AI")
st.write(
    "AI chatbot for blockchain financial analysis and research project support."
)

# OpenAI API Key
openai_api_key = st.text_input("OpenAI API Key", type="password")

if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")

else:

    # Create OpenAI client
    client = OpenAI(api_key=openai_api_key)

    # Session messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask anything about the project..."):

        # Save user message
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        # Show user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # =========================
        # NET PROFIT ANALYSIS
        # =========================

        if "net profit" in prompt.lower() or "صافي الربح" in prompt:

            with st.chat_message("assistant"):

                st.image("Screenshot 2026-04-26 043008.png")

                st.write("""
يوضح تحليل صافي الربح وجود تحسن ملحوظ
نتيجة تحسين كفاءة المعاملات باستخدام تقنية البلوك تشين.
""")

            st.stop()

        # =========================
        # OPENAI RESPONSE
        # =========================

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

        # Show assistant response
        with st.chat_message("assistant"):
            response = st.write_stream(stream)

        # Save assistant response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )
