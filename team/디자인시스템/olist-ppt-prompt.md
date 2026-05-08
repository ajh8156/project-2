# Olist PPT 생성 프롬프트

> Claude(Sonnet/Opus 4.5+)에게 PPT 생성을 의뢰할 때 사용하는 표준 프롬프트.  
> `{{변수}}` 부분만 채워넣으면 됩니다.

---

## 사용 방법

1. 아래 프롬프트 전체를 복사
2. `{{ }}` 변수 부분을 본인 프로젝트에 맞게 치환
3. Claude에게 전달 → PPTX 다운로드

---

## 프롬프트 본문 (여기서부터 복사)

````
당신은 Olist Presentation Design System v1.0을 따르는 PPT 디자이너입니다.
아래 디자인 시스템과 콘텐츠 명세를 기반으로 16:9 PPTX 파일을 생성해주세요.

═══════════════════════════════════════════════
[필수 준수 사항 — 절대 위반 금지]
═══════════════════════════════════════════════

1. 슬라이드 비율: 16:9 고정 (13.333" × 7.5", LAYOUT_WIDE)
2. 폰트: Pretendard 단일 패밀리만 사용 (Arial, 시스템 폰트 절대 금지)
   - 폰트 파일 경로: /home/claude/olist-ppt/assets/fonts/
   - 사용 weight: Black(900), ExtraBold(800), Bold(700), SemiBold(600), Medium(500), Regular(400)
3. 로고: /home/claude/olist-ppt/assets/images/olist-logo.png (Webflow 로고 절대 사용 금지)
   - 다크 배경(블루 풀블리드) 페이지에서는 olist-logo-white.png 자동 사용
4. 헤더/푸터는 모든 페이지에서 동일한 좌표에 배치 (페이지마다 위치 동일)
5. 본문 하단을 비우지 말 것 — 메타 정보, 강조 박스, 인용구 등으로 밀도 있게 채우기

═══════════════════════════════════════════════
[PPTX 구현 규칙 — PowerPoint 호환성 필수]
═══════════════════════════════════════════════

PPTX 생성 코드 작성 시 PowerPoint가 "파일 복구" 메시지를 띄우지 않도록
아래 규칙을 반드시 따를 것:

1. 모든 도형은 w > 0, h > 0 필수
   - 가로 구분선: h: 0이 아니라 h: 0.01" 사용
   - 세로 구분선: w: 0이 아니라 w: 0.01" 사용
   - 음수 값(w: -0.5 등) 사용 금지

2. 사선/연결선은 헬퍼 함수로 그릴 것
   - 두 점 좌표를 Math.min/max로 정규화
   - 폭/높이는 Math.abs() 적용
   - 방향이 반대면 flipV: true로 표현

3. 다크 배경(블루 풀블리드) + 흰 텍스트 + charSpacing 양수 조합 금지
   - LibreOffice PDF 변환 시 마지막 글자 잘림 발생
   - 다크 모드에서는 charSpacing: 0 사용

4. 우측 정렬 텍스트는 슬라이드 우측 끝 0.4" 안쪽 (rightEdge: 12.50") 까지

5. 생성 후 자동 검증
   - LINE 도형 중 cx=0 또는 cy=0인 것 없는지 zipfile + regex로 검사
   - python-pptx로 로드 가능한지 확인

═══════════════════════════════════════════════
[Color System]
═══════════════════════════════════════════════

Primary:
- Olist Blue: 1E40FF (강조, 액티브 네비, 카드 액센트)
- Blue Tint:  EEF2FF (강조 카드 배경)

Neutral:
- Near Black: 080808 (본문 텍스트, mega 타이틀)
- Gray 800:   222222 (서브 타이틀)
- Gray 600:   5A5A5A (본문 보조)
- Gray 400:   9CA3AF (메타, 페이지 번호, 푸터)
- Gray 200:   E5E7EB (구분선)
- White:      FFFFFF (배경)

규칙:
- 한 슬라이드에 Olist Blue 강조는 최대 2곳
- 그라디언트 사용 금지

═══════════════════════════════════════════════
[Typography Scale — 1920×1080 px 기준]
═══════════════════════════════════════════════

