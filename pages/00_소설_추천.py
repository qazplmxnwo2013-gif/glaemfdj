import streamlit as st
import time

# 1. 페이지 기본 설정 및 타이틀
st.set_page_config(
    page_title="MBTI 소설 매칭 연구소",
    page_icon="📚",
    layout="centered"
)

# 헤더 부분 효과
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🔮 MBTI 맞춤형 소설 추천 연구소</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; font-size: 1.1em;'>당신의 MBTI 성향을 분석하여 딱 맞는 소설 장르와 역대 베스트셀러를 매칭해 드립니다.</p>", unsafe_allow_html=True)
st.markdown("---")

# 2. 16가지 MBTI별 추천 데이터 (아마존 베스트셀러 데이터셋 기반)
mbti_recommendations = {
    # ------------------ 분석가형 (NT) ------------------
    "INTJ": {
        "title": "🧠 이성적 전략가 (INTJ)를 위한 추천",
        "genres": [
            {"name": "SF / 과학 소설", "desc": "치밀한 과학적 논리와 생존 전략을 즐기는 당신", "book": "The Martian (앤디 위어)", "detail": "화성에 홀로 남겨진 우주비행사의 압도적인 생존기"},
            {"name": "스릴러 / 미스터리", "desc": "사건의 실마리를 추적하며 두뇌 싸움을 벌이는 장르", "book": "Gone Girl (길리언 플린)", "detail": "치밀한 반전과 인간 심리의 바닥을 보여주는 추리 명작"},
            {"name": "디스토피아", "desc": "통제된 사회 구조와 모순을 파헤치는 이야기", "book": "The Hunger Games (수잔 콜린스)", "detail": "거대한 체제에 맞서는 치밀한 전략과 SF 생존극"}
        ]
    },
    "INTP": {
        "title": "💡 호기심 많은 사색가 (INTP)를 위한 추천",
        "genres": [
            {"name": "하드 SF", "desc": "지적 호기심과 독창적인 상상력을 자극하는 소설", "book": "The Martian (앤디 위어)", "detail": "철저한 고증과 이과적 유머가 결합된 최고의 하드 SF"},
            {"name": "심리 스릴러", "desc": "파편화된 단서를 모아 진실을 조립하는 퍼즐", "book": "The Girl on the Train (폴라 호킨스)", "detail": "기억의 파편을 맞춰나가는 고도의 심리 추리극"},
            {"name": "정치 / 서사시", "desc": "사회 구조와 인간의 야망을 관찰하는 장르", "book": "The Great Gatsby (F. 스콧 피츠제럴드)", "detail": "인간의 맹목적인 욕망을 날카롭게 해부한 고전"}
        ]
    },
    "ENTJ": {
        "title": "👑 대담한 통솔자 (ENTJ)를 위한 추천",
        "genres": [
            {"name": "생존 / 디스토피아", "desc": "극한의 위기에서 리더십과 전술로 판을 뒤집는 이야기", "book": "The Hunger Games (수잔 콜린스)", "detail": "시스템의 허점을 뚫고 혁명을 이끄는 주인공의 대서사시"},
            {"name": "미스터리 스릴러", "desc": "예상치 못한 변수를 통제하며 진실을 쫓는 장르", "book": "Gone Girl (길리언 플린)", "detail": "완벽해 보이는 통제 이면의 소름 돋는 진실 게임"},
            {"name": "고전 문학", "desc": "인간 군상의 권력과 야망, 성공을 통찰하는 작품", "book": "The Great Gatsby (F. 스콧 피츠제럴드)", "detail": "화려한 재력 뒤에 숨겨진 서늘한 현실 통찰"}
        ]
    },
    "ENTP": {
        "title": "⚡ 뜨거운 논쟁을 즐기는 변론가 (ENTP)를 위한 추천",
        "genres": [
            {"name": "풍자 / 블랙 코미디", "desc": "틀에 박힌 관습과 편견을 깨부수는 위트 있는 소설", "book": "The Help (캐스린 스톡킷)", "detail": "유쾌하면서도 묵직하게 사회의 부조리를 꼬집는 명작"},
            {"name": "모험 / SF 스릴러", "desc": "최악의 상황에서도 유머와 재치로 헤쳐 나가는 이야기", "book": "The Martian (앤디 위어)", "detail": "절망 속에서도 빛나는 임기응변의 정수"},
            {"name": "하이 판타지", "desc": "독창적이고 복잡한 세계관 속에서의 모험", "book": "Harry Potter Box Set (J.K. 롤링)", "detail": "상상력을 자극하는 방대하고 흥미로운 마법 세계"}
        ]
    },
    # ------------------ 외교관형 (NF) ------------------
    "INFJ": {
        "title": "🔮 선의의 옹호자 (INFJ)를 위한 추천",
        "genres": [
            {"name": "성장 / 윤리 소설", "desc": "내면의 깊은 울림과 인류애, 정의를 탐구하는 장르", "book": "To Kill a Mockingbird (하퍼 리)", "detail": "편견에 맞서 인간 존엄성을 지키는 따뜻한 서사"},
            {"name": "감성 판타지", "desc": "숨겨진 은유와 인간에 대한 깊은 애정이 녹아있는 이야기", "book": "Harry Potter Box Set (J.K. 롤링)", "detail": "희생, 사랑, 연대의 힘을 웅장하게 그려낸 마스터피스"},
            {"name": "휴먼 드라마", "desc": "상처입은 이들이 서로를 치유하며 유대감을 쌓는 소설", "book": "The Shack (윌리엄 P. 영)", "detail": "깊은 상실을 넘어 용서와 치유로 나아가는 영적 여정"}
        ]
    },
    "INFP": {
        "title": "🌸 열정적인 중재자 (INFP)를 위한 추천",
        "genres": [
            {"name": "로맨스 / 감성 소설", "desc": "순수하고 깊은 감수성을 자극하는 아련한 장르", "book": "The Fault in Our Stars (존 그린)", "detail": "아픔 속에서도 반짝이는 삶의 의미와 사랑을 그린 소설"},
            {"name": "서정적 판타지", "desc": "현실을 벗어나 낭만적이고 환상적인 세계로의 여행", "book": "Harry Potter Box Set (J.K. 롤링)", "detail": "가슴 한편에 묻어둔 마법 같은 세계관과 깊은 감동"},
            {"name": "성장 문학 / 휴머니즘", "desc": "세상에 대한 따뜻한 시선과 위로를 건네는 이야기", "book": "Love You Forever (로버트 먼치)", "detail": "가슴 뭉클한 모성애와 세대를 잇는 깊은 사랑의 동화"}
        ]
    },
    "ENFJ": {
        "title": "🤝 정의로운 사회운동가 (ENFJ)를 위한 추천",
        "genres": [
            {"name": "사회 고발 / 드라마", "desc": "연대와 희망, 공동체의 긍정적 변화를 이끄는 소설", "book": "The Help (캐스린 스톡킷)", "detail": "차별에 저항하며 목소리를 내는 사람들의 감동 실화 기반 소설"},
            {"name": "성장 / 정의", "desc": "올바른 가치관을 향해 나아가는 뜨거운 성장 서사", "book": "To Kill a Mockingbird (하퍼 리)", "detail": "사회의 편견 속에서도 정의와 양심을 일깨우는 명작"},
            {"name": "로맨틱 드라마", "desc": "인간 관계 속에서 진정한 헌신과 사랑의 의미를 찾는 이야기", "book": "The Shack (윌리엄 P. 영)", "detail": "상처를 치유하고 진정한 관계의 의미를 찾는 이야기"}
        ]
    },
    "ENFP": {
        "title": "✨ 재기발랄한 활동가 (ENFP)를 위한 추천",
        "genres": [
            {"name": "하이틴 / 청춘 로맨스", "desc": "감정에 솔직하고 열정적인 에너지가 넘치는 장르", "book": "The Fault in Our Stars (존 그린)", "detail": "유쾌함과 슬픔을 넘나들며 진정한 삶의 소중함을 일깨우는 서사"},
            {"name": "하이 판타지", "desc": "무한한 상상력과 친구들과의 흥미진진한 모험", "book": "Harry Potter Box Set (J.K. 롤링)", "detail": "지루할 틈 없이 펼쳐지는 마법과 우정의 대서사시"},
            {"name": "휴먼 / 가족 소설", "desc": "주변 사람들과의 따뜻하고 통통 튀는 유대감", "book": "Love You Forever (로버트 먼치)", "detail": "마음이 몽글몽글해지는 사랑과 감동의 이야기"}
        ]
    },
    # ------------------ 관리자형 (SJ) ------------------
    "ISTJ": {
        "title": "📋 청렴결백한 논리주의자 (ISTJ)를 위한 추천",
        "genres": [
            {"name": "고전 문학", "desc": "시대를 초월하여 검증된 완성도 높은 클래식", "book": "To Kill a Mockingbird (하퍼 리)", "detail": "올곧은 신념과 원칙을 지키는 변호사의 감동적인 서사"},
            {"name": "법정 / 미스터리 스릴러", "desc": "사실과 단서를 기반으로 논리적으로 진실을 밝히는 장르", "book": "The Girl on the Train (폴라 호킨스)", "detail": "흩어진 단서들을 체계적으로 조합해 나가는 치밀한 스릴러"},
            {"name": "역사 / 시대극", "desc": "과거의 시대상을 현실적이고 생생하게 재현한 소설", "book": "The Great Gatsby (F. 스콧 피츠제럴드)", "detail": "1920년대 미국의 시대상을 완벽하게 묘사한 걸작"}
        ]
    },
    "ISFJ": {
        "title": "🛡️ 용감한 수호자 (ISFJ)를 위한 추천",
        "genres": [
            {"name": "가족 / 감동 드라마", "desc": "헌신적인 사랑과 일상 속의 따뜻함을 다룬 이야기", "book": "The Help (캐스린 스톡킷)", "detail": "서로를 보듬고 지켜주는 따뜻한 사람들의 연대기"},
            {"name": "로맨스 / 힐링", "desc": "마음을 편안하게 해주는 잔잔하고 감동적인 소설", "book": "The Shack (윌리엄 P. 영)", "detail": "가족의 아픔을 극복하고 깊은 위로를 전하는 힐링 소설"},
            {"name": "고전 문학", "desc": "전통적인 가치와 책임감을 묵직하게 그려낸 소설", "book": "To Kill a Mockingbird (하퍼 리)", "detail": "보이지 않는 곳에서 가족과 신념을 지키는 이야기"}
        ]
    },
    "ESTJ": {
        "title": "💼 엄격한 관리자 (ESTJ)를 위한 추천",
        "genres": [
            {"name": "사회 / 정치 스릴러", "desc": "체제와 질서, 그리고 이를 둘러싼 권력 다툼", "book": "The Hunger Games (수잔 콜린스)", "detail": "철저한 사회 시스템 안에서의 통제와 생존 투쟁"},
            {"name": "법정 / 고전 소설", "desc": "사회적 규범과 정의가 부딪히는 현실적인 드라마", "book": "To Kill a Mockingbird (하퍼 리)", "detail": "원칙과 법의 테두리 안에서 올바름을 증명하는 서사"},
            {"name": "논리 스릴러", "desc": "치밀한 계획과 실행력이 돋보이는 추리극", "book": "Gone Girl (길리언 플린)", "detail": "한 치의 오차도 없는 설계와 이를 쫓는 집요한 과정"}
        ]
    },
    "ESFJ": {
        "title": "💝 사교적인 외교관 (ESFJ)를 위한 추천",
        "genres": [
            {"name": "로맨틱 코미디 / 드라마", "desc": "사람들과의 관계와 풍부한 감정을 다루는 대중적인 장르", "book": "The Fault in Our Stars (존 그린)", "detail": "눈물과 웃음이 공존하는 아름다운 관계에 대한 이야기"},
            {"name": "휴먼 드라마", "desc": "공동체의 조화와 일상 속 영웅들의 따뜻한 이야기", "book": "The Help (캐스린 스톡킷)", "detail": "갈등을 넘어 진정한 이웃과 친구가 되어가는 감동 서사"},
            {"name": "대중 판타지 로맨스", "desc": "화려하고 모두가 열광하는 트렌디한 로맨스", "book": "Breaking Dawn (스테프니 메이어)", "detail": "전 세계를 열광시킨 매혹적인 뱀파이어 로맨스 신드롬"}
        ]
    },
    # ------------------ 탐험가형 (SP) ------------------
    "ISTP": {
        "title": "🛠️ 만능 재주꾼 (ISTP)를 위한 추천",
        "genres": [
            {"name": "생존 / 하드보일드", "desc": "복잡한 감정보다 뛰어난 문제 해결 능력이 빛나는 소설", "book": "The Martian (앤디 위어)", "detail": "어떤 위기 상황에서도 실용적인 기술로 살아남는 생존기"},
            {"name": "액션 / 스릴러", "desc": "빠른 전개와 손에 땀을 쥐게 하는 긴장감", "book": "The Hunger Games (수잔 콜린스)", "detail": "본능적인 감각과 신체 능력으로 데스매치를 돌파하는 액션"},
            {"name": "추리 / 미스터리", "desc": "사실적인 증거를 바탕으로 퍼즐을 푸는 이야기", "book": "The Girl on the Train (폴라 호킨스)", "detail": "현장의 단서를 조합해 진실에 다가가는 서늘한 추리"}
        ]
    },
    "ISFP": {
        "title": "🎨 호기심 많은 예술가 (ISFP)를 위한 추천",
        "genres": [
            {"name": "판타지 로맨스", "desc": "탐미적이고 감각적인 묘사가 돋보이는 환상적인 장르", "book": "Breaking Dawn (스테프니 메이어)", "detail": "시각적이고 감각적인 사랑의 감정을 극대화한 로맨스"},
            {"name": "청춘 / 성장 소설", "desc": "자유로운 영혼의 감정선과 아름다운 순간을 담은 이야기", "book": "The Fault in Our Stars (존 그린)", "detail": "현재의 감정에 충실한 주인공들의 반짝이는 청춘 드라마"},
            {"name": "서정적 드라마", "desc": "인간 내면의 고독과 아름다움을 섬세하게 터치하는 작품", "book": "The Great Gatsby (F. 스콧 피츠제럴드)", "detail": "화려함 속에 깃든 쓸쓸함과 탐미주의의 절정"}
        ]
    },
    "ESTP": {
        "title": "🔥 모험을 즐기는 사업가 (ESTP)를 위한 추천",
        "genres": [
            {"name": "액션 / 스릴러", "desc": "아드레날린이 솟구치는 짜릿하고 빠른 템포의 소설", "book": "The Hunger Games (수잔 콜린스)", "detail": "직관적인 판단력과 행동력으로 한계를 돌파하는 생존 게임"},
            {"name": "반전 미스터리", "desc": "긴장감이 끊이지 않는 스펙타클한 심리전", "book": "Gone Girl (길리언 플린)", "detail": "충격적인 반전과 속도감 넘치는 전개로 눈을 뗄 수 없는 스릴러"},
            {"name": "재난 / 생존 SF", "desc": "극한 상황에 던져져 본능적으로 돌파구를 찾는 이야기", "book": "The Martian (앤디 위어)", "detail": "쉴 새 없이 터지는 위기를 재치 있게 극복하는 카타르시스"}
        ]
    },
    "ESFP": {
        "title": "🎉 자유로운 영혼의 연예인 (ESFP)를 위한 추천",
        "genres": [
            {"name": "로맨틱 판타지", "desc": "모두의 이목을 끄는 화려하고 매혹적인 트렌디 로맨스", "book": "Breaking Dawn (스테프니 메이어)", "detail": "강렬한 감정과 드라마틱한 사건들이 몰아치는 판타지 로맨스"},
            {"name": "성인 로맨스 드라마", "desc": "파격적이고 스릴 넘치는 자극적인 사랑 이야기", "book": "Fifty Shades of Grey (E L 제임스)", "detail": "전 세계 독자들을 사로잡은 도발적이고 열정적인 로맨스"},
            {"name": "청춘 로맨스", "desc": "웃음과 눈물, 감동이 스펙터클하게 펼쳐지는 하이틴 소설", "book": "The Fault in Our Stars (존 그린)", "detail": "통통 튀는 유머와 짙은 여운이 어우러진 매력적인 이야기"}
        ]
    }
}

