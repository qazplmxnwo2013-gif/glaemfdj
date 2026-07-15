import streamlit as st
import pandas as pd
import time

# 1. 페이지 기본 설정 및 타이틀
st.set_page_config(
    page_title="MBTI 소설 매칭 연구소",
    page_icon="📚",
    layout="centered"
)

# 헤더 부분 효과
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🔮 MBTI 맞춤형 소설 추천 연구소</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>당신의 MBTI 성향을 분석하여 딱 맞는 소설 장르와 역대 베스트셀러를 매칭해 드립니다.</p>", unsafe_allow_html=True)
st.markdown("---")

# 2. MBTI 및 추천 데이터 정의 (제공해주신 데이터셋의 실제 베스트셀러 반영)
mbti_recommendations = {
    # 분석가형 (NT)
    "INTJ": {
        "title": "🧠 이성적 전략가 (INTJ)를 위한 추천",
        "genres": [
            {"name": "SF / 과학 소설", "desc": "거대한 세계관과 치밀한 과학적 논리를 즐기는 당신", "book": "The Martian (앤디 위어)", "detail": "화성에 홀로 남겨진 우주비행사의 생존기로 과학적 개연성이 돋보이는 작품"},
            {"name": "스릴러 / 미스터리", "desc": "사건의 실마리를 추적하며 두뇌 싸움을 벌이는 장르", "book": "Gone Girl (길리언 플린)", "detail": "치밀한 반전과 인간 심리의 바닥을 보여주는 추리 스릴러 명작"},
            {"name": "디스토피아", "desc": "통제된 사회 구조와 시스템적 모순을 파헤치는 이야기", "book": "The Hunger Games (수잔 콜린스)", "detail": "생존을 위한 치밀한 전략과 거대한 체제에 맞서는 SF 디스토피아"}
        ]
    },
    "INTP": {
        "title": "💡 호기심 많은 사색가 (INTP)를 위한 추천",
        "genres": [
            {"name": "하드 SF", "desc": "우주적 스케일과 독창적인 상상력을 자극하는 소설", "book": "The Martian (앤디 위어)", "detail": "철저한 고증과 이과적 유머가 결합된 최고의 하드 SF"},
            {"name": "심리 스릴러", "desc": "인간 심리의 심층적인 퍼즐을 맞추는 이야기", "book": "The Girl on the Train (폴라 호킨스)", "detail": "기억의 파편을 맞춰나가는 고도의 심리 추리극"},
            {"name": "다크 판타지", "desc": "독창적이고 방대한 법칙이 존재하는 이세계 이야기", "book": "Harry Potter Box Set (J.K. 롤링)", "detail": "치밀하게 짜인 마법 세계관의 절대적인 기준점"}
        ]
    },
    "ENTJ": {
        "title": "👑 대담한 통솔자 (ENTJ)를 위한 추천",
        "genres": [
            {"name": "정치 / 사회 스릴러", "desc": "권력 투쟁과 거대한 스케일의 음모론을 다룬 소설", "book": "The Lost Symbol (댄 브라운)", "detail": "역사적 비밀 조직과 상징을 파헤치는 숨막히는 지적 추적극"},
            {"name": "생존 / 디스토피아", "desc": "위기 속에서 리더십을 발휘하고 살아남는 이야기", "book": "The Hunger Games (수잔 콜린스)", "detail": "시스템의 허점을 뚫고 혁명을 이끄는 주인공의 대서사시"},
            {"name": "고전 문학 / 서사시", "desc": "인간 군상의 야망과 사회적 성공을 통찰하는 작품", "book": "The Great Gatsby (F. 스콧 피츠제럴드)", "detail": "화려한 재력 뒤에 숨겨진 인간의 야망과 상실을 그린 고전"}
        ]
    },
    "ENTP": {
        "title": "⚡ 뜨거운 논쟁을 즐기는 변론가 (ENTP)를 위한 추천",
        "genres": [
            {"name": "풍자 / 블랙 코미디", "desc": "틀에 박힌 관습을 깨부수는 위트 있는 소설", "book": "The Help (캐스린 스톡킷)", "detail": "유쾌하면서도 묵직하게 사회적 편견을 꼬집는 명작"},
            {"name": "모험 / SF 스릴러", "desc": "예측 불가능한 상황에서 번뜩이는 재치로 헤쳐 나가는 이야기", "book": "The Martian (앤디 위어)", "detail": "절망적인 상황에서도 유머와 임기응변으로 생존하는 주인공의 매력"},
            {"name": "미스터리 스릴러", "desc": "작가와 독자가 치열한 두뇌 밀당을 벌이는 반전극", "book": "Gone Girl (길리언 플린)", "detail": "기존 관념을 뒤흔드는 통쾌하고도 충격적인 반전 소설"}
        ]
    },
    # 외교관형 (NF)
    "INFJ": {
        "title": "🔮 선의의 옹호자 (INFJ)를 위한 추천",
        "genres": [
            {"name": "서정적 / 성장 소설", "desc": "내면의 깊은 성장과 윤리적 가치를 탐구하는 장르", "book": "To Kill a Mockingbird (하퍼 리)", "detail": "편견에 맞서 인간 존엄성과 정의를 지키는 따뜻하고 묵직한 서사"},
            {"name": "감성 판타지", "desc": "숨겨진 은유와 인간에 대한 깊은 애정이 녹아있는 이야기", "book": "Harry Potter Box Set (J.K. 롤링)", "detail": "사랑과 희생, 그리고 연대의 힘을 보여주는 최고의 판타지"},
            {"name": "휴먼 드라마", "desc": "서로 다른 이들이 상처를 치유하며 유대감을 쌓아가는 소설", "book": "The Help (캐스린 스톡킷)", "detail": "연대와 용기를 통해 세상의 벽을 허무는 감동적인 이야기"}
        ]
    },
    "INFP": {
        "title": "🌸 열정적인 중재자 (INFP)를 위한 추천",
        "genres": [
            {"name": "서정적 판타지", "desc": "낭만적이고 환상적인 세계에서 자아를 찾는 소설", "book": "Harry Potter Box Set (J.K. 롤링)", "detail": "누구나 한 번쯤 꿈꿔본 마법 같은 세계관과 깊은 감동"},
            {"name": "로맨스 / 감성 소설", "desc": "가슴 아프지만 아름답고 순수한 감수성을 자극하는 장르", "book": "The Fault in Our Stars (존 그린)", "detail": "아픔 속에서도 반짝이는 삶의 의미와 사랑을 그린 눈물샘 자극 소설"},
            {"name": "성장 문학 / 휴머니즘", "desc": "인간의 선함과 깊은 내면의 울림을 주는 따뜻한 소설", "book": "Love You Forever (로버트 먼치)", "detail": "세대를 초월하여 가슴 뭉클한 감동과 위로를 전하는 이야기"}
        ]
    },
    "ENFJ": {
        "title": "🤝 정의로운 사회운동가 (ENFJ)를 위한 추천",
        "genres": [
            {"name": "사회 고발 / 드라마", "desc": "공동체의 변화와 인간성 회복을 부르짖는 소설", "book": "The Help (캐스린 스톡킷)", "detail": "차별에 저항하며 목소리를 내는 사람들의 연대와 감동 실화 기반 소설"},
            {"name": "성장 / 정의", "desc": "올바른 가치관을 향해 나아가는 뜨거운 성장 서사", "book": "To Kill a Mockingbird (하퍼 리)", "detail": "사회의 편견 속에서도 정의와 양심이 무엇인지 깨닫게 하는 책"},
            {"name": "로맨틱 드라마", "desc": "인간 관계 속에서 진정한 헌신과 사랑의 의미를 찾는 이야기", "book": "The Shack (윌리엄 P. 영)", "detail": "상처와 슬픔을 치유하고 용서와 사랑으로 나아가는 깊은 울림"}
        ]
    },
    "ENFP": {
        "title": "✨ 재기발랄한 활동가 (ENFP)를 위한 추천",
        "genres": [
            {"name": "하이 판타지", "desc": "무한한 상상력과 흥미진진한 모험이 가득한 세계", "book": "Harry Potter Box Set (J.K. 롤링)", "detail": "지루할 틈 없는 흥미진진한 마법 모험의 대명사"},
            {"name": "하이틴 / 청춘 로맨스", "desc": "감정에 솔직하고 열정적인 에너지가 넘치는 장르", "book": "The Fault in Our Stars (존 그린)", "detail": "유쾌함과 슬픔을 넘나들며 진정한 삶의 소중함을 일깨워주는 소설"},
            {"name": "휴먼 / 가족 소설", "desc": "주변 사람들과의 따뜻하고 통통 튀는 유대감을 다룬 이야기", "book": "Love You Forever (로버트 먼치)", "detail": "듣기만 해도 마음이 몽글몽글해지는 사랑과 감동의 바이블"}
        ]
    }
}

