import streamlit as st
import numpy as np
import pandas as pd

# =============== 스타일 ===============
st.markdown("""
<style>
.card {
    background-color: #FFFFFF;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.06);
    margin-bottom: 22px;
}
</style>
""", unsafe_allow_html=True)

st.title("📈 스트레스 지수 예측")
st.caption("차분한 무채색 UI 기반의 경량 예측 모델")

# ---------- 예측 함수 ----------
def predict_tomorrow(last_seq):
    return np.mean(last_seq)

def predict_week(last_seq):
    preds = []
    seq = last_seq.copy()
    for _ in range(7):
        tomorrow = np.mean(seq)
        preds.append(tomorrow)
        seq = np.append(seq[1:], tomorrow)
    return preds

# ---------- 입력 ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📥 최근 7일 자율신경활성도 입력")
user_input = st.text_input("예: 50,52,55,53,51,49,50", "")

if st.button("예측하기"):
    try:
        last_seq = np.array(list(map(float, user_input.split(","))))
        if len(last_seq) != 7:
            st.error("정확히 7개의 값을 입력해야 합니다!")
        else:
            tomorrow = predict_tomorrow(last_seq)
            week = predict_week(last_seq)

            st.success(f"🎯 내일 예측 스트레스 지수: {tomorrow:.2f}")

            df_week = pd.DataFrame({
                "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                "Predicted Stress": week
            })
            st.line_chart(df_week)

    except:
        st.error("입력 형식이 올바르지 않습니다!")

st.markdown("</div>", unsafe_allow_html=True)
