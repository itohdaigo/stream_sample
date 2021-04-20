import streamlit as st#これで、streamlitをインポートする
import time

st.title('Streamlit 入門')
st.write('プログレスバーの表示')
'Start !!'

latest_iteration = st.empty()#barの上に記載しているので、文字がバーの上に出る
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Itration{i+1}')#プログレスバーの所に表示する文字
    bar.progress(i + 1)
    time.sleep(0.1)#0.1秒止まって次の処理に移動。これがないとすぐ終わってしまう。

'DONE!!!'

left_column,right_column = st.beta_columns(2)#2カラム分の表示をする
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')
