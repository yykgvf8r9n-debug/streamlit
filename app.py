import streamlit as st
import pandas as pd
import numpy as np

st.title("my first stramlit app")

st.write("here is our first attempt at using data to create a table")
st.write(pd.DataFrame({
    'first column' : [1, 2, 3, 4],
    'second column' : [10, 20, 30, 40]
}))

st.write("Streamlit supports a wide range of data visualizations, including [Plotly, Altair, and Bokeh charts](https://docs.streamlit.io/develop/api-reference/charts). 📊 And with over 20 input widgets, you can easily make your data interactive!")

all_users = ["Alice", "Bob", "Charly"]
with st.container(border=True):
    users = st.multiselect("Users", all_users, default=all_users)
    rolling_average = st.toggle("Rolling average")

np.random.seed(42)
data = pd.DataFrame(np.random.randn(20, len(users)), columns=users)
if rolling_average:
    data = data.rolling(7).mean().dropna()

tab1, tab2 = st.tabs(["Chart", "Dataframe"])
tab1.line_chart(data, height=250)
tab2.dataframe(data, height=250, use_container_width=True)

st.set_page_config(layout="wide", page_title="Streamlit 데이터 편집 예제")

st.title("🛠️ 고급 데이터프레임 및 편집")
st.write("다양한 데이터 유형을 표시하고, 사용자가 웹에서 직접 데이터를 수정할 수 있습니다.")


num_rows = st.slider("Number of rows", 1, 1000, 50, help="생성할 데이터프레임의 행 수를 선택하세요.")

np.random.seed(42)
data = []

for i in range(num_rows):
    data.append(
        {
            "Preview": f"https://picsum.photos/400/200?lock={i}",
            "Views": np.random.randint(0, 1000), 
            "Active": np.random.choice([True, False]),
            "Category": np.random.choice(["✨ LLM", "📊 Data", "🛠️ Tool"]),
            "Progress": np.random.randint(1, 100), 
        }
    )

df = pd.DataFrame(data)

config = {
    "Preview": st.column_config.ImageColumn(label="Preview"),
    "Progress": st.column_config.ProgressColumn(
        label="Progress", 
        format="%d %%", 
        min_value=0, 
        max_value=100
    ),
    "Views": st.column_config.NumberColumn("Views", format="%.0f"),
}

enable_editing = st.toggle("Enable editing", help="활성화 시 데이터를 직접 수정할 수 있습니다.")

if enable_editing:
    edited_data = st.data_editor(
        df,
        column_config=config,
        use_container_width=True, 
    )
    st.caption("✨ 데이터를 수정했습니다!")
    
else:
    st.dataframe(
        df,
        column_config=config,
        use_container_width=True
    )


