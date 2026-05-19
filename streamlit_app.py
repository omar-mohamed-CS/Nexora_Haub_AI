import streamlit as st
from openai import OpenAI
import PyPDF2

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Nexora Hub AI",
    page_icon="💬",
    layout="centered"
)

# =====================================================
# TITLE
# =====================================================
st.title("💬 Nexora Hub AI")

st.write(
    "AI chatbot for blockchain financial analysis and research project support."
)

# =====================================================
# OPENAI API KEY
# =====================================================
openai_api_key = st.secrets["OPENAI_API_KEY"]

# =====================================================
# OPENAI CLIENT
# =====================================================
client = OpenAI(api_key=openai_api_key)

# =====================================================
# READ PDF FILE
# =====================================================
pdf_text = ""

with open("Nx1.pdf", "rb") as file:

    reader = PyPDF2.PdfReader(file)

    for page in reader.pages:

        text = page.extract_text()

        if text:
            pdf_text += text

# =====================================================
# SESSION STATE
# =====================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================================
# DISPLAY OLD MESSAGES
# =====================================================
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# =====================================================
# CHAT INPUT
# =====================================================
if prompt := st.chat_input("Ask anything about the project..."):

    # =================================================
    # SAVE USER MESSAGE
    # =================================================
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # =================================================
    # SHOW USER MESSAGE
    # =================================================
    with st.chat_message("user"):

        st.markdown(prompt)

    # =================================================
    # NET PROFIT
    # =================================================
    if (
        "net profit" in prompt.lower()
        or "صافي الربح" in prompt
    ):

        with st.chat_message("assistant"):

            st.image("Screenshot 2026-04-26 043008.png")

            st.markdown("""
## تحليل صافي الربح (Net Profit)

يتضح من الشكل أن متوسط صافي الربح قبل التطبيق كان (8.75)

بينما بعد التطبيق أصبح (32.17)

مما يشير إلى وجود تحسن في الأداء المالي للبنك.

وهو ما يعكس تأثيرًا إيجابيًا للتقنية المستخدمة
على جودة المعلومات المالية.
""")

        st.stop()

    # =================================================
    # ASSETS
    # =================================================
    if (
        "assets" in prompt.lower()
        or "إجمالي الأصول" in prompt
        or "الاصول" in prompt
    ):

        with st.chat_message("assistant"):

            st.image("Screenshot 2026-04-26 045020.png")

            st.markdown("""
## تحليل إجمالي الأصول (Assets)

يتضح من الشكل ارتفاع إجمالي الأصول
بعد تطبيق البلوك تشين.

مما يشير إلى نمو حجم البنك
وتحسن كفاءة إدارة الموارد.

وهو ما يعكس تأثيرًا إيجابيًا
للتقنية المستخدمة
على ملائمة المعلومات المالية.
""")

        st.stop()

    # =================================================
    # ROA
    # =================================================
    if (
        "roa" in prompt.lower()
        or "return on assets" in prompt.lower()
        or "العائد على الأصول" in prompt
    ):

        with st.chat_message("assistant"):

            st.image("Screenshot 2026-04-26 050316.png")

            st.markdown("""
## تحليل العائد على الأصول (ROA)

يتضح من الشكل وجود تحسن
في متوسط العائد على الأصول
بعد تطبيق التقنية.

مما يشير إلى زيادة كفاءة البنك
في استخدام أصوله لتحقيق الأرباح.

وهو ما يعكس تأثيرًا إيجابيًا
للتقنية المستخدمة
على موثوقية المعلومات المالية.
""")

        st.stop()

    # =================================================
    # ROE
    # =================================================
    if (
        "roe" in prompt.lower()
        or "return on equity" in prompt.lower()
        or "العائد على حقوق الملكية" in prompt
    ):

        with st.chat_message("assistant"):

            st.image("Screenshot 2026-04-26 053321.png")

            st.markdown("""
## تحليل العائد على حقوق الملكية (ROE)

يتضح من الشكل وجود تحسن
في متوسط العائد على حقوق الملكية
بعد التطبيق.

مما يشير إلى زيادة قدرة البنك
على تحقيق عائد للمساهمين.

وهو ما يعكس تأثيرًا إيجابيًا
لتقنية البلوك تشين المستخدمة
على قابلية المقارنة والشفافية.
""")

        st.stop()

    # =================================================
    # SEARCH INSIDE PDF
    # =================================================
    search_text = ""

    if (
        "مقدمة" in prompt
        or "introduction" in prompt.lower()
    ):

        start = pdf_text.find("مقدمة")

        if start != -1:
            search_text = pdf_text[start:start+4000]

    elif (
        "مشكلة" in prompt
        or "problem" in prompt.lower()
    ):

        start = pdf_text.find("مشكلة")

        if start != -1:
            search_text = pdf_text[start:start+4000]

    elif (
        "الفصل الثاني" in prompt
        or "chapter 2" in prompt.lower()
    ):

        start = pdf_text.find("الفصل الثاني")

        if start != -1:
            search_text = pdf_text[start:start+5000]

    elif (
        "النتائج" in prompt
        or "results" in prompt.lower()
    ):

        start = pdf_text.find("النتائج")

        if start != -1:
            search_text = pdf_text[start:start+5000]

    elif (
        "التوصيات" in prompt
        or "recommendations" in prompt.lower()
    ):

        start = pdf_text.find("التوصيات")

        if start != -1:
            search_text = pdf_text[start:start+5000]

    else:

        search_text = pdf_text[:6000]

    # =================================================
    # SYSTEM PROMPT
    # =================================================
    system_prompt = f"""
You are Nexora Hub AI.

You are an AI assistant specialized in:
- Blockchain
- Banking systems
- Financial analysis
- Research projects

Use ONLY the following extracted text
from the uploaded PDF project
to answer the user.

Extracted Text:

{search_text}

Answer clearly and professionally.
You can answer in Arabic or English.
"""

    # =================================================
    # OPENAI RESPONSE
    # =================================================
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",

        messages=[
            {
                "role": "system",
                "content": system_prompt
            },

            *[
                {
                    "role": m["role"],
                    "content": m["content"]
                }
                for m in st.session_state.messages
            ]
        ],

        stream=True,
    )

    # =================================================
    # SHOW RESPONSE
    # =================================================
    with st.chat_message("assistant"):

        response = st.write_stream(stream)

    # =================================================
    # SAVE RESPONSE
    # =================================================
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
