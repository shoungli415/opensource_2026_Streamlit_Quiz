import streamlit as st
import streamlit.components.v1 as components
from ui_styles import inject_custom_css
from views import login_view, quiz_view, short_quiz_view
from data_provider import get_quiz_questions, get_short_answer_questions

st.set_page_config(page_title="배틀그라운드 모의고사", layout="centered")
inject_custom_css()


def scroll_to_top():
    components.html(
        """
        <script>
            function forceScrollTop() {
                const doc = window.parent.document;

                // 여러 Streamlit 버전에서 가능한 스크롤 컨테이너 후보들
                const scrollTargets = [
                    window.parent,
                    doc.documentElement,
                    doc.body,
                    doc.querySelector('section.main'),
                    doc.querySelector('.main'),
                    doc.querySelector('[data-testid="stAppViewContainer"]'),
                    doc.querySelector('[data-testid="stMain"]')
                ];

                scrollTargets.forEach((target) => {
                    if (!target) return;

                    try {
                        if (target === window.parent) {
                            target.scrollTo(0, 0);
                        } else {
                            target.scrollTop = 0;
                            target.scrollTo(
                                { top: 0, left: 0, behavior: "auto" }
                            );
                        }
                    } catch (e) {}
                });
            }

            // 페이지가 그려지는 타이밍 차이를 고려해서 여러 번 실행
            forceScrollTop();
            setTimeout(forceScrollTop, 50);
            setTimeout(forceScrollTop, 150);
            setTimeout(forceScrollTop, 300);
            setTimeout(forceScrollTop, 600);
        </script>
        """,
        height=0
    )


# 세션 상태 관리
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "score" not in st.session_state:
    st.session_state.score = 0

if "current_menu" not in st.session_state:
    st.session_state.current_menu = "객관식 전형"

if "wrong_answers" not in st.session_state:
    st.session_state.wrong_answers = []

if "need_scroll_top" not in st.session_state:
    st.session_state.need_scroll_top = False


# 전체 채점 함수
def grade_all_questions():
    quiz_questions = get_quiz_questions()
    short_questions = get_short_answer_questions()

    wrong_count = 0
    wrong_answers = []

    # 객관식 채점
    for i, q in enumerate(quiz_questions):
        user_choice = st.session_state.get(f"mc_answer_{i}", None)

        if user_choice != q["answer"]:
            wrong_count += 1

            wrong_answers.append({
                "type": "객관식",
                "number": i + 1,
                "question": q["question"],
                "user_answer": (
                    user_choice if user_choice is not None else "미선택"
                ),
                "correct_answer": q["answer"]
            })

    # 주관식 채점
    for i, q in enumerate(short_questions):
        user_answer = st.session_state.get(f"sa_answer_{i}", "").strip()

        if user_answer != q["answer"]:
            wrong_count += 1

            wrong_answers.append({
                "type": "주관식",
                "number": i + 1,
                "question": q["question"],
                "user_answer": user_answer if user_answer else "미입력",
                "correct_answer": q["answer"]
            })

    score = 100 - (wrong_count * 10)

    st.session_state.score = score
    st.session_state.wrong_count = wrong_count
    st.session_state.wrong_answers = wrong_answers
    st.session_state.submitted = True


# 로그인 여부 확인
if not st.session_state.logged_in:
    login_view()

else:
    if st.session_state.get("need_scroll_top", False):
        scroll_to_top()
        st.session_state.need_scroll_top = False
    # 사이드바 메뉴
    st.sidebar.markdown("### 🎮 전형 선택")
    st.sidebar.caption("응시할 전형을 선택하세요")

    exam_type = st.sidebar.radio(
        label="전형 선택",
        options=[
            "객관식 전형",
            "주관식 전형"
        ],
        label_visibility="collapsed"
    )

    # 현재 선택한 메뉴 저장
    st.session_state.current_menu = exam_type

    st.sidebar.markdown("---")

    # 전체 답안 제출 버튼
    if st.sidebar.button("전체 답안 제출", use_container_width=True):
        grade_all_questions()
        st.rerun()

    # 로그아웃 버튼
    if st.sidebar.button("로그아웃", key="logout_button"):
        st.session_state.logged_in = False
        st.session_state.submitted = False
        st.session_state.score = 0
        st.rerun()

    # 결과 화면
    if st.session_state.submitted:
        st.markdown(
            f"""
            <div class="exam-container" style="text-align:center;">
                <h1>🎖️ 최종 성적표</h1>
                <hr>
                <p>배틀그라운드 영역 최종 결과</p>
                <h1 style="font-size:4rem; color:#d32f2f;">
                    {st.session_state.score} 점</h1>
                <p>틀린 문제 수 : {st.session_state.wrong_count}개</p>
                <br>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.session_state.wrong_count == 0:
            st.balloons()
            st.success("모든 문제를 맞혔습니다! 완벽합니다.")
        else:
            st.markdown("### 오답 확인")

            for item in st.session_state.wrong_answers:
                st.markdown(
                    f"""
                    <div style="
                        border: 1px solid #ddd;
                        border-radius: 12px;
                        padding: 18px;
                        margin-bottom: 16px;
                        background-color: #ffffff;
                    ">
                        <p><b>[{item['type']} {item['number']}번]
                        </b></p>
                        <p><b>문제</b> : {item['question']}</p>
                        <p style="color:#d32f2f;"><b>내 답</b> :
                            {item['user_answer']}</p>
                        <p style="color:#2e7d32;"><b>정답</b> :
                            {item['correct_answer']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        if st.button("다시 응시하기"):
            st.session_state.submitted = False
            st.session_state.score = 0
            st.session_state.wrong_count = 0
            st.session_state.wrong_answers = []

            for i in range(len(get_quiz_questions())):
                st.session_state.pop(f"mc_answer_{i}", None)
                st.session_state.pop(f"_mc_{i}", None)

            for i in range(len(get_short_answer_questions())):
                st.session_state.pop(f"sa_answer_{i}", None)
                st.session_state.pop(f"_sa_{i}", None)

            st.rerun()

    else:
        # 선택한 전형에 따라 화면 출력
        if exam_type == "객관식 전형":
            quiz_view()

        elif exam_type == "주관식 전형":
            short_quiz_view()
