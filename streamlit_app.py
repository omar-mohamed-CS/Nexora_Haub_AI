import streamlit as st
import google.generativeai as genai
import PyPDF2

# =========================
# إعداد الصفحة
# =========================

st.set_page_config(
    page_title="Nexora Hub AI",
    page_icon="💬",
    layout="wide"
)

# =========================
# API KEY
# =========================

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-pro")

# =========================
# قراءة ملف الـ PDF
# =========================

pdf_text = ""

try:
    with open("Nx1.pdf", "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text = page.extract_text()

            if text:
                pdf_text += text

except:
    pdf_text = "PDF file not found."

# =========================
# الصور والتحليلات
# =========================

indicators_data = """

1) Net Profit - صافي الربح

Image:
Screenshot 2026-04-26 043008.png

Explanation:
يتضح من الشكل أن متوسط صافي الربح قبل التطبيق كان (8.75)
بينما بعد التطبيق أصبح (32.17)
مما يشير إلى وجود تحسن في الأداء المالي للبنك
وهو ما يعكس تأثيرًا إيجابيًا للتقنية المستخدمة على جودة المعلومات المالية.

---------------------------------------------------

2) Assets - إجمالي الأصول

Image:
Screenshot 2026-04-26 045020.png

Explanation:
يتضح من الشكل ارتفاع إجمالي الأصول بعد تطبيق البلوك تشين
مما يشير إلى نمو حجم البنك وتحسن كفاءة إدارة الموارد
وهو ما يعكس تأثيرًا إيجابيًا للتقنية المستخدمة
على ملائمة المعلومات المالية.

---------------------------------------------------

3) ROA - Return On Assets - العائد على الأصول

Image:
Screenshot 2026-04-26 050316.png

Explanation:
يتضح من الشكل وجود تحسن في متوسط العائد على الأصول
بعد تطبيق التقنية مما يشير إلى زيادة كفاءة البنك
في استخدام أصوله لتحقيق الأرباح
وهو ما يعكس تأثيرًا إيجابيًا للتقنية المستخدمة
على موثوقية المعلومات المالية.

---------------------------------------------------

4) ROE - Return On Equity - العائد على حقوق الملكية

Image:
Screenshot 2026-04-26 053321.png

Explanation:
يتضح من الشكل وجود تحسن في متوسط العائد
على حقوق الملكية بعد التطبيق
مما يشير إلى زيادة قدرة البنك على تحقيق عائد للمساهمين
وهو ما يعكس تأثيرًا إيجابيًا لتقنية البلوك تشين
على قابلية المقارنة والشفافية.

"""

# =========================
# تصميم الواجهة
# =========================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.stChatInput input {
    background-color: #262730;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================
# العنوان
# =========================

st.title("💬 Nexora Hub AI")

st.write(
    "AI chatbot for blockchain financial analysis and research project support."
)

# =========================
# عرض الصور
# =========================

with st.expander("📊 Financial Indicators Charts"):

    st.subheader("Net Profit")
    st.image("Screenshot 2026-04-26 043008.png")

    st.subheader("Assets")
    st.image("Screenshot 2026-04-26 045020.png")

    st.subheader("ROA")
    st.image("Screenshot 2026-04-26 050316.png")

    st.subheader("ROE")
    st.image("Screenshot 2026-04-26 053321.png")

# =========================
# الشات
# =========================

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل القديمة

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال سؤال جديد

prompt = st.chat_input("Ask anything about the project...")

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # =========================
    # Search داخل الـ PDF
    # =========================

    search_result = ""

    lower_prompt = prompt.lower()

    keywords = lower_prompt.split()

    for line in pdf_text.split("\n"):

        line_lower = line.lower()

        if any(word in line_lower for word in keywords):
            search_result += line + "\n"

    if len(search_result) > 4000:
        search_result = search_result[:4000]

    # =========================
    # Prompt النهائي
    # =========================

    final_prompt = f"""

You are Nexora Hub AI.

You are an AI assistant specialized in explaining
a blockchain financial analysis research project.

Answer in Arabic or English depending on user language.

The user may ask in:
- Arabic
- English
- Egyptian Arabic slang

Answer naturally and clearly.

PROJECT PDF CONTENT:
{search_result}

FINANCIAL INDICATORS DATA:
{indicators_data}

USER QUESTION:
{prompt}

"""

    # =========================
    # Gemini Response
    # =========================

    response = model.generate_content(final_prompt)

    answer = response.text

    # =========================
    # عرض الصور حسب السؤال
    # =========================

    if "profit" in lower_prompt or "صافي الربح" in lower_prompt:
        st.image("Screenshot 2026-04-26 043008.png")

    if "assets" in lower_prompt or "الأصول" in lower_prompt:
        st.image("Screenshot 2026-04-26 045020.png")

    if "roa" in lower_prompt or "العائد على الأصول" in lower_prompt:
        st.image("Screenshot 2026-04-26 050316.png")

    if "roe" in lower_prompt or "حقوق الملكية" in lower_prompt:
        st.image("Screenshot 2026-04-26 053321.png")

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.markdown(answer)
