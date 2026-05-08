# Olist Presentation Design System

> **Version 1.2** · 2026.05  
> **For**: Olist 성장 진단 컨설팅 PPT 시리즈 (팀 공유용)  
> **Slide Format**: 16:9 only (1920×1080 px / 13.333" × 7.5")

---

## 0. 디자인 철학

이 디자인 시스템은 **"Less is more, but louder"** 원칙을 따릅니다.

- **여백 ≠ 공백**: 좌측 거대 타이포그래피 + 우측 콘텐츠의 비대칭 구도가 시각적 무게를 만듭니다.
- **블루는 도구**: Olist Blue(`#1E40FF`)는 강조 단어 1개에만 사용하여 정보 우선순위를 명확히 합니다.
- **반복은 신뢰**: 헤더·푸터·그리드는 모든 페이지에서 동일한 좌표를 유지합니다.
- **대문자 영문 = 시각적 앵커**: 본문은 한글이지만, 페이지 타이틀은 영문 대문자 mega 타입으로 시선을 잡습니다.
- **컨설팅 덱 톤**: 외부 컨설팅사가 클라이언트에게 진단/제안하는 어조. 주관적 표현 대신 데이터·프레임워크·근거 중심. SCR(Situation-Complication-Resolution), MECE 트리, 2D 로드맵 등 컨설팅 표준 시각 언어를 차용.

---

## 1. Color System

### 1.1 Primary
| Role | HEX | RGB | 용도 |
|------|-----|-----|------|
| **Olist Blue** | `#1E40FF` | 30, 64, 255 | 브랜드 컬러, 강조 텍스트, 액티브 네비, CTA |
| **Olist Blue Hover** | `#1730CC` | 23, 48, 204 | 인터랙션 hover (참고용) |
| **Blue Tint** | `#EEF2FF` | 238, 242, 255 | 강조 카드 배경 (10% tint) |

### 1.2 Neutral
| Role | HEX | 용도 |
|------|-----|------|
| **Near Black** | `#080808` | 본문 텍스트, 메인 타이포 |
| **Gray 800** | `#222222` | 서브 타이틀 |
| **Gray 600** | `#5A5A5A` | 본문 보조, 캡션 |
| **Gray 400** | `#9CA3AF` | 메타 라벨, 페이지 번호, 푸터 |
| **Gray 200** | `#E5E7EB` | 디바이더 라인, 카드 테두리 |
| **White** | `#FFFFFF` | 기본 배경, 다크 섹션 텍스트 |

### 1.3 Semantic (강조 색상 — v1.3 갱신)
> **블루 단색 시스템의 시각 강도 차이를 만드는 용도.** 강조 표현이 필수인 곳에만 사용 (남용 금지).
> 한 슬라이드에 Olist Blue + Semantic 합쳐 **최대 3곳**까지.

| Role | HEX | RGB | 용도 |
|------|-----|-----|------|
| **Critical** | `#EE1D36` | 238, 29, 54 | 위기·부정 지표 (Retention 붕괴, 이탈, 지연 등) |
| **Warning**  | `#FFAE13` | 255, 174, 19 | 주의·중간 지표 (Activation 흔들림, 일부 KR 미달) |
| **Success**  | `#00D722` | 0, 215, 34 | 긍정·달성 지표 (KR 목표 달성, 정시 배송 등) |

**적용 권장 케이스:**
- AARRR 3축 신호등 dot → Acquisition `Success` / Activation `Warning` / Retention `Critical`
- KR 게이지 — 현재값(중립) → 목표값에 `Success`
- Before/After 비교 — Before stat에 `Critical`, After stat에 `Success`
- Journey Map 색대 그라데이션 — 🟢 첫경험(`Success`) → 🔵 재구매(Olist Blue) → 🟡→🔴 이탈방지(`Warning`→`Critical`)
- 기대효과 표 — 목표값(12개월 컬럼)에 `Success`