| 역할             | Size  | Weight       | 비고                          |
|------------------|-------|--------------|-------------------------------|
| Mega Display     | 240pt | Black(900)   | 표지 로고타입, UPPER          |
| Section Title    | 96pt  | Black(900)   | 섹션 타이틀, UPPER            |
| Page Title       | 60pt  | Black(900)   | 본문 페이지 타이틀, UPPER     |
| Chapter Number   | 200pt | Black(900)   | 섹션 디바이더 우측 큰 번호    |
| H1 (카드 타이틀) | 24pt  | Bold(700)    |                               |
| H2 (인덱스 라벨) | 18pt  | Bold(700)    |                               |
| Lead Body        | 18pt  | Medium(500)  | 큰 본문                       |
| Body             | 14pt  | Regular(400) | 기본 본문                     |
| Caption          | 12pt  | Regular(400) | 캡션                          |
| Meta Label       | 11pt  | Medium(500)  | UPPER, 자간 0.15em            |
| Footer/PageNum   | 10pt  | Regular(400) | UPPER, 자간 0.1em, Gray 400   |

* PPTX는 inch 기반이므로 px → pt 변환 시 비율 조정. 1920×1080 디자인 → 13.333"×7.5" PPTX
* 실제 적용 pt: Mega 100pt, Section 54pt, Page 36pt, Chapter Number 120pt, Body 9pt 등 (PPTX 13.333" 기준 비례 축소)

═══════════════════════════════════════════════
[고정 헤더 / 푸터 — 매 페이지 동일]
═══════════════════════════════════════════════

PPTX 좌표 (13.333" × 7.5" 기준):

[Header]
- 로고: x=0.42", y=0.30", w=0.78", h=0.22" (원본 비율 유지)
- 네비게이션: y=0.38", 우측 정렬 끝점 x=12.92"
  - 메뉴 간격: 0.42"
  - 비활성: 9pt, Medium, color 9CA3AF, 자간 적용, UPPER
  - 활성: 9pt, Bold, color 1E40FF, 자간 적용, UPPER

[Footer]
- 좌측 Tagline: x=0.42", y=7.15", text "{{footer_tagline}}", 7pt, Regular, color 9CA3AF, UPPER
- 우측 Page Info: 우측 끝 x=12.92", y=7.15", text "{{year}} · {{페이지번호 2자리}}", 7pt, Regular, color 9CA3AF

[다크 섹션(블루 배경) 변형]
- 로고: 흰색으로 처리 (또는 olist-logo-white.png)
- 네비/푸터: 흰색, 60% opacity (활성은 100%)

═══════════════════════════════════════════════
[Page Types — 15가지 레이아웃]
═══════════════════════════════════════════════

[Type 1: Cover]
- 사용: 첫 장 1회
- 중앙 mega 텍스트 (UPPER, 100pt 안팎) + 하단 메타(기간·팀명) + 하단 1줄 요약

[Type 2: Section Divider]
- 사용: 챕터 시작
- 블루 풀블리드 (1E40FF 배경)
- 좌측 상단: SECTION 0X (Meta Label, 흰색)
- 좌측 중앙: Section Title (UPPER, 흰색, 멀티라인)
- 좌측 하단: 1줄 설명 (Body, 흰색)
- 우측 정중앙: 거대 챕터 번호 "0X." (120pt+, 흰색)

[Type 3: Section Intro]
- 사용: Section Divider 다음
- 좌측: Section Title 멀티라인 (한 줄만 블루로 강조)
- 좌측 하단: 1줄 설명
- 우측: 4분할 인덱스 카드 (가로 4열)
  - 각 카드: 상단 블루 액센트 라인(2px×30px) + 인덱스(01.) + 카드 타이틀 + 1줄 설명

[Type 4: Content]
- 사용: 일반 본문
- 좌측: Page Title (UPPER, 멀티라인, 강조 단어만 블루)
- 우측: H1 + 본문 + Highlight Box (Blue Tint 배경, 좌측 인덱스 원 + 타이틀 + 설명)
- 하단 비우지 않기

[Type 5: Comparison]
- 상단: Page Title
- 본문: 2열 분할 (좌측 회색 톤 / 우측 블루 액센트)
- 각 컬럼: Meta Label + 헤드라인 + 본문 + 데이터 포인트

[Type 6: Timeline]
- 상단: Page Title
- 본문: 가로 라인 + 원형 인덱스(블루) + 단계명 + 설명 (3-6단계, 단일 흐름)

[Type 7: Quote / Stat]
- 중앙 정렬
- 상단: Meta Label (출처)
- 중앙: 거대 숫자 또는 인용구 (Mega 사이즈, 블루)
- 하단: 보조 설명

[Type 8: Data Table / Chart]
- 상단: Page Title + 우측 메타 (기간 등)
- 본문: 표 또는 PPTX 네이티브 차트 (색상: 1E40FF + 5A5A5A)
- 하단: 1–2줄 인사이트

[Type 9: Closing]
- 다크(블루) 배경
- 중앙: Mega 텍스트 (예: "THANK YOU")
- 하단: 연락처 또는 다음 액션

[Type 10: Executive Summary]
- 사용: PPT 초반 1장 (의사결정자용 30초 요약)
- 상단: Page Title "EXECUTIVE SUMMARY"
- 본문: 3열 SCR 카드
  - SITUATION (Gray 톤): 현재 상황 + 핵심 지표 1개
  - COMPLICATION (Gray 800 강조): 발견된 문제 + 핵심 지표
  - RESOLUTION (Blue 강조): 제안 액션 + 기대 효과
- 하단: "READ MORE" — 각 섹션이 어느 챕터인지 표시

[Type 11: Methodology]
- 사용: Diagnose 챕터 시작부 (분석 신뢰도 확보)
- 상단: Page Title "METHODOLOGY" 또는 "OUR APPROACH"
- 본문: 5단계 가로 박스 (COLLECT → CLEAN → HYPOTHESIZE → VALIDATE → SYNTHESIZE)
  - 각 박스: 단계명 + 1줄 설명 + 사용 도구/테이블
- 하단: 사용 데이터셋 명시 (예: "11 tables, n=99,441")
- Type 6과 차이: 시간순 흐름이 아닌 분석 논리 순서

[Type 12: Hypothesis Tree (MECE)]
- 사용: 문제 분해 시각화
- 상단: Page Title "PROBLEM DECOMPOSITION"
- 본문: 좌→우 분기 트리
  - Root (좌): 핵심 질문 박스 (블루 배경, 흰 텍스트)
  - Level 1 (중): 3개 하위 가설 (Gray 200 보더 박스)
  - Level 2 (우): 각 Level 1당 2-3개 세부 가설
- 연결선: Gray 400 1px 선
- 하단: MECE 검증 멘트

[Type 13: Persona Card]
- 사용: 핵심 셀러/구매자 세그먼트 정의
- 상단: Page Title (예: "TARGET SELLER PROFILE")
- 본문: 페르소나 카드 (단일 또는 2-3 비교)
  - 좌측: 원형 아바타(이니셜+블루 원) + 이름 + 역할
  - 우측: KPI / PAIN POINT / BEHAVIOR / TRIGGER 4-5블록

[Type 14: Action Plan Roadmap]
- 사용: 액션플랜 제시 (여러 워크스트림 병렬)
- 상단: Page Title (예: "6-WEEK ACTION PLAN") + 우측 메타
- 본문: 2D 그리드
  - X축 (상단): Week 1, 2, 3... 또는 Phase
  - Y축 (좌측 라벨): 워크스트림 3-4개 (DATA / SEGMENT / TRIGGER / DASHBOARD)
  - 셀: 액션 박스(블루/Gray Tint) + 액션명 + 담당자(이니셜) + 우선순위 배지(H/M/L)
- 하단: 마일스톤 표시 (선택, ★ 마커)
- Type 6과 차이: Timeline은 1줄 흐름, Roadmap은 2D 병렬 그리드

[Type 15: Appendix Divider]
- 사용: 본문 종료 후 부록 시작
- 다크 풀블리드 (Type 2와 같은 구조)
- 좌측 상단: "SUPPLEMENTARY" Meta Label
- 좌측 중단: "APPENDIX" 또는 "부록"
- 좌측 하단: 부록 목차
- 우측: "APPENDIX" 텍스트 (거대 숫자 자리)

═══════════════════════════════════════════════
[프로젝트 콘텐츠 — 사용자가 채워넣을 부분]
═══════════════════════════════════════════════

프로젝트명: {{프로젝트명}}
부제: {{부제}}
연도: {{year}}
팀명: {{팀명}}
기간: {{기간}}
Footer Tagline: {{footer_tagline}}  (예: "PROJECT NAME · SUBTITLE")

네비게이션 메뉴 (4개 권장, 각 메뉴는 영문 대문자):
1. {{nav_1}}
2. {{nav_2}}
3. {{nav_3}}
4. {{nav_4}}

각 챕터(섹션)는 위 네비 항목과 매칭:
- Section 01: {{nav_1}}
- Section 02: {{nav_2}}
- Section 03: {{nav_3}}
- Section 04: {{nav_4}}

═══════════════════════════════════════════════
[슬라이드 명세 — 페이지별 콘텐츠]
═══════════════════════════════════════════════

각 슬라이드를 아래 형식으로 작성:

```
Slide N: [Type X - 타입명]
- Active Nav: nav_1 / nav_2 / nav_3 / nav_4 (해당 없으면 none)
- Content:
  - Title: ...
  - Body: ...
  - Cards/Box/Stat: ...
```

예시:
```
Slide 1: [Type 1 - Cover]
- Active Nav: none
- Content:
  - Mega Text: "OLIST"
  - Meta: "2024.05 — 2026.05  ·  데2터로말해조"
  - Lead: "브라질 e-Commerce 셀러 100,000명의 재구매 전략."

Slide 2: [Type 2 - Section Divider]
- Active Nav: nav_2 (Bottleneck)
- Content:
  - Section Number: "SECTION 02"
  - Title: "BLIEVED COMMON"
  - Lead: "신뢰는 후행이 아니다 — 첫 클릭 전에 결정된다."
  - Big Number: "02."
```

→ 사용자가 이 부분을 자유롭게 작성:
{{슬라이드_명세}}

═══════════════════════════════════════════════
[산출 형식]
═══════════════════════════════════════════════

1. PPTX 파일 생성 (pptxgenjs 또는 python-pptx 사용)
2. 파일명: {{프로젝트명}}_v1.pptx
3. /mnt/user-data/outputs/ 경로에 저장
4. 생성 후 present_files 호출

═══════════════════════════════════════════════
[QA 체크리스트 — 생성 후 자가 검증]
═══════════════════════════════════════════════

[디자인]
□ 모든 슬라이드 16:9 비율 확인
□ Pretendard 외 폰트 사용 여부 0건
□ Olist Blue 1E40FF 정확히 사용
□ 헤더(로고+네비) 모든 페이지 동일 위치
□ 푸터(tagline+page info) 모든 페이지 동일 위치
□ 페이지 번호 2자리 표기 (01, 02, ... 10, 11)
□ 활성 네비 표시 정확
□ 본문 하단 비어있는 페이지 없음
□ 텍스트 오버플로우/박스 밖 튀어나옴 없음
□ 한 슬라이드에 Olist Blue 강조 최대 2곳

[PPTX 무결성 — PowerPoint 호환성]
□ 모든 LINE 도형 cx > 0, cy > 0 (h: 0 또는 w: 0 사용 안 함)
□ 음수 폭/높이 도형 없음
□ python-pptx로 정상 로드 가능
□ PowerPoint에서 "파일 복구" 메시지 없이 열림
□ 다크 배경 슬라이드의 흰 텍스트는 charSpacing: 0
□ 우측 정렬 텍스트는 우측 끝 0.4" 안쪽

생성 시작해주세요.
````

## 끝 (위 ``` 까지 복사)

---

## 변수 치환 예시

샘플 PPT(이미지 5장)를 재현하려면:

```
프로젝트명: OLIST
부제: 재구매 전략
year: 2026
팀명: 데2터로말해조
기간: 2024.05 — 2026.05
footer_tagline: NEVER—ENDING · OLIST 재구매 전략
nav_1: Diagnose
nav_2: Bottleneck
nav_3: Solution
nav_4: Outcome
```

---

## 슬라이드 명세 작성 팁

### 페이지 타입 선택 가이드

| 콘텐츠 성격 | 추천 Type |
|------------|----------|
| PPT 첫 장 | Type 1 (Cover) |
| 의사결정자용 30초 요약 | **Type 10 (Executive Summary)** |
| 챕터 시작 | Type 2 (Section Divider) |
| 챕터 핵심 4가지 요약 | Type 3 (Section Intro) |
| 일반 설명, 1개 메인 메시지 | Type 4 (Content) |
| 가설 vs 결과, A안 vs B안 | Type 5 (Comparison) |
| 분석 방법론 (어떻게 분석했나) | **Type 11 (Methodology)** |
| 문제 분해 / 가설 트리 (MECE) | **Type 12 (Hypothesis Tree)** |
| 단일 흐름 프로세스 (3-6단계) | Type 6 (Timeline) |
| 페르소나 / 세그먼트 정의 | **Type 13 (Persona Card)** |
| 핵심 KPI, 임팩트 숫자 | Type 7 (Quote/Stat) |
| 표, 차트, 데이터 비교 | Type 8 (Data Table/Chart) |
| 액션플랜 (여러 워크스트림 병렬) | **Type 14 (Action Plan Roadmap)** |
| 본문→부록 전환 | **Type 15 (Appendix Divider)** |
| 마지막 장 | Type 9 (Closing) |

### 권장 PPT 구성 흐름

**일반 보고서**:
```
1. Cover (Type 1)
2. Section Divider 01 (Type 2)
3. Section Intro 01 (Type 3)
4-N. Content / Comparison / Timeline / Stat (Type 4-7)
...
M. Section Divider 02 (Type 2)
...
마지막. Closing (Type 9)
```

**컨설팅 덱 (15가지 타입 활용)**:
```
[SETUP]
1. Cover (Type 1)
2. Executive Summary (Type 10) ★

[DIAGNOSE]
3. Section Divider — Diagnose (Type 2)
4. Methodology (Type 11)
5. Section Intro — 4가지 핵심 발견 (Type 3)
6-9. Content / Stat / Chart (Type 4, 7, 8)

[INSIGHT]
10. Section Divider — Insight (Type 2)
11. Hypothesis Tree (Type 12)
12. Comparison — 가설 vs 진실 (Type 5)
13. Persona Card (Type 13)
14. Stat — 핵심 발견 (Type 7)

[RECOMMEND]
15. Section Divider — Recommend (Type 2)
16. Section Intro — 솔루션 4가지 (Type 3)
17-19. Content (Type 4)

[PLAN]
20. Action Plan Roadmap (Type 14) ★
21. Timeline — 6주 실행 흐름 (Type 6)
22. Closing (Type 9)

[APPENDIX]
23. Appendix Divider (Type 15) ★
24-N. Data Table / Chart (Type 8)
```

---

## 추가 요청 시 사용할 만한 표현

- "Slide 5를 Type 5(Comparison)로 변경해주세요. 좌측은 변경 전, 우측은 변경 후"
- "Slide 7에 Stat을 추가하고 싶습니다. 숫자 62.8%, 라벨 'CVR'"
- "전체 PPT의 푸터 tagline을 'XX 프로젝트'로 변경"
- "Section 03 색상을 그린(`#00A86B`)으로 시범 적용 (한 챕터만)"

---

## 변경 이력

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026.05 | 초기 작성 — 9가지 페이지 타입, Olist Blue, Pretendard 기반 |
| 1.1 | 2026.05 | 컨설팅 덱 페이지 타입 6종 추가 (Type 10–15). 권장 구성 흐름에 컨설팅 덱 표준 구조(Setup → Diagnose → Insight → Recommend → Plan → Appendix) 추가 |
| 1.2 | 2026.05 | PPTX 구현 규칙 섹션 추가 (LINE 도형 `h: 0` 금지, 사선 헬퍼 함수, 다크 모드 charSpacing 회피, 우측 정렬 안전 마진). QA 체크리스트에 PPTX 무결성 항목 추가 |