mbti_list = list(mbti_recommendations.keys())

# MBTI 선택 드롭다운
selected_mbti = st.selectbox(
    "👉 당신의 MBTI를 선택하세요:",
    mbti_list,
    index=None,
    placeholder="여기를 눌러 MBTI 선택..."
)

if selected_mbti:
    # 로딩 애니메이션 (찾는 척 하는 귀여운 효과)
    with st.spinner(f'🔍 {selected_mbti}의 책장을 뒤지는 중입니다...'):
        time.sleep(1.2)
    
    data = mbti_recommendations[selected_mbti]
    
    # 선택 시 풍선 이모지 파티!
    st.balloons() 
    
    # 결과 출력
    st.markdown(f"<h3 style='color: #4A90E2;'>{data['title']}</h3>", unsafe_allow_html=True)
    st.write(f"**{selected_mbti}** 독자님 취향 저격! 맞춤 장르와 역대 최고 베스트셀러 3권을 소개합니다. 🎉")
    st.write("")
    
    for idx, g in enumerate(data['genres'], 1):
        # 각각의 장르를 하나의 컨테이너/카드 형태로 묶어주기
        with st.container():
            st.markdown(f"#### 🏷️ {idx}. {g['name']}")
            st.caption(f"💡 {g['desc']}")
            
            # 책 정보를 눈에 띄는 Info 박스로 표시
            st.info(f"🏆 **역대 베스트셀러:** `{g['book']}`\n\n📌 **도서 소개:** {g['detail']}")
            st.write("---") # 구분선
            
    st.success("📚 오늘 밤, 이 책들 중 한 권 어떠신가요? ☕")