**금지:**
- 큰 면적 배경 (Soft tint도 X)
- 카드 보더 전체에 Semantic
- 한 슬라이드에 3개 모두 동시 노출 (정보 혼란)

### 1.4 사용 규칙
- ✅ 한 슬라이드에 Primary Blue는 **최대 2곳**까지만 사용
- ✅ 본문 텍스트는 항상 `#080808` (검정에 가까운 near-black)
- ❌ 그라디언트 사용 금지 (Olist Blue는 단색으로만)
- ❌ 임의의 색상 추가 금지 (위 팔레트 외 사용 시 팀 리뷰 필수)

---

## 2. Typography System

### 2.1 단일 폰트 패밀리: **Pretendard**

| Weight | 파일명 | 용도 |
|--------|--------|------|
| 900 Black | `Pretendard-Black.otf` | Mega Display (표지 로고타입, 챕터 번호) |
| 800 ExtraBold | `Pretendard-ExtraBold.otf` | Section Title, Page Title |
| 700 Bold | `Pretendard-Bold.otf` | Sub-heading, 강조 텍스트 |
| 600 SemiBold | `Pretendard-SemiBold.otf` | 카드 타이틀, Active 네비 |
| 500 Medium | `Pretendard-Medium.otf` | 본문 강조, 라벨 |
| 400 Regular | `Pretendard-Regular.otf` | 본문 기본 |
| 300 Light | `Pretendard-Light.otf` | 큰 본문(Lead text) |
| 200 ExtraLight | `Pretendard-ExtraLight.otf` | 사용 자제 |
| 100 Thin | `Pretendard-Thin.otf` | 사용 자제 |

> **타 폰트 사용 절대 금지.** Arial, Helvetica, 시스템 기본 폰트 모두 불가.

### 2.2 Type Scale (16:9 / 1920×1080 기준)

| 역할 | Size | Weight | Line Height | Letter Spacing | Case |
|------|------|--------|-------------|----------------|------|
| **Mega Display** | 240pt | 900 Black | 1.0 | -0.04em | UPPER |
| **Section Title** | 96pt | 900 Black | 1.05 | -0.02em | UPPER |
| **Page Title** | 60pt | 900 Black | 1.05 | -0.02em | UPPER |
| **Chapter Number** | 200pt | 900 Black | 1.0 | -0.02em | — |
| **H1 / 카드 타이틀** | 24pt | 700 Bold | 1.3 | normal | — |
| **H2 / 인덱스 라벨** | 18pt | 700 Bold | 1.3 | normal | — |
| **Lead Body** | 18pt | 500 Medium | 1.5 | normal | — |
| **Body** | 14pt | 400 Regular | 1.6 | normal | — |
| **Caption** | 12pt | 400 Regular | 1.4 | normal | — |
| **Meta Label** (uppercase) | 11pt | 500 Medium | 1.3 | 0.15em | UPPER |
| **Footer / Page Num** | 10pt | 400 Regular | 1.3 | 0.1em | UPPER |

### 2.3 사용 규칙
- ✅ Mega/Section/Page Title은 **영문 대문자**가 기본 (시각적 앵커)
- ✅ 본문은 한글, 타이틀은 영문 대문자 — 의도된 조합
- ✅ Meta Label은 `letter-spacing 0.15em`을 반드시 적용
- ❌ Italic 사용 금지 (Pretendard는 italic이 어색함)
- ❌ 같은 슬라이드에서 3개 이상의 weight 동시 사용 금지

---

## 3. Layout Grid

### 3.1 슬라이드 규격
- **Aspect Ratio**: 16:9 고정
- **Resolution**: 1920×1080 px (디자인 기준) / 13.333" × 7.5" (PPTX)
- **단위 변환**: 1 inch = 144 px (디자인 ↔ PPTX)

