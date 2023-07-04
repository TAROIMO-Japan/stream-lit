import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time 

st.title("Streamlit 超入門")

# st.write("DataFrame")

# st.write("Display Image")

st.write("プログレスバーの表示")
"start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

"Done!!!!"

# left_column, right_column = st.columns(2) #Betaは不要
# button = left_column.button("右カラムに文字を表示")
# if button:
#     right_column.write("ここは右カラム")

# expander = st.expander("問い合わせ") #Betaは不要
# expander.write("問い合わせ内容を書く")

# option =  st.text_input("あなたの趣味を教えてください。")
# #あなたの趣味は、", option, "です。"

# condition = st.slider("あなたの今の調子は？", 0, 100, 50)
# 'コンディション:', condition

# if st.checkbox("Show Image"):
#     img = Image.open(r"C:\Users\tarok\OneDrive\Pictures\Camera Roll\FWS02 - WIN_20160206_122120.JPG")
#     st.image(img, caption="Taro", use_column_width=True)

# option =  st.selectbox(
#     "あなたの好きな数字を教えてください",
#     list(range(1, 11))
#     )
# "あなたの好きな数字は、", option, "です。"

# df = pd.DataFrame({
#     "1列目": [1, 2, 3, 4],
#     "2列目": [10, 20, 30, 40]
#     })

# st.write(df)

# st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)

# st.table(df.style.highlight_max(axis=0))

# """
# # 章  
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """

# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a', 'b', 'c']
#     )

# st.line_chart(df)

# st.area_chart(df)

# st.bar_chart(df)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
#     )

# st.map(df)