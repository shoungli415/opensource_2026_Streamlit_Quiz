import streamlit as st


def inject_custom_css():
    st.markdown(
        """
        <style>
        @import url(
            'https://fonts.googleapis.com/css2?family=Song+Myung'
            '&display=swap'
        );
        @import url(
            'https://fonts.googleapis.com/css2?family=Nanum+Myeongjo'
            ':wght@700;800&display=swap'
        );

        /* 메인 배경 설정 */
        .main {
            background-color: #ffffff;
        }

        /* 전체 컨테이너 */
        .exam-container {
            max-width: 650px;
            margin: 0 auto;
            padding-top: 50px;
            font-family: 'Song Myung', serif;
            color: #333;
            background-color: transparent;
        }

        /* 제 1교시 배지 */
        .badge-container {
            text-align: center;
            margin-bottom: 30px;
        }

        .period-badge {
            border: 1px solid #333;
            border-radius: 30px;
            padding: 4px 30px;
            display: inline-block;
            font-size: 1.2rem;
            background-color: white;
        }

        /* 제목 섹션 */
        .exam-header {
            text-align: center;
            margin-bottom: 40px;
        }

        .exam-year {
            font-size: 1.4rem;
            margin-bottom: 10px;
            color: #444;
        }

        .exam-title {
            font-family: 'Nanum Myeongjo', serif;
            font-size: 4.5rem;
            font-weight: 800;
            margin: 10px 0;
            letter-spacing: -2px;
        }

        /* 성명/수험번호 섹션 */
        .info-row {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 40px;
        }

        .info-box {
            display: flex;
            border: 1px solid #333;
            height: 40px;
            align-items: center;
        }

        .label {
            background-color: #bcbcbc;
            width: 80px;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            border-right: 1px solid #333;
        }

        .value {
            width: 160px;
            padding-left: 10px;
        }

        /* 유의사항 박스 */
        .instruction-box {
            border: 1px solid #333;
            padding: 25px 40px;
            margin-bottom: 20px;
            font-size: 1rem;
            line-height: 2;
            text-align: left;
        }

        .instruction-box ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .instruction-box li::before {
            content: "○ ";
        }

        /* 하단 회색 강조 바 */
        .gray-banner {
            background-color: #d9d9d9;
            border: 1px solid #333;
            padding: 15px;
            text-align: center;
            font-weight: bold;
            font-size: 1rem;
        }

        /* 하단 푸터 */
        .footer-logo {
            margin-top: 50px;
            text-align: center;
            font-size: 1.1rem;
        }

        /* ============================= */
        /* 사이드바 전체 */
        /* ============================= */

        section[data-testid="stSidebar"] {
            background-color: #f1f3f6;
        }

        section[data-testid="stSidebar"] > div {
            padding-left: 24px;
            padding-right: 24px;
        }

        section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
            width: 100%;
        }

        /* ============================= */
        /* 전형 선택 라디오 */
        /* ============================= */

        section[data-testid="stSidebar"] div[data-testid="stRadio"] {
            width: 100%;
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] {
            width: 100%;
            gap: 8px;
        }

        /* 라디오 동그라미 숨기기 */
        section[data-testid="stSidebar"] div[role="radiogroup"] \
        label > div:first-child {
            display: none;
        }

        /* 객관식/주관식 항목: 전체 답안 제출 버튼과 같은 너비 */
        section[data-testid="stSidebar"] div[role="radiogroup"] label {
            width: 100%;
            min-height: 46px;
            box-sizing: border-box;
            background-color: transparent;
            border-radius: 14px;
            padding: 11px 18px;
            margin-bottom: 8px;
            cursor: pointer;
            transition: background-color 0.2s ease;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] label p {
            font-size: 15px;
            color: #222;
            margin: 0;
            text-align: center;
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
            background-color: #e9eaec;
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] \
        label:has(input:checked) {
            background-color: #dfe3e8;
            font-weight: 700;
        }

        section[data-testid="stSidebar"] div[role="radiogroup"] \
        label:has(input:checked) p {
            font-weight: 700;
            color: #111;
        }

        /* ============================= */
        /* 사이드바 버튼 기본값 */
        /* ============================= */

        section[data-testid="stSidebar"] div[data-testid="stButton"] {
            width: 100%;
        }

        section[data-testid="stSidebar"] div[data-testid="stButton"] button {
            width: 100%;
            min-height: 44px;
            border-radius: 8px;
        }

        /* ============================= */
        /* 로그아웃 버튼만 아래로 보내기 */
        /* ============================= */

        /*
           Streamlit에서 사이드바 버튼이 여러 개 있을 때,
           마지막 버튼을 로그아웃으로 사용하는 구조 기준입니다.
           app.py에서 반드시 전체 답안 제출 버튼 다음에 로그아웃 버튼을 두세요.
        */

        section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] \
        > div:has(button):last-child {
            position: fixed;
            left: 24px;
            bottom: 28px;
            width: auto !important;
            z-index: 999;
        }

        section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] \
        > div:has(button):last-child div[data-testid="stButton"] {
            width: auto !important;
        }

        section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] \
        > div:has(button):last-child button {
            width: auto !important;
            min-height: auto !important;
            background-color: transparent !important;
            border: none !important;
            box-shadow: none !important;
            padding: 0 !important;
            color: #333 !important;
            font-size: 15px !important;
            font-weight: 500 !important;
        }

        section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] \
        > div:has(button):last-child button:hover {
            background-color: transparent !important;
            border: none !important;
            color: #000 !important;
            text-decoration: underline;
        }

        section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] \
        > div:has(button):last-child button:focus {
            box-shadow: none !important;
            border: none !important;
            outline: none !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