### 3.2 Safe Zone & Margins
| 영역 | px (1920×1080) | inch (13.33×7.5) |
|------|---------------|------------------|
| Outer Margin (좌/우) | 80px | 0.56" |
| Outer Margin (상/하) | 50px | 0.35" |
| Header 영역 (Top) | 50–110px (60px 높이) | 0.35"–0.76" |
| Footer 영역 (Bottom) | 1010–1060px | 7.01"–7.36" |
| Body 영역 | 150–970px (820px 높이) | 1.04"–6.74" |

### 3.3 Column Grid
- **12 컬럼 / 24px gutter** (디자인 작업용 가이드, 실제 PPT는 자유 배치)
- 본문 패턴: **5:7 비대칭** (좌 mega title 5열 / 우 콘텐츠 7열)

---

## 4. Fixed Elements (모든 페이지 공통)

### 4.1 Header (상단 고정)
| 요소 | 위치 (px) | 위치 (inch) | 스타일 |
|------|-----------|-------------|--------|
| **Olist 로고** | x: 80, y: 50 | x: 0.56", y: 0.35" | 높이 32px(0.22"), 원본 비율 유지 |
| **Navigation** | y: 50, 우측 정렬 끝점 x: 1840 | y: 0.42", 우측 끝 x: 12.78" | 메뉴 간격 60px(0.42") |

**네비게이션 스타일:**
- 비활성: Pretendard 500 Medium, 14pt, color `#9CA3AF`, letter-spacing `0.1em`, UPPER
- 활성(현재 챕터): Pretendard 700 Bold, 14pt, color `#1E40FF`, letter-spacing `0.1em`, UPPER

### 4.2 Footer (하단 고정)
| 요소 | 위치 (px) | 위치 (inch) | 스타일 |
|------|-----------|-------------|--------|
| **Tagline (좌)** | x: 80, y: 1030 | x: 0.56", y: 7.15" | 10pt, Regular, `#9CA3AF`, letter-spacing `0.1em`, UPPER |
| **Page Info (우)** | y: 1030, 우측 끝 x: 1840 | y: 7.15", 우측 끝 x: 12.78" | 10pt, Regular, `#9CA3AF`, letter-spacing `0.1em` |

**Tagline 형식**: `{프로젝트명} · {부제}` (예: `NEVER—ENDING · OLIST 재구매 전략`)  
**Page Info 형식**: `{연도} · {페이지번호 2자리}` (예: `2026 · 03`)

### 4.3 다크 섹션(블루 풀블리드)에서의 변형
- 로고: `olist-logo-white.png` 사용 또는 흰색 처리
- 네비/푸터 비활성 텍스트: `#FFFFFF` 60% opacity
- 네비 활성: `#FFFFFF` 100% (블루 위에서 블루 강조 불가)

---

## 5. Page Types (15가지)

> 모든 페이지는 §4의 Header/Footer를 동일하게 포함합니다.  
> Type 1–9는 범용 레이아웃, Type 10–15는 컨설팅 덱 특화 레이아웃입니다.

### Type 1. Cover (표지)
- **용도**: PPT 첫 장 1회 사용
- **레이아웃**: 중앙 정렬, mega 로고타입 (240pt) + 기간/팀명 + 한 줄 설명
- **샘플**: 이미지 2 ("OLIST")
- **구성 요소**:
  - 중앙 mega title (페이지 정중앙)
  - 하단 메타: 기간(`2024.05 — 2026.05`) · 구분점 · 팀명
  - 하단 1줄 요약 (Lead Body 18pt)

### Type 2. Section Divider (챕터 구분)
- **용도**: 챕터(섹션) 시작 시 1장씩
- **레이아웃**: 블루 풀블리드 배경, 좌측 거대 타이틀 + 우측 거대 챕터 번호
- **샘플**: 이미지 4 ("BLIEVED COMMON" + "02.")
- **구성 요소**:
  - 좌측 상단: `SECTION 0X` Meta Label
  - 좌측 중단: Section Title (96pt, 흰색)
  - 좌측 하단: 1줄 설명 (Body, 흰색)
  - 우측: 거대 챕터 번호 (200pt, 흰색)

### Type 3. Section Intro (챕터 인트로)
- **용도**: Section Divider 다음 장, 챕터 핵심 요약
- **레이아웃**: 좌측 mega title (2-3줄) + 우측 4분할 인덱스 카드
- **샘플**: 이미지 3 ("SEVERAL CORE FINDINGS")
- **구성 요소**:
  - 좌측: Section Title 멀티라인, 두 번째 줄만 블루
  - 좌측 하단: 1줄 설명
  - 우측: 4개 카드 (각 카드: 상단 블루 라인 + 인덱스 번호 + 제목 + 1줄 설명)

### Type 4. Content (일반 본문)
- **용도**: 가장 많이 쓰이는 본문 페이지
- **레이아웃**: 좌측 mega title (60–96pt) + 우측 본문 콘텐츠
- **샘플**: 이미지 5 ("SEVERAL BUILDINGS BEAUTY")
- **구성 요소**:
  - 좌측: Page Title 멀티라인, 강조 단어만 블루
  - 우측: H1 → Body 텍스트 → 강조 카드(Blue Tint 배경)
  - 하단 비우지 않기: 추가 메타 정보, 인용 박스, 또는 작은 시각 요소

### Type 5. Comparison (좌우 비교)
- **용도**: Before/After, A안 vs B안, 가설 vs 결과
- **레이아웃**: 상단 페이지 타이틀 + 하단 2열 분할
- **구성 요소**:
  - 상단 좌측: Page Title (60pt, 멀티라인 가능)
  - 본문: 2열 (좌측: 회색 톤 / 우측: 블루 강조 또는 White + 블루 액센트)
  - 각 컬럼: 라벨(Meta Label) + 헤드라인 + 본문 + 데이터 포인트

### Type 6. Timeline (타임라인 / 프로세스)
- **용도**: 단계별 흐름, 일정, 프로세스 (단일 흐름)
- **레이아웃**: 상단 타이틀 + 하단 가로 스텝 (3–6단계)
- **구성 요소**:
  - 상단: Page Title
  - 본문: 가로 라인 + 원형 인덱스(블루) + 단계명 + 설명
  - 단계 간격: 균등 분할
  - 마지막 단계는 블루 강조 가능

### Type 7. Quote / Stat (숫자/인용 강조)
- **용도**: 핵심 지표, 임팩트 있는 한 마디
- **레이아웃**: 중앙 정렬, mega 숫자 또는 큰 인용구
- **구성 요소**:
  - 상단: Meta Label (출처 또는 카테고리)
  - 중앙: 거대 숫자(180pt, Black, 블루) 또는 인용구(60pt, ExtraBold)
  - 하단: 보조 설명 (Lead Body)
  - 하단 좌측 또는 우측: 데이터 출처 캡션

### Type 8. Data Table / Chart (데이터 중심)
- **용도**: KPI 대시보드, 비교표, 차트
- **레이아웃**: 상단 타이틀 + 하단 표/차트 (가로 풀폭)
- **구성 요소**:
  - 상단: Page Title (60pt) + 우측 메타(기간 등)
  - 본문: 표 또는 차트 (PPTX 네이티브 차트 사용)
  - 차트 색상: Olist Blue + Gray 600 (단색 강조)
  - 하단: 1–2줄 인사이트 (Body)

### Type 9. Closing (마무리)
- **용도**: PPT 마지막 장
- **레이아웃**: 중앙 정렬, "THANK YOU" 또는 핵심 메시지
- **구성 요소**:
  - 중앙: Mega 텍스트 (예: `THANK YOU` / `LET'S BUILD`)
  - 하단: 연락처 또는 다음 액션 (Body)
  - 다크 섹션(블루 배경)으로 구성하여 시각적 마침표

---

### Type 10. Executive Summary (경영진 요약)
- **용도**: PPT 초반 1장. 전체 덱의 미니어처. 의사결정자가 30초 안에 핵심을 파악
- **레이아웃**: 3열 SCR 프레임워크 (Situation / Complication / Resolution)
- **구성 요소**:
  - 상단: Page Title "EXECUTIVE SUMMARY" + 1줄 설명
  - 본문: 3개 컬럼 카드
    - **SITUATION** (Gray 톤): 현재 상황 라벨 + 헤드라인 + 1-2줄 설명 + 핵심 지표 1개
    - **COMPLICATION** (Gray 800 강조): 발견된 문제 + 헤드라인 + 1-2줄 + 핵심 지표
    - **RESOLUTION** (Blue 강조): 제안 액션 + 헤드라인 + 1-2줄 + 기대 효과
  - 하단: "READ MORE" 가이드 (각 섹션이 어느 챕터에서 다뤄지는지 표시)

### Type 11. Methodology (분석 접근법)
- **용도**: Diagnose 챕터 시작부. "어떻게 분석했는지" 신뢰도 확보
- **레이아웃**: 가로 5단계 프로세스 + 각 단계별 도구/테이블/산출물 명시
- **구성 요소**:
  - 상단: Page Title "METHODOLOGY" (또는 "OUR APPROACH")
  - 본문: 5개 박스 가로 배열 (각 박스 = 한 단계)
    - 단계명 (예: COLLECT / CLEAN / HYPOTHESIZE / VALIDATE / SYNTHESIZE)
    - 1줄 설명
    - 사용 도구/테이블 (예: "olist_orders_dataset · marketing_funnel")
  - 하단: 사용 데이터셋 목록 (예: "Olist Brazilian E-Commerce Dataset (11 tables, n=99,441)")
  - **Type 6 Timeline과의 차이**: Timeline은 실행 단계(시간순), Methodology는 분석 방법론(논리순)

### Type 12. Hypothesis Tree (가설 구조도, MECE)
- **용도**: 문제 분해. "이탈률 = A + B + C → A는 다시 A1 + A2"
- **레이아웃**: 좌→우 분기 트리 (1 → 3 → 6-9 노드)
- **구성 요소**:
  - 상단: Page Title (예: "PROBLEM DECOMPOSITION")
  - 본문: 트리 다이어그램
    - **Root** (좌측): 핵심 질문 박스 (블루 배경, 흰 텍스트)
    - **Level 1** (중앙): 3개 하위 가설 (Gray 200 보더 박스)
    - **Level 2** (우측): 각 Level 1당 2-3개 세부 가설
  - 연결선: Gray 400 1px 선
  - 하단: MECE 검증 멘트 (예: "각 분기는 상호 배타적이며 합쳐서 전체를 포괄합니다.")

### Type 13. Persona Card (페르소나 카드)
- **용도**: 핵심 셀러/구매자 세그먼트 정의 시
- **레이아웃**: 1인 페르소나 또는 2-3인 비교 페르소나
- **구성 요소**:
  - 상단: Page Title (예: "TARGET SELLER PROFILE")
  - 본문: 페르소나 카드 (단일 또는 다중)
    - **좌측 (좁은 컬럼)**: 원형 아바타(이니셜+블루 원) + 페르소나 이름 + 역할 라벨
    - **우측 (넓은 컬럼)**: 4–5개 정보 블록
      - **KPI**: 핵심 지표 (예: "월 매출 R$5,000+")
      - **PAIN POINT**: 주요 어려움
      - **BEHAVIOR**: 행동 패턴
      - **TRIGGER**: 우리가 활용할 동기
  - 다중 페르소나의 경우 가로로 2-3개 나열, 각 카드는 동일 구조

### Type 14. Action Plan Roadmap (2D 실행 로드맵)
- **용도**: 액션플랜 제시 페이지. 여러 워크스트림 병렬 시각화
- **레이아웃**: 2D 그리드 (X축: 주차/월, Y축: 워크스트림)
- **구성 요소**:
  - 상단: Page Title (예: "6-WEEK ACTION PLAN") + 우측 메타(기간)
  - 본문: 그리드
    - **상단 헤더 (X축)**: Week 1 / Week 2 / ... 또는 Phase 1 / 2
    - **좌측 라벨 (Y축)**: 워크스트림 3-4개 (예: DATA / SEGMENT / TRIGGER / DASHBOARD)
    - **셀**: 액션 박스 (블루 또는 Gray Tint 배경) + 액션명 + 담당자(이니셜) + 우선순위 배지(H/M/L)
  - 하단: 마일스톤 표시 (선택, 특정 주차에 ★ 마커)
  - **Type 6 Timeline과의 차이**: Timeline은 단일 흐름(5단계 1줄), Roadmap은 2D 그리드(여러 워크스트림 병렬)

### Type 15. Appendix Divider (부록 구분)
- **용도**: 본 덱과 부록 구분. 컨설팅 덱은 보통 본문 + 부록 구조
- **레이아웃**: 다크 섹션 디바이더와 동일하나, 우측 큰 번호 대신 "APPENDIX" 텍스트
- **구성 요소**:
  - 좌측 상단: `SUPPLEMENTARY` Meta Label
  - 좌측 중단: "APPENDIX" 또는 한글 "부록" (Section Title 사이즈)
  - 좌측 하단: 부록 목차 (예: "01 Data Schema  ·  02 Detail Charts  ·  03 References")
  - 우측: "APPENDIX" 텍스트 (Type 2의 거대 숫자 대신, 같은 사이즈)

---

## 6. Components

### 6.1 Index Card (인덱스 카드, Type 3에서 사용)
- 크기: 약 240×120px (1.67" × 0.83")
- 상단: 블루 액센트 라인 (높이 2px, 폭 30px)
- 본문:
  - 인덱스 번호 (24pt, 900 Black, 블루)
  - 카드 타이틀 (16pt, 700 Bold, 검정)
  - 1줄 설명 (12pt, 400 Regular, Gray 600)
- 카드 간 간격: 24px

### 6.2 Highlight Box (강조 박스, Type 4에서 사용)
- 배경: `#EEF2FF` (Blue Tint)
- 패딩: 16px
- 좌측: 인덱스 원형 라벨 (블루, 24×24px)
- 우측: 타이틀(14pt Bold, 블루) + 1줄 설명(12pt Regular)

### 6.3 Stat Block (지표 블록)
- 큰 숫자: 60–96pt, 900 Black, 블루
- 라벨: 12pt, Meta Label 스타일
- 보조: 14pt, Body

### 6.4 Divider Line (구분선)
- 색상: `#E5E7EB`
- 두께: 1px
- 길이: 자유

---

## 7. Spacing & Sizing Tokens

```
Space Tokens (px):
  xs:  4   sm:  8   md: 16   lg: 24
  xl: 32   2xl: 48  3xl: 64  4xl: 80

Border Radius:
  none: 0   sm: 4   md: 8   round: 50%
  (8px 이상은 사용 자제 — 샤프한 인상 유지)

Border Width:
  thin: 1px   thick: 2px
```

---

## 8. Iconography

- **금지**: 컬러풀하거나 일러스트 스타일 아이콘
- **권장**: 단색 라인 아이콘 (Heroicons, Lucide 스타일)
- **색상**: 검정(`#080808`) 또는 Olist Blue
- **크기**: 본문에 사용 시 16–24px

---

## 9. Do's & Don'ts

### ✅ Do
- 매 페이지 헤더/푸터를 동일한 좌표에 배치
- 좌측 mega title + 우측 콘텐츠 비대칭 구도 유지
- Olist Blue는 한 슬라이드에 최대 2곳
- 본문 하단 여백을 메타 정보, 인용 박스로 채우기
- 영문 대문자 타이틀 + 한글 본문 조합

### ❌ Don't
- Pretendard 외 다른 폰트 사용
- 그라디언트, 그림자(과한 것), 입체 효과
- 8px 이상의 큰 border-radius
- 한 슬라이드에 3개 이상의 weight 동시 사용
- 의미 없는 장식용 풀폭 컬러바, 액센트 라인 (AI 슬라이드 티남)
- 본문 텍스트 가운데 정렬 (타이틀만 가운데 가능)
- 크림/베이지 배경 (흰색만)

---

## 10. Asset References

### 10.1 폰트 파일
경로: `/assets/fonts/`
- Pretendard-Black.otf, Bold.otf, ExtraBold.otf, ExtraLight.otf, Light.otf, Medium.otf, Regular.otf, SemiBold.otf, Thin.otf

### 10.2 로고 파일
경로: `/assets/images/`
- `olist-logo.png` (블루 버전, 흰 배경용)
- `olist-logo-white.png` (흰색 버전, 블루 배경용 — 별도 제작 필요)

### 10.3 다운로드
- Pretendard 공식: https://github.com/orioncactus/pretendard
- Olist 로고: 사내 자산 (브랜드팀 문의)

---

## 11. PPTX 구현 주의사항 (Implementation Notes)

PPT 생성 코드 작성 시 PowerPoint와의 호환성을 위해 반드시 따라야 할 규칙입니다. 위반 시 PowerPoint가 "파일 복구" 메시지를 띄우거나 일부 도형이 깨질 수 있습니다.

### 11.1 도형 크기 (모든 도형 공통)

- **모든 도형은 `w > 0` 그리고 `h > 0`을 만족해야 합니다.**
- 가로 구분선처럼 시각적으로 매우 가는 요소를 만들 때는 `h: 0`이 아니라 **`h: 0.01"`(약 1px)** 을 사용합니다.
- 세로 구분선도 동일하게 **`w: 0.01"`** 사용.
- 음수 값(`w: -0.5`, `h: -0.3`) 사용 금지. 좌표 계산 시 좌→우/상→하가 보장되도록 `Math.min/max`로 정규화 후 폭/높이는 `Math.abs()` 사용.

```javascript
// ❌ Bad — PowerPoint 복구 모드 진입
slide.addShape(pres.shapes.LINE, {
  x: 1, y: 5, w: 10, h: 0,  // h가 0
  line: { color: "E5E7EB", width: 1 },
});

// ✓ Good
slide.addShape(pres.shapes.LINE, {
  x: 1, y: 5, w: 10, h: 0.01,  // 매우 가는 가로선
  line: { color: "E5E7EB", width: 1 },
});
```

### 11.2 사선/연결선 그리기

두 점 사이를 잇는 사선(예: 트리 다이어그램의 연결선)은 시작점과 끝점의 좌표 관계에 따라 음수 폭/높이가 발생할 수 있습니다. 헬퍼 함수로 안전하게 처리합니다.

```javascript
/**
 * 두 점 (x1,y1) → (x2,y2) 사이에 직선/사선을 그리는 헬퍼.
 * pptxgenjs의 LINE 도형은 음수 w/h를 PowerPoint에 거부당하므로,
 * 좌표를 정규화하고 방향이 반대면 flipV로 표현.
 */
function addLine(slide, x1, y1, x2, y2, lineOpts) {
  const x = Math.min(x1, x2);
  const y = Math.min(y1, y2);
  const w = Math.abs(x2 - x1);
  const h = Math.abs(y2 - y1);
  
  // 두께 0 회피 (수평/수직선 최소 두께)
  const safeW = w === 0 ? 0.001 : w;
  const safeH = h === 0 ? 0.001 : h;
  
  // 방향 결정: 끝점이 시작점보다 위에 있으면 수직 반전
  const flipV = (y2 < y1);
  
  slide.addShape(pres.shapes.LINE, {
    x, y, w: safeW, h: safeH,
    line: lineOpts,
    flipV: flipV,
  });
}
```

### 11.3 텍스트 박스 자간 (charSpacing) — 다크 모드

LibreOffice의 PDF 변환 엔진에서 **다크 배경(블루 풀블리드) 위 흰 텍스트 + `charSpacing` 양수 값** 조합은 마지막 글자가 잘리는 렌더링 버그가 있습니다. PowerPoint 실제 뷰어에서는 정상이지만 PDF 미리보기에 이슈가 발생합니다.

```javascript
// 다크 모드에서는 charSpacing 0 사용
const navCharSpacing = darkMode ? 0 : 1.5;
const footerCharSpacing = darkMode ? 0 : 1.0;
```

### 11.4 텍스트 잘림 방지

- 텍스트 박스의 `w`(폭)는 들어갈 텍스트 길이의 1.2배 이상 잡습니다.
- `align: "right"` 텍스트는 슬라이드 우측 끝에서 최소 0.4" 안쪽에 배치 (PDF 변환 시 안전 마진).
- 우측 끝점 기준값: **`rightEdge = 12.50"`** (슬라이드 폭 13.333"에서 0.83" 안쪽).

### 11.5 폰트 임베딩 주의

- Pretendard는 시스템 설치 또는 폰트 파일 임베딩이 필요합니다.
- PPTX 생성 시 폰트가 시스템에 없으면 PowerPoint가 대체 폰트로 렌더링하므로, 프레젠테이션 환경(특히 발표 PC)에 Pretendard가 설치되어 있는지 사전 확인.
- macOS/Windows 환경에서 Pretendard 미설치 시 시스템 sans-serif로 fallback.

### 11.6 차트 데이터 라벨

PPTX 네이티브 차트의 `showValue: true`는 기본값이 정수 표시입니다. 소수점 표시가 필요하면 PowerPoint에서 직접 데이터 라벨 형식을 수정해야 합니다(코드로는 한계 있음).

### 11.7 검증 체크리스트

PPTX 파일 생성 후 PowerPoint에서 열기 전 아래 자동 검증 권장:

```python
import zipfile
import re

def validate_pptx(pptx_path):
    issues = []
    with zipfile.ZipFile(pptx_path) as z:
        slide_files = [n for n in z.namelist() if n.startswith("ppt/slides/slide") and n.endswith(".xml")]
        
        for slide_path in slide_files:
            content = z.read(slide_path).decode("utf-8")
            
            # LINE preset 도형 중 cx=0 또는 cy=0 검사
            line_geoms = re.finditer(r'<a:prstGeom prst="line">.*?</p:sp>', content, re.DOTALL)
            for lg in line_geoms:
                sp_start = content.rfind('<p:sp>', 0, lg.start())
                sp_block = content[sp_start:lg.end()]
                ext_match = re.search(r'<a:ext cx="(\d+)" cy="(\d+)"', sp_block)
                if ext_match:
                    cx, cy = int(ext_match.group(1)), int(ext_match.group(2))
                    if cx == 0 or cy == 0:
                        issues.append(f"{slide_path}: LINE with cx={cx} cy={cy}")
    
    return issues
```

---

## 12. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026.05 | 초기 정의 — 9가지 페이지 타입, Olist Blue `#1E40FF`, Pretendard 단일 폰트 시스템 |
| 1.1 | 2026.05 | 컨설팅 덱 페이지 타입 6종 추가 (Type 10–15: Executive Summary, Methodology, Hypothesis Tree, Persona Card, Action Plan Roadmap, Appendix Divider). 디자인 철학에 컨설팅 덱 톤 추가 |
| 1.2 | 2026.05 | PPTX 구현 주의사항 섹션 추가 (LINE 도형 `h: 0` 금지, 사선 헬퍼 함수, 다크 모드 charSpacing 회피 등). 프로젝트 명칭을 "Olist 성장 진단 컨설팅"으로 명확화 |

---

**문의**: 그로스/CRM 팀 주형
