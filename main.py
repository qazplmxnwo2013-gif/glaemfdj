import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 포켓몬 & 직업 추천",
    page_icon="🔮",
    layout="centered"
)

# MBTI별 포켓몬, 성향, 추천 직업 데이터 세팅
# (이미지는 깨지지 않는 PokeAPI 공식 고화질 아트워크 URL 사용)
mbti_data = {
    "ISTJ": {"poke": "꼬부기 🐢", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/7.png", "desc": "책임감이 강하고 묵묵히 제 할 일을 해내는 듬직한 성향!", "jobs": ["📊 공인회계사", "🛡️ 데이터베이스 관리자", "📋 감정평가사"]},
    "ISFJ": {"poke": "이상해씨 🌿", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png", "desc": "주변 사람들을 세심하게 챙기고 배려하는 따뜻한 성향!", "jobs": ["🩺 간호사", "🧸 유치원 교사", "🤝 사회복지사"]},
    "INFJ": {"poke": "가디안 🔮", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png", "desc": "통찰력이 뛰어나고 사람들에게 영감을 주는 신비로운 성향!", "jobs": ["🛋️ 심리상담사", "✍️ 소설가/작가", "🎨 아트 디렉터"]},
    "INTJ": {"poke": "뮤츠 🧬", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png", "desc": "전체적인 흐름을 읽고 완벽한 계획을 세우는 전략가!", "jobs": ["💻 데이터 과학자", "📈 경영 컨설턴트", "🏛️ 건축가"]},
    "ISTP": {"poke": "나무지기 🦎", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/252.png", "desc": "상황 적응력이 뛰어나고 효율적인 해결책을 찾는 만능 재주꾼!", "jobs": ["⌨️ 소프트웨어 개발자", "🔧 항공기 정비사", "🚑 응급구조사"]},
    "ISFP": {"poke": "토게피 🥚", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/175.png", "desc": "온화하고 예술적인 감각이 뛰어난 자유로운 영혼!", "jobs": ["🖌️ 일러스트레이터", "💐 플로리스트", "👗 패션 디자이너"]},
    "INFP": {"poke": "메타몽 💧", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/132.png", "desc": "상상력이 풍부하고 타인의 감정에 깊이 공감하는 몽상가!", "jobs": ["🎬 애니메이터", "healing 미술 치료사", "📚 동화작가"]},
    "INTP": {"poke": "후딘 🥄", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png", "desc": "지적 호기심이 넘치고 논리적인 분석을 즐기는 천재형!", "jobs": ["🎓 대학교수/연구원", "로봇공학자", "🤔 철학자"]},
    "ESTP": {"poke": "피카츄 ⚡", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png", "desc": "에너지가 넘치고 언제나 스릴과 모험을 즐기는 활동가!", "jobs": ["🚒 소방관", "🏃 스포츠 에이전트", "💼 스타트업 창업가"]},
    "ESFP": {"poke": "푸린 🎤", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png", "desc": "분위기 메이커! 사람들의 이목을 끄는 타고난 엔터테이너!", "jobs": ["⭐ 연예인/방송인", "🎉 파티 플래너", "🏄 레크리에이션 강사"]},
    "ENFP": {"poke": "이브이 🦊", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png", "desc": "무한한 잠재력! 호기심 많고 열정적인 아이디어 뱅크!", "jobs": ["📹 크리에이터 (유튜버)", "💡 카피라이터", "🎪 이벤트 기획자"]},
    "ENTP": {"poke": "팬텀 👻", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png", "desc": "틀을 깨는 기발한 생각과 논리적인 달변을 자랑하는 발명가!", "jobs": ["⚙️ 제품 발명가", "💰 벤처 캐피탈리스트", "🎙️ 정치인"]},
    "ESTJ": {"poke": "리자몽 🔥", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png", "desc": "불타는 리더십! 체계적으로 목표를 달성해 내는 타고난 보스!", "jobs": ["🏢 기업 임원(경영자)", "⚖️ 판사", "📅 프로젝트 매니저"]},
    "ESFJ": {"poke": "럭키 🥚", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/113.png", "desc": "친절과 배려의 아이콘! 모두가 의지하는 든든한 서포터!", "jobs": ["🏨 호텔 지배인", "인사(HR) 담당자", "🏫 초등학교 교사"]},
    "ENFJ": {"poke": "망나뇽 🐉", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/149.png", "desc": "부드러운 카리스마! 사람들의 성장을 돕는 열정적인 멘토!", "jobs": ["📢 홍보(PR) 전문가", "🤝 기업 교육 강사", "🌍 시민단체 활동가"]},
    "ENTJ": {"poke": "루카리오 🐺", "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png", "desc": "강력한 추진력과 결단력으로 팀을 이끄는 카리스마 리더!", "jobs": ["👑 최고경영자(CEO)", "변호사", "체스/e스포츠 감독"]}
}

# --- 메인 화면 UI ---
st.title("✨ 나의 MBTI와 찰떡인 포켓몬은? 🐾")
st.markdown("나의 **MBTI**를 선택하고, 나와 쏙 빼닮은 포켓몬과 **가장 잘 어울리는 직업 3가지**를 알아보세요!")
st.divider()

# MBTI 선택 드롭다운
mbti_list = list(mbti_data.keys())
selected_mbti = st.selectbox("👉 당신의 MBTI를 선택해주세요!", ["선택하세요..."] + mbti_list)

# 결과 보기 버튼
if selected_mbti != "선택하세요...":
    if st.button("결과 확인하기 🚀"):
        
        # 시각적 흥미: 버튼 클릭 시 풍선이 날아오르는 효과
        st.balloons()
        
        # 선택된 데이터 가져오기
        data = mbti_data[selected_mbti]
        
        st.divider()
        st.subheader(f"🎉 당신과 찰떡인 포켓몬은 **{data['poke']}**!")
        st.info(data['desc'])
        
        # 2단 레이아웃 (좌: 포켓몬 이미지, 우: 직업 추천)
        col1, col2 = st.columns([1, 1.5])
        
        with col1:
            # 포켓몬 이미지 출력 (외부 라이브러리 없이 URL 직결)
            st.image(data["url"], use_column_width=True)
            
        with col2:
            st.markdown("### 💼 추천 직업 TOP 3")
            st.markdown(f"**1.** {data['jobs'][0]}")
            st.markdown(f"**2.** {data['jobs'][1]}")
            st.markdown(f"**3.** {data['jobs'][2]}")
            
            st.success("새로운 분야에 도전하기 딱 좋은 성향이네요! 응원합니다. 💪")