# 3. UI 구현
mbti_list = list(mbti_recommendations.keys()) + ["ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"]
# 누락된 유형은 INFJ/INFP 등과 유사한 베스트셀러 카테고리로 매칭되도록 자동 보완 처리

selected_mbti = st.selectbox(
    "👉 당신의 MBTI를 선택하세요:",
    mbti_list,
    index=None,
    placeholder="선택하기..."
)

if selected_mbti:
    # 로딩 애니메이션 효과
    with st.spinner('🔮 당신의 성향 파악 중... 소설 세계관을 분석하고 있습니다.'):
        time.sleep(1)
    
    # NT/NF 외의 예외 유형 보완 매칭용 로직
    target_mbti = selected_mbti
    if target_mbti not in mbti_recommendations:
        # 간단한 매칭 규칙 (S 유형들을 성향이 유사한 N 유형의 데이터로 임시 매칭)
        mapping = {"ISTJ": "INTJ", "ISFJ": "INFJ", "ESTJ": "ENTJ", "ESFJ": "ENFJ", "ISTP": "INTP", "ISFP": "INFP", "ESTP": "ENTP", "ESFP": "ENFP"}
        target_mbti = mapping[selected_mbti]
        
    data = mbti_recommendations[target_mbti]
    
    st.balloons() # 매칭 성공 시 풍선 효과!
    
    st.markdown(f"### {data['title']}")
    st.write(f"**{selected_mbti}** 성향의 독자님께 강력 추천하는 장르 Top 3입니다! 🎉")
    
    for idx, g in enumerate(data['genres'], 1):
        with st.container():
            st.markdown(f"#### {idx}. {g['name']}")
            st.caption(f"💡 {g['desc']}")
            
            # 메트릭 박스 형태로 베스트셀러 강조 표시
            st.info(f"🏆 **역대 최고 베스트셀러:** `{g['book']}`\n\n📌 **도서 소개:** {g['detail']}")
            st.markdown("<br>", unsafe_allow_html=True)
            
    st.success("📚 오늘 밤, 이 책 한 권 어떠신가요?")
