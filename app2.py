

import streamlit as st
import pandas as pd

# تغيير الخلفية إلى اللون الأسود باستخدام CSS
st.markdown(
    """
    <style>
    body {
        background-color: #0d1117; /* خلفية سوداء مثل GitHub */
        margin: 0; /* إزالة المساحة الفارغة */
        padding: 0; /* إزالة المساحة الفارغة */
    }
    .stApp {
        background-color: #0d1117; /* خلفية سوداء لمحتوى التطبيق */
        color: white; /* لون النص */
        min-height: 100vh; /* ضمان تغطية الشاشة بالكامل */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# عنوان التطبيق القديم
st.title('Enhanced Streamlit App')

# عنوان التطبيق الجديد
st.markdown("<h2 style='color: lightblue;'>Climate Change Awareness Hub</h2>", unsafe_allow_html=True)

# عرض الصورة الثلاثية الأبعاد الأول
st.components.v1.html(
    """
    <script type="module" src="https://unpkg.com/@splinetool/viewer@1.9.27/build/spline-viewer.js"></script>
    <spline-viewer url="https://prod.spline.design/64CRHkUkB9DAnFZV/scene.splinecode"></spline-viewer>
    """,
    height=600
)

# عرض النص الترحيبي
st.write('Welcome to the Climate Change Awareness Hub! Explore the impact of climate change and how we can make a difference.')

# عرض الصور
st.image('newplot.png', caption='First Plot Image', use_column_width=True)
st.image('newplot2.png', caption='New Plot Image', use_column_width=True)

# قراءة البيانات من ملف CSV
data = pd.read_csv('climate data.csv')
st.write("Data from climate data:")
st.dataframe(data)

# عرض النموذج الثلاثي الأبعاد الثاني
st.components.v1.html(
    """
    <script type="module" src="https://unpkg.com/@splinetool/viewer@1.9.27/build/spline-viewer.js"></script>
    <spline-viewer url="https://prod.spline.design/mI5B1O6hZJk21uic/scene.splinecode"></spline-viewer>
    """,
    height=600
)

# عرض النموذج الثلاثي الأبعاد الجديد بدلاً من الثالث
st.components.v1.html(
    """
    <script type="module" src="https://unpkg.com/@splinetool/viewer@1.9.27/build/spline-viewer.js"></script>
    <spline-viewer url="https://prod.spline.design/1vDTiLR4iZG1lozC/scene.splinecode"></spline-viewer>
    """,
    height=600
)

# عرض النموذج الثلاثي الأبعاد الرابع (النموذج الجديد)
st.components.v1.html(
    """
    <script type="module" src="https://unpkg.com/@splinetool/viewer@1.9.27/build/spline-viewer.js"></script>
    <spline-viewer url="https://prod.spline.design/rrFC8EVFFlqhXMgm/scene.splinecode"></spline-viewer>
    """,
    height=600
)

# عرض النموذج الثلاثي الأبعاد الخامس كخلفية
st.components.v1.html(
    """
    <script type="module" src="https://unpkg.com/@splinetool/viewer@1.9.27/build/spline-viewer.js"></script>
    <spline-viewer url="https://prod.spline.design/VcwI1f3jUR388pow/scene.splinecode" style="position: fixed; width: 100vw; height: 100vh; top: 0; left: 0; z-index: -1;"></spline-viewer>
    """,
    height=600
)

# إضافة المقال
st.write("### Climate Change and Global Warming")
st.write("""
Climate change refers to long-term shifts in temperatures and weather patterns, primarily caused by human activities such as burning fossil fuels, deforestation, and industrial processes. These activities release greenhouse gases into the atmosphere, which trap heat and lead to global warming.

Global warming is the increase in Earth's average surface temperature due to rising levels of greenhouse gases. This phenomenon is associated with severe weather events, rising sea levels, and changes in wildlife populations and habitats.

Addressing climate change requires global cooperation and commitment to reduce emissions, adopt renewable energy sources, and protect natural ecosystems. Awareness and education play a crucial role in this effort, as individuals and communities can contribute to sustainable practices.
""")

# واجهة الدردشة
st.write("### Chatbot (Interactive Version)")

# متغير للتحكم في إظهار الدردشة
if 'chat_visible' not in st.session_state:
    st.session_state.chat_visible = True

if st.session_state.chat_visible:
    options = ["Environmental Conservation", "Climate Change", "Pollution", "Global Warming"]
    selected_option = st.selectbox("Choose a topic:", options)

    # معلومات عن الموضوع المختار
    if selected_option:
        if selected_option == "Environmental Conservation":
            st.write("Here's some information about environmental conservation.")
            st.write("For more details, you can refer to:")
            st.write("- [Wikipedia: Environmental Conservation](https://en.wikipedia.org/wiki/Environmental_conservation)")
        elif selected_option == "Climate Change":
            st.write("Climate change is a significant global challenge affecting us all.")
            st.write("For more information, check:")
            st.write("- [Wikipedia: Climate Change](https://en.wikipedia.org/wiki/Climate_change)")
        elif selected_option == "Pollution":
            st.write("Pollution is harmful to our health and the environment.")
            st.write("Learn more here:")
            st.write("- [Wikipedia: Pollution](https://en.wikipedia.org/wiki/Pollution)")
        elif selected_option == "Global Warming":
            st.write("Global warming refers to the long-term heating of Earth’s climate system.")
            st.write("For additional resources, visit:")
            st.write("- [Wikipedia: Global Warming](https://en.wikipedia.org/wiki/Global_warming)")

    # زر لإغلاق المحادثة
    if st.button("Close Chat"):
        st.session_state.chat_visible = False
else:
    if st.button("Open Chat"):
        st.session_state.chat_visible = True

# إضافة زر "Contact Us" و "Learn More" مع أيقونة GitHub تحت واجهة الدردشة
st.markdown(
    """
    <div style="text-align:center; margin-top:10px;">
        <a href="mailto:contact@example.com" style="color:white; margin-right: 15px; text-decoration: none; font-size:18px;">Contact Us</a>
        <a href="https://en.wikipedia.org/wiki/Climate_change" target="_blank" style="color:white; margin-right: 15px; text-decoration: none; font-size:18px;">Learn More</a>
        <a href="https://github.com/climate-change" target="_blank">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" style="width:30px; vertical-align:middle;">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
