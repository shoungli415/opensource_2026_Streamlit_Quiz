import streamlit as st
from data_provider import get_quiz_questions, get_short_answer_questions


def login_view():
    """상단 박스를 제거한 깔끔한 시험지 표지"""
    # 전체 감싸는 컨테이너 시작
    st.markdown('<div class="exam-container">', unsafe_allow_html=True)

    # 1. 제 1교시 배지
    st.markdown(
        '<div class="badge-container"><div class="period-badge">'
        '제 1교시</div></div>',
        unsafe_allow_html=True
    )

    # 2. 메인 제목
    st.markdown("""
        <div class="exam-header">
            <div class="exam-year">2026학년도 게임능력시험 문제지</div>
            <div class="exam-title">배틀그라운드 영역</div>
        </div>
    """, unsafe_allow_html=True)

    # 3. 성명/수험번호 칸 (이미지 스타일)
    st.markdown(
        """
        <div class="info-row">
            <div class="info-box">
                <div class="label">성 명</div>
                <div class="value"> 이은송</div>
            </div>
            <div class="info-box">
                <div class="label">학 번</div>
                <div class="value"> 2023204045</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 4. 유의사항 및 배너
    st.markdown("""
        <div class="instruction-box">
            <ul>
                <li>문제를 풀기 전, 본인의 성명과 학번을 정확히 작성했는지 확인하십시오.</li>
                <li>모든 문항은 배틀그라운드 게임의 요소를 바탕으로 출제되었습니다.</li>
                <li>문제를 읽고 가장 적절하다고 생각되는 답을 선택하거나 작성하십시오.</li>
                <li>실제 게임 경험과 다를 수 있으므로, 문제에서 제시한 상황과 조건을 기준으로 판단하십시오.</li>
                <li>답안 작성 시 줄임말이나 비속어 사용은 지양하고, 가능한 한 명확하게 작성하십시오.</li>
            </ul>
        </div>
        <div class="gray-banner">
            ※ 본 시험은 오픈소스소프트웨어 실습의 중간고사 대체 과제입니다.
        </div>
    """, unsafe_allow_html=True)

    # 5. 푸터
    st.markdown("""
        <div class="footer-logo">
            출제위원회 / <b style="font-size:1.3rem;"> 이은송</b>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # 컨테이너 끝

    # --- 실제 로그인 입력 (하단 배치) ---
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        user_id = st.text_input(
            "성명 (ID: admin)", placeholder="이름 입력"
        )
    with col2:
        user_pw = st.text_input(
            "수험번호 (PW: 1234)",
            type="password",
            placeholder="번호 입력"
        )

    if st.button("시험장 입장", use_container_width=True):
        if user_id == "admin" and user_pw == "1234":
            st.session_state.logged_in = True
            st.session_state.need_scroll_top = True
            st.rerun()
        else:
            st.error("정보가 일치하지 않습니다.")


def quiz_view():
    questions = get_quiz_questions()

    st.markdown('<div class="exam-container">', unsafe_allow_html=True)
    st.markdown(
        '<div class="exam-header"><div class="exam-title" '
        'style="font-size:2.5rem;">배틀그라운드 영역 '
        '(객관식)</div></div>',
        unsafe_allow_html=True
    )

    with st.container(border=True):
        for i, q in enumerate(questions):
            st.write(f"**【문항 {i+1}】** {q['question']}")

            saved_choice = st.session_state.get(f"mc_answer_{i}", None)

            if saved_choice in q["options"]:
                default_index = q["options"].index(saved_choice)
            else:
                default_index = None

            choice = st.radio(
                label=f"문항 {i+1} 답안 선택",
                options=q["options"],
                key=f"_mc_{i}",
                index=default_index,
                label_visibility="collapsed"
            )

            # 위젯 값과 별도로 답안을 영구 저장
            if choice is not None:
                st.session_state[f"mc_answer_{i}"] = choice
                selected_number = q["options"].index(choice) + 1
                st.markdown(f"**선택한 답 : {selected_number}번**")

            st.write("---")

    st.markdown('</div>', unsafe_allow_html=True)


def short_quiz_view():
    questions = get_short_answer_questions()

    st.markdown('<div class="exam-container">', unsafe_allow_html=True)
    st.markdown(
        '<div class="exam-header"><div class="exam-title" '
        'style="font-size:2.5rem;">배틀그라운드 영역 '
        '(주관식)</div></div>',
        unsafe_allow_html=True
    )

    with st.container(border=True):
        for i, q in enumerate(questions):
            st.write(f"**【주관식 {i+1}】** {q['question']}")

            saved_answer = st.session_state.get(f"sa_answer_{i}", "")

            ans = st.text_input(
                label=f"주관식 {i+1} 답안 입력",
                key=f"_sa_{i}",
                value=saved_answer,
                placeholder="답안을 입력하세요",
                label_visibility="collapsed"
            )

            # 위젯 값과 별도로 답안을 영구 저장
            st.session_state[f"sa_answer_{i}"] = ans.strip()

            st.write("---")

    st.markdown('</div>', unsafe_allow_html=True)
