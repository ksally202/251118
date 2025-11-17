import streamlit as st
import numpy as np
import pandas as pd

# =============================
# 전체 스타일 (무채색 컨셉)
# =============================
st.markdown("""
<style>

@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');

html, body, [class*="css"] {
    font-family: 'Pretendard', sans-serif;
}

body {
    background-color: #F5F5F5;
    color: #333333;
}

/* 카드 */
.card {
    background-color: #FFFFFF;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.06);
    margin-bottom: 22px;
}

/* 프리미엄 카드 */
.premium-card {
    background: rgba(255,255,255,0.35);
    backdrop-filter: blur(10px);
    padding: 25px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.4);
    margin-bottom: 22px;
}

/* 버튼 디자인 */
div.stButton > button {
    background: linear-gradient(to right, #333333, #555555);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 20px;
    font-size: 16px;
    transition: 0.2s ease;
}

div.stButton > button:hover {
    background: linear-gradient(to right, #000000, #333333);
}

</style>
""", unsafe_allow_html=True)


# =============================
# 전체 페이지 구조 시작
# =============================

st.title("🌿 ALL DAY Stress Out")
st.caption("차분한 무채색 기반 헬스케어 · 스트레스 관리 서비스")

# ---------- 기분 선택 ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🙂 오늘의 기분 선택")
mood = st.segmented_control(
    "오늘 기분",
    ["😊 행복", "🙂 보통", "😥 스트레스", "😭 매우 스트레스"]
)
st.write(f"**👉 오늘 기분:** {mood}")
st.markdown("</div>", unsafe_allow_html=True)

# ---------- 오늘 스트레스 ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📊 오늘의 스트레스 지수")
today_stress = np.random.randint(30, 90)
st.metric("스트레스 지수", f"{today_stress}/100")
st.markdown("</div>", unsafe_allow_html=True)

# ---------- 추천 ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🧘 오늘의 스트레스 완화 추천")
st.info("오늘은 따뜻한 샤워나 차분한 음악과 함께 휴식을 취해보는 것을 추천드려요.")
st.video("https://www.youtube.com/watch?v=UBMk30rjy0o")
st.markdown("</div>", unsafe_allow_html=True)

# ---------- 프리미엄 ----------
st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
st.subheader("🔒 Premium — 수면 패턴 분석")
premium = st.checkbox("프리미엄 기능 잠금 해제")

if not premium:
    st.write("프리미엄 구독 시 수면 패턴 분석 기능을 사용할 수 있습니다.")
else:
    sleep_hours = np.random.randint(4, 9, size=7)
    df = pd.DataFrame({"Day": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"], "Sleep": sleep_hours})
    st.bar_chart(df, x="Day", y="Sleep")

st.markdown("</div>", unsafe_allow_html=True)

st.caption("© 2025 ALL DAY Stress Out – Minimal Black & White Theme")
