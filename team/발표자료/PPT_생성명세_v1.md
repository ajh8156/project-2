# Olist 재구매 전략 발표 — PPT 생성 명세 v1

> 작성일: 2026-05-08 (D-1)
> 형식: [team/디자인시스템/olist-ppt-prompt.md](../디자인시스템/olist-ppt-prompt.md) v1.2 표준
> 콘텐츠 SSOT: [슬라이드_구성안_v3.md](슬라이드_구성안_v3.md)
> 디자인 시스템: [team/디자인시스템/olist-design-system.md](../디자인시스템/olist-design-system.md) v1.2
>
> ## 사용법
> 본 문서를 통째로 복사해 클로드에게 던지면 PPTX 30장이 생성됩니다.
> 또는 사람이 PPT 직제작 시 슬라이드별 Type·Active Nav·콘텐츠 그대로 따라 만드시면 됩니다.

---

## 0-1. 강조 색상 시스템 (v1.3 갱신)

블루 단색 시스템에서 시각 강도 차이가 필요한 곳에 사용하는 Semantic 색상.

| Role | HEX | 용도 |
|---|---|---|
| 🚨 **Critical** | `#EE1D36` | 위기·부정 (Retention 붕괴, 이탈, 지연) |
| ⚠️ **Warning** | `#FFAE13` | 주의·중간 (Activation 흔들림) |
| ✅ **Success** | `#00D722` | 긍정·달성 (KR 목표 달성, 정시 배송) |

**적용 슬라이드 (현재 코드에 반영됨)**:
- 슬5 3축 신호등 dot — Acquisition `Success` / Activation `Warning` / Retention `Critical`
- 슬20 TF3 KR1 카드 — 목표 4.5%에 `Success ✓`
- 슬22 Journey Map 색대 — 첫경험 `Success` / 재구매 Olist Blue / 이탈방지 `Warning→Critical`
- 슬25 기대효과 표 — 12개월 컬럼 KR1 행에 `Success`

**규칙**:
- 한 슬라이드에 Olist Blue + Semantic 합쳐 최대 3곳
- dot·뱃지·작은 강조 한정 (큰 면적 금지)
- 한 슬라이드에 3색 모두 동시 노출 금지 (정보 혼란)

---

## 0. 변수 치환 (확정값)

```
프로젝트명: OLIST
부제: 재구매 전략
year: 2018                                      ← 컨설팅 수행 연도 (시나리오 시점)
팀명: 데2터로말해조
기간: 2017.01 — 2018.08                         ← 분석 데이터 기간
footer_tagline: NEVER—ENDING · OLIST 재구매 전략
nav_1: Diagnose                                 ← Act 1·2 (도입·현황)
nav_2: Bottleneck                               ← Act 3·3.5·4 (병목·피크·원인)
nav_3: Solution                                 ← Act 5·6 (TF 인트로·실행안)
nav_4: Outcome                                  ← Act 7·8 (결론·CTA·참고)
```

> 📌 컨설팅 시나리오 = 2018년 시점이므로 푸터 연도는 `2018 · NN`. 발표 진행 연도(2026)와 다름.

---

## 1. 슬라이드 ↔ Page Type 매핑 한눈에 (30장)

| 슬# | 제목 | Type | Active Nav | 페이지 # |
|---|---|---|---|---|
| 1 | 표지 — 컨설팅 보고서 커버 | 1 Cover | none | 01 |
| 2 | 의뢰 수령 — Olist의 이메일 | 4 Content | nav_1 Diagnose | 02 |
| 3 | 우리 — 데2터로말해조 | 11 Methodology | nav_1 Diagnose | 03 |
| 4 | 결론 먼저 — 재구매 구조가 없습니다 | **10 Executive Summary** | nav_1 Diagnose | 04 |
| 5 | 3축 신호등 진단 | 4 Content | nav_1 Diagnose | 05 |
| 6 | RFM 세그먼테이션 (4분면) | 8 Chart | nav_1 Diagnose | 06 |
| 7 | KPI Tree × AARRR 병합 | **12 Hypothesis Tree** | nav_2 Bottleneck | 07 |
| 8 | 저평점 원인 분해 (4팀 분산) | 8 Chart | nav_2 Bottleneck | 08 |
| 9 | 🔥 5점 편향 — "5점은 배송이 만든다" | **7 Quote/Stat** | nav_2 Bottleneck | 09 |
| 10 | Finding 3개 + 가설 검증 | 4 Content | nav_2 Bottleneck | 10 |
| 11 | TF의 정당성 | 4 Content | nav_3 Solution | 11 |
| 12 | 5팀 × 3TF 협업 매트릭스 | 8 Chart (표) | nav_3 Solution | 12 |
| 13 | 이중 트랙 구조도 | 6 Timeline | nav_3 Solution | 13 |
| 14 | TF1 ① 지표·목표 | 4 Content | nav_3 Solution | 14 |
| 15 | TF1 ② 병목 해결 Before/After | **5 Comparison** | nav_3 Solution | 15 |
| 16 | TF1 ③ 결과물 (지도·번들·교육) | 4 Content | nav_3 Solution | 16 |
| 17 | TF2 ① 지표·목표 | 4 Content | nav_3 Solution | 17 |
| 18 | TF2 ② 병목 해결 Before/After | **5 Comparison** | nav_3 Solution | 18 |
| 19 | TF2 ③ 결과물 4종 | 4 Content | nav_3 Solution | 19 |
| 20 | TF3 ① 지표·목표 (KR1 4.5% ★) | 4 Content | nav_3 Solution | 20 |
| 21 | TF3 ② 병목 해결 Before/After | **5 Comparison** | nav_3 Solution | 21 |
| 22 | TF3 ③ Lifecycle Journey Map ★ | **6 Timeline** | nav_3 Solution | 22 |
| 23 | TF3 ④ 결과물 4종 + CRM best-of | 4 Content | nav_3 Solution | 23 |
| 24 | 결론 재선언 (Before/After) | **5 Comparison** | nav_4 Outcome | 24 |
| 25 | 기대효과 — 3열 시계열 | 8 Chart (표) | nav_4 Outcome | 25 |
| 26 | CTA — Olist가 내일부터 할 일 (4단) | **14 Action Plan Roadmap** | nav_4 Outcome | 26 |
| 27 | Looker Studio 대시보드 | 8 Chart | nav_4 Outcome | 27 |
| 28 | 추가 분석 자료 인덱스 | 4 Content | nav_4 Outcome | 28 |
| 29 | THANK YOU | **9 Closing** | none | 29 |
| 30 | Q&A | 9 Closing 변형 | none | 30 |

---

## 2. 슬라이드 명세 — Slide 1 ~ 30

### Slide 1: [Type 1 - Cover]
- Active Nav: none
- Content:
  - Mega Text: "OLIST"
  - Meta: "2017.01 — 2018.08  ·  데2터로말해조"
  - Lead: "올리스트 성장 진단 컨설팅 보고서. 이탈률 개선을 위한 액션플랜."

---

### Slide 2: [Type 4 - Content] — 변형: 좌측 mega + 우측 이메일 카드
- Active Nav: nav_1 Diagnose
- Content:
  - Title (좌, 멀티라인 mega): "AN <accent>EMAIL</accent>  FROM  OLIST"
  - Lead (좌측 하단): "2018.04.10 — Olist Growth Director Carlos Silva로부터 의뢰가 도착했습니다."
  - Email Card (우측, 받은 메일함 UI):
    - From: `Carlos Silva <carlos.silva@olist.com>` / Olist Growth Director
    - To: `데2터로말해조 컨설팅`
    - 제목: `[의뢰] 성장 정체 진단 — 이탈률 개선의 건`
    - 본문: 안녕하세요. 올리스트 Growth Team의 Carlos Silva입니다.
      최근 1년간 신규 가입자는 꾸준히 늘었지만, 매출 성장이 눈에 띄게 둔화되었습니다.
      특히 한 번 구매하고 돌아오지 않는 고객이 너무 많습니다.
      "성장이 정체되고 있는 우리를 진단해주세요."
    - 서명: Carlos Silva / Growth Director, Olist

---

### Slide 3: [Type 11 - Methodology] — 변형: 5단계 → 4분면 (팀 카드)
- Active Nav: nav_1 Diagnose
- Content:
  - Page Title: "WHO WE ARE — <accent>DATA2-RO MAL-HAE-JO</accent>"
  - Lead: "외부 데이터 컨설팅팀 6인이 의뢰를 측정 가능한 KPI로 정제했습니다."
  - 4 Cards (가로 4열, 각 카드 = 단계 박스 변형):
    - Card 01 — TEAM (Gray Tint):
      - Number: 01
      - Title: "TEAM"
      - Desc: "기획자 중심 6인"
      - Tools: "외부 컨설팅 — 독립 분석"
    - Card 02 — TOOLS (Gray Tint):
      - Number: 02
      - Title: "TOOLS"
      - Desc: "BigQuery · Looker · Python"
      - Tools: "Pandas · matplotlib"
    - Card 03 — DATASET (Gray Tint):
      - Number: 03
      - Title: "DATASET"
      - Desc: "Olist BR E-Commerce + Marketing Funnel"
      - Tools: "11 tables · 99,441 orders"
    - Card 04 — MISSION (Blue Tint, Highlight):
      - Number: 04
      - Title: "MISSION"
      - Desc 1: "받은 일 — 이탈률 개선"
      - Desc 2: "제안 목표 — KR1 재구매율 3.0% → 4.5%"
  - Bottom Meta: "DATA SCOPE — 2017.01 — 2018.08"

---

### Slide 4: [Type 10 - Executive Summary]
- Active Nav: nav_1 Diagnose
- Content:
  - Page Title: "<accent>NO REPURCHASE</accent>  STRUCTURE"
  - Lead: "Olist 재구매 진단 결과 — 한 장 요약. 100명 중 0.5명만 돌아옵니다."
  - 3 Cards (SCR):
    - SITUATION (Gray):
      - Headline: "재구매율 3.00%"
      - Body: "100명 중 97명이 한 번 사고 돌아오지 않습니다. 매출 94%가 일회성 고객 의존."
      - Stat Label: "재구매 주문 비중"
      - Stat Value: "6.13%"
    - COMPLICATION (Gray 800):
      - Headline: "BF cohort 0.56%"
      - Body: "작년 BF로 만든 고객조차 30일 내 재구매율이 0.56%. 마케팅 비용 회수 불가."
      - Stat Label: "BF 30일 재구매율"
      - Stat Value: "0.56%"
    - RESOLUTION (Blue):
      - Headline: "TF 3개로 재구매 구조를 만든다"
      - Body: "배송 품질 + 첫 경험 + 재구매 유도 — 3개 TF로 KR1 재구매율 4.5% 달성."
      - Stat Label: "1년 목표 KR1"
      - Stat Value: "4.5%"
  - Read More: "Diagnose → Section 01  ·  Bottleneck → Section 02  ·  Solution → Section 03"

---

### Slide 5: [Type 4 - Content] — 변형: 3카드 (3축 신호등)
- Active Nav: nav_1 Diagnose
- Content:
  - Page Title: "THREE  <accent>SIGNALS</accent>"
  - Lead: "AARRR 3축으로 본 Olist의 현재. 숫자 3개로 끝납니다."
  - 3 Cards (가로):
    - Card 1 — Acquisition (Gray Tint, 옅은 dot):
      - Label: "ACQUISITION"
      - Number: "93,104"
      - Desc: "규모는 충분하다 — 신규 유입 정상"
    - Card 2 — Activation (Gray Tint, 중간 dot):
      - Label: "ACTIVATION"
      - Number: "8.16% / 12.82%"
      - Desc: "배송 지연·저평점 — 첫 경험이 흔들린다"
    - Card 3 — Retention (Blue Tint, 진한 dot ★):
      - Label: "RETENTION"
      - Number: "3.0%"
      - Desc: "돌아오지 않는다 — 진짜 병목은 여기"
  - Bottom Highlight Box: "들어오는 건 잘 되고, 첫 경험이 흔들리고, 다시 안 옵니다."

---

### Slide 6: [Type 8 - Data Table/Chart] — RFM 4분면 산점도
- Active Nav: nav_1 Diagnose
- Content:
  - Page Title: "RFM  <accent>SEGMENTATION</accent>"
  - Meta (우측): "RECENCY × FREQUENCY  ·  N=93,104"
  - Lead: "이탈재구매 2,562명 — 우리가 회복할 수 있는 우선 타겟."
  - Chart: 2D 산점도 (X: Recency, Y: Frequency)
    - 4분면 라벨:
      - 우상 — 충성 고객 (유지)
      - **좌상 — 이탈재구매 2,562명 ★** (Olist Blue 강조 영역)
      - 우하 — 신규 (양육)
      - 좌하 — 이탈 (포기)
    - 점 색상: Olist Blue 단색 (강조 영역만 진하게)
  - Insight Box (Blue Tint): "이탈재구매 2,562명 → 10% 전환 시 +256명 충성 고객 확보"

---

### Slide 7: [Type 12 - Hypothesis Tree (MECE)]
- Active Nav: nav_2 Bottleneck
- Content:
  - Page Title: "BOTTLENECK  <accent>DECOMPOSITION</accent>"
  - Lead: "수식 병목과 여정 병목이 같은 지점에서 만난다 — Retention."
  - Tree Structure:
    - **Root (좌, 블루)**: "GMV 정체의 핵심 병목"
    - **Level 1 (중, 3노드)**:
      - 노드 1: "Acquisition — 정상 ✅"
      - 노드 2: "Activation — 흔들림 ⚠️"
      - 노드 3 (Highlight): "Retention — 붕괴 🚨"
    - **Level 2 (우, 세부)**:
      - 1.1 신규 유입 93,104명 (정상 규모)
      - 2.1 첫 구매 배송 지연 8.16%
      - 2.2 첫 구매 저평점 12.82%
      - 3.1 재구매율 3.0% (Highlight ★)
      - 3.2 BF cohort 30일 0.56% (Highlight ★)
      - 3.3 Frequency 1.0334 — 수식 병목 = 여정 병목
  - MECE Check: "수식(GMV = Customers × Frequency)이 가리키는 병목과 여정(AARRR)이 가리키는 병목은 같은 지점 — Retention입니다."

---

### Slide 8: [Type 8 - Data Table/Chart] — 저평점 원인 분포
- Active Nav: nav_2 Bottleneck
- Content:
  - Page Title: "<accent>FOUR TEAMS,</accent>  ONE PROBLEM"
  - Meta (우측): "저평점 원인 분포  ·  N=12,847"
  - Lead: "한 팀이 못 푸는 분포 — TF로 묶어야 하는 정당성."
  - Chart: 100% 누적 막대 (가로) 또는 도넛
    - 미배송/배송 지연 — 42% (물류) — Olist Blue
    - CS 무응답 — 20% (CX) — Gray 800
    - 상품 기대 불일치 — 20% (Seller Ops) — Gray 600
    - UX 문제 — 18% (Product) — Gray 400
  - Insight Box: "원인이 4개 팀에 분산 — 한 팀 단독으로 못 푼다. TF 재편의 근거."

---

### Slide 9: [Type 7 - Quote/Stat] 🔥 발표 정점
- Active Nav: nav_2 Bottleneck
- Content:
  - Meta (상단): "CORE INSIGHT  ·  RATING × REPURCHASE"
  - Mega Number: "<accent>3.12%</accent>"
  - Headline: "5점 리뷰만 재구매를 만든다"
  - Body: "1점·2점·3점·4점 리뷰 모두 재구매율 ~2.5% 동일. 5점만 3.12%. 그리고 5점을 만드는 것은 정시 배송(3.04%) — 지연 시 2.51%."
  - Bottom Quote: "재구매 구조의 뿌리는 배송 경험이다."
  - Caption (하단): "SOURCE: Olist Reviews × Repurchase Linkage  ·  N=99,441"

---

### Slide 10: [Type 4 - Content] — Finding 통합 표
- Active Nav: nav_2 Bottleneck
- Content:
  - Page Title: "THREE  <accent>FINDINGS,</accent>  THREE TFs"
  - Lead: "3가지 원인이 보입니다. 그런데 이 3가지는 모두 한 팀에서 못 풉니다."
  - Table (3행):
    - 행 1: ① 배송 지연 / 정시 3.04% vs 지연 2.51% (-0.53%p) / H1 ✅ / **TF1**
    - 행 2: ② 5점 편향 / 1~4점 동일 / 5점만 3.12% / H2 ✅ / **TF2**
    - 행 3 (Highlight): ③ 재구매 유도 부재 / CRM·추천·쿠폰 인프라 전무 / H3 ✅ / **TF3 ★**
  - Highlight Box: "각 원인은 각각 다른 TF의 책임 영역. 다음 장부터 TF 정당성과 실행안을 보여드립니다."

---

### Slide 11: [Type 4 - Content] — TF 정당성
- Active Nav: nav_3 Solution
- Content:
  - Page Title: "WHY  <accent>TF</accent>,  NOT TEAMS"
  - Lead: "저평점 원인 4팀 분산 + 재구매 Journey 7터치포인트 분산 = TF 재편 정당성."
  - 좌측: 슬8 4팀 분산 차트 미니 (참고용 작은 사이즈)
  - 우측: TF 매핑 (3 카드)
    - TF1 — 물류 · Seller Ops · CX (저평점 42% 영역)
    - TF2 — Product · 물류 · CX · SO (공동 책임 100%)
    - TF3 ★ (Highlight) — CRM · Product · MD (KR1 재구매율 직접 책임)
  - Highlight Box: "TF3는 우리 발표의 핵심 KR(재구매율 4.5%)을 직접 책임지는 TF입니다."

---

### Slide 12: [Type 8 - Data Table/Chart] — 5팀×3TF 매트릭스
- Active Nav: nav_3 Solution
- Content:
  - Page Title: "FIVE TEAMS  <accent>×</accent>  THREE TFs"
  - Lead: "3-Core 팀이 각 TF 리드, Support 2팀(SO·MD)이 교차 보조."
  - Matrix Table (5행 × 3열, 셀에 리드/보조 마킹):
    - CRM × TF1 = – / TF2 = – / **TF3 = 🔵 리드 ★**
    - Product × TF1 = 보조 / **TF2 = 🔵 리드 ★** / TF3 = 보조
    - Logistics × **TF1 = 🔵 리드 ★** / TF2 = 보조 / TF3 = –
    - Seller Ops × TF1 = 보조 / TF2 = 보조 / TF3 = –
    - MD × TF1 = – / TF2 = – / TF3 = 보조
  - Bottom Note: "매트릭스 셀에 책임 표시 — 발표 시 TF3 컬럼 강조."

---

### Slide 13: [Type 6 - Timeline] — 이중 트랙
- Active Nav: nav_3 Solution
- Content:
  - Page Title: "<accent>DUAL TRACK</accent>  TO 4.5%"
  - Lead: "TF는 BF로 증명, 구조 개선은 1년으로 완성. 둘 다 KR1 4.5%로 수렴."
  - Timeline (가로 5단계, Now → BF → 6M → 12M):
    - 01 Now (3M) — TF 셋업
    - 02 BF (6M) — BF cohort 1.5~2.0% 검증 ★
    - 03 12M (1년) — KR1 재구매율 4.5% 달성 (Olist Blue 강조)
  - Sub-timeline: 단기 트랙(TF1·2·3) + 장기 트랙(물류 3PL · SO 등급제 · MD 번들)
  - Bottom Quote: "두 트랙 모두 KR1 4.5%로 수렴 — 그 수렴점을 직접 책임지는 게 TF3."

---

### Slide 14: [Type 4 - Content] — TF1 ① 지표·목표
- Active Nav: nav_3 Solution
- Content:
  - Page Title: "TF1  <accent>DELIVERY</accent>"
  - Meta: "AARRR — ACTIVATION 🚨  ·  KR4 책임 (간접)"
  - 2 Stats:
    - KR4 첫 구매 배송 지연율: 8.16% → **6.0%**
    - KR2 BF 기간 전체 지연율: 20.93% → **15.0% 이하**
  - Milestone Timeline (3M / 6M / 12M):
    - 3M — 지연 다발 셀러 모니터링
    - 6M — 북동부 3PL 파트너십
    - 12M — Total Lead Time 12.1일 → 8일

---

### Slide 15: [Type 5 - Comparison] — TF1 Before/After
- Active Nav: nav_3 Solution
- Content:
  - Page Title: "TF1  <accent>BEFORE</accent>  /  AFTER"
  - Meta: "병목 — BF 7.94배 폭증으로 지연율 20.93% 도달"
  - 좌 Before (Gray):
    - Label: "BEFORE — 평시 / BF"
    - Headline: "지연율 8.16% / 20.93%"
    - Body: "BF 주문량 7.94배 폭증 시 지연율 통제 불가. 첫 구매 고객 대량 이탈."
    - Stat: 8.16% / 20.93%
  - 우 After (Blue):
    - Label: "AFTER — TF1 가동"
    - Headline: "지연율 6.0% / 15.0% 이하"
    - Body: "지연 셀러 모니터링 + 북동부 3PL + Lead Time 단축 — 평시·BF 모두 통제."
    - Stat: 6.0% / 15.0%

---

### Slide 16: [Type 4 - Content] — TF1 결과물
- Active Nav: nav_3 Solution
- Content:
  - Page Title: "TF1  <accent>OUTPUTS</accent>"
  - Lead: "지역별 지연율 지도 + 셀러 교육 + MD 묶음 배송 번들."
  - 3 Output Boxes:
    - Output 1 — 브라질 지도 4종 (이미지 삽입: tf1-brazilmap1~4.png)
      - 지연율 / 셀러 수 / Gap / 1P 임시 방편
    - Output 2 — 셀러 교육 (PPT 도형 압축):
      - A 신규 (첫 30일 가이드) / B 기존 (지연 vs 리뷰) / C 위험 (1점 대응) / D VIP (전담 AM)
      - Fast-Ship 인증 태깅 → 상단 노출 베네핏
    - Output 3 — MD 묶음 배송 번들 (이미지 3종)
  - Highlight Box: "MD 팀 협업 — 묶음 배송으로 BF 배송비 부담 흡수."

---

### Slide 17: [Type 4 - Content] — TF2 ① 지표·목표
- Active Nav: nav_3 Solution
- Content:
  - Page Title: "TF2  <accent>EXPERIENCE</accent>"
  - Meta: "AARRR — ACTIVATION ⚠️  ·  KR5 책임 (간접) · 4팀 공동 KR"
  - Stat: 첫 구매 저평점 비중: 12.82% → **10.5%**
  - Sub-KRs (팀별 기여):
    - 물류 — KR4 8.16% → 6.0%
    - CX — 48시간 대응률 90% 달성
    - SO — 위험셀러 4.0점 23명 中 15명
  - Milestone (3M/6M/12M): PDP 신뢰 → Thank-you → 상품 정보 표준화

---

### Slide 18: [Type 5 - Comparison] — TF2 Before/After
- Active Nav: nav_3 Solution
- Content:
  - Page Title: "TF2  <accent>BEFORE</accent>  /  AFTER"
  - Meta: "병목 — 저평점 원인 4팀 분산"
  - 좌 Before (Gray):
    - Label: "BEFORE"
    - Headline: "책임 모호 (12.82%)"
    - Body: "원인 4팀 분산 → 한 팀 단독 풀이 불가, 책임 소재 모호."
  - 우 After (Blue):
    - Label: "AFTER — TF2"
    - Headline: "공동 KR 1 + 기여 KR 4 (10.5%)"
    - Body: "유저 만족 ↑ → 평점 ↑ → 재구매 (TF3 핸드오프). 월 1회 합동 리뷰."
  - Bottom Data: tf2-data-rating-by-category.png 미니 차트

---

### Slide 19: [Type 4 - Content] — TF2 결과물 4종
- Active Nav: nav_3 Solution
- Content:
  - Page Title: "TF2  <accent>OUTPUTS</accent>"
  - Lead: "PDP 신뢰 + CX SLA + Thank-you + BF 랜딩 — 4종 산출물."
  - 4 Cards (2×2):
    - ① PDP Before/After (이미지: tf2-pdp-hero-soft-curve.png 등)
    - ② CX 48h SLA (이미지: tf2-cx-sla-90percent.png) — "6h 배정 → 90% 달성"
    - ③ Thank-you 4채널 (이미지: tf2-thankyou-after.png) — "D+0~D+60 → TF3 핸드오프"
    - ④ 블프 프로모션 랜딩 (이미지 ref: tf2-bf-ref-gmarket-blackprime.png)

---

### Slide 20: [Type 4 - Content] — TF3 ① 지표·목표 ★
- Active Nav: nav_3 Solution
- Content:
  - Page Title: "TF3  <accent>RETENTION ★</accent>"
  - Meta: "AARRR — RETENTION 🚨  ·  KR1·KR3 직접 책임 ★"
  - 3 Stats (KR1 1.5배 강조):
    - **KR1 재구매율: 3.0% → 4.5% ★** (가장 큰 게이지)
    - KR3 재구매 주문 비중: 6.13% → 9.0%
    - BF-KR5 BF 30일 재구매: 0.56% → 1.5~2.0%
  - Milestone: 3M D+7 푸시 → 6M D+30 자동화 → 12M 7터치포인트 자동화
  - Highlight Box: "발표 핵심 KR 3개를 직접 책임지는 TF — 비중 2분."

---

### Slide 21: [Type 5 - Comparison] — TF3 Before/After
- Active Nav: nav_3 Solution
- Content:
  - Page Title: "TF3  <accent>BEFORE</accent>  /  AFTER"
  - Meta: "병목 — 재구매 유도 인프라 전무 (CRM·추천·쿠폰 모두 없음)"
  - 좌 Before (Gray):
    - Label: "BEFORE"
    - Headline: "구매 완료 → 공백 → 97% 이탈"
    - Body: "CRM·추천·쿠폰 인프라 전무. 첫 구매 후 어떤 훅도 없음."
  - 우 After (Blue):
    - Label: "AFTER — TF3"
    - Headline: "7터치포인트 가동, 코호트 자동화"
    - Body: "D+0~D+90 라이프사이클 자동화. CRM + MD + Product 협업으로 재방문 트리거."
  - Quote (정점): "앞 모든 분석이 결국 한 가지로 수렴 — 재구매 인프라가 아예 없다는 사실입니다."

---

### Slide 22: [Type 6 - Timeline] — TF3 Lifecycle Journey Map ★ 발표 시각 정점
- Active Nav: nav_3 Solution
- Content:
  - Page Title: "<accent>LIFECYCLE</accent>  JOURNEY MAP"
  - Meta: "7 TOUCHPOINTS  ·  D+0 → D+90"
  - Timeline (7단계, 가로 풀폭, 색대 그라데이션):
    - 01 첫구매 (Olist Blue)
    - 02 D+0 — Thank-you (Blue Tint, 🟢 첫경험)
    - 03 D+3 — 만족도 체크 (Blue Tint, 🟢)
    - 04 D+7 — 앱푸시 (Olist Blue, 🟢→🟡 재구매 시작)
    - 05 D+30 — 카카오 + 이메일 (Olist Blue, 🟡 재구매 본격)
    - 06 D+60 — 카카오 시크릿 (Gray, 🟡→🔴 이탈 방지)
    - 07 D+90 — 윈백 캠페인 (Gray, 🔴 이탈 직전)
  - Stage Labels (상단 띠): 첫경험 확보 / 재구매 유도 / 이탈 방지
  - Team Labels (하단 띠): Prod+물류→CRM / CRM+MD / CRM+Prod
  - Bottom Quote: "이게 우리가 만들 7터치포인트 라이프사이클 — D+0부터 D+90까지 자동으로 굴러갑니다."

---

### Slide 23: [Type 4 - Content] — TF3 결과물 4종
- Active Nav: nav_3 Solution
- Content:
  - Page Title: "TF3  <accent>OUTPUTS</accent>"
  - Lead: "CRM 목업 best-of 3장 + 번들 + 셀러 다각화 + BF 코호트 추적."
  - 상단 — CRM Best-of 3장 (가로 그리드, 모바일 mockup):
    - tf3_D07_push_A.png (D+7 인테리어 가이드 콘텐츠 훅)
    - tf3_D30_kakao.png (D+30 카카오 플친)
    - tf3_D32_kakao.png (D+32 이탈 직전 마지막 훅)
  - 하단 — 4종 산출물 (2×2):
    - ② 번들 카드 (tf3-bundle-bedding-set.png + 2차 구매 쿠폰 시안)
    - ③ 셀러 다각화 (tf3-seller-diversification.png)
    - ④ BF 코호트 추적 (tf3-bf-cohort-tracking.png)
    - ⑤ Caption: "이 4가지가 7터치포인트의 실체"

---

### Slide 24: [Type 5 - Comparison] — 결론 재선언
- Active Nav: nav_4 Outcome
- Content:
  - Page Title: "FROM  <accent>NO STRUCTURE</accent>  TO 4.5%"
  - Meta: "결론 재선언 — 슬라이드 4와 같은 카드, 다른 답"
  - 좌 Before (Gray, 슬4 시각 그대로):
    - Label: "BEFORE — 슬4의 결론"
    - Headline: "재구매 구조가 없습니다"
    - Stats: 3.0% / 0.56% / 6.13%
  - 우 After (Blue):
    - Label: "AFTER — TF 3개로"
    - Headline: "재구매 구조를 만듭니다"
    - Stats: 4.5% / 1.5~2.0% / 9.0%
  - Bottom Quote: "슬라이드 4에서 드린 결론을 다시 한 번 — 우리는 이렇게 풀겠습니다."

---

### Slide 25: [Type 8 - Data Table/Chart] — 기대효과 3열 시계열
- Active Nav: nav_4 Outcome
- Content:
  - Page Title: "<accent>EXPECTED</accent>  IMPACT"
  - Meta: "3M / 6M / 12M  ·  By 책임 TF"
  - Lead: "3개월 = TF 성과, 6~12개월 = 장기 구조 개선 성과."
  - Table (7행 × 5열, 상단 3행 TF3 좌측 색띠 강조):
    - **★ TF3 KR1 재구매율: 3.0% → 3.5% → 4.0% → 4.5%**
    - ★ TF3 BF 30일 재구매: 0.56% → 1.5~2.0%
    - ★ TF3 KR3 재구매 주문 비중: 6.13% → 7.0% → 8.0% → 9.0%
    - TF1 첫 구매 지연율: 8.16% → 7.0% → 6.5% → 6.0%
    - TF1 (장기) Total Lead Time: 12.1일 → 10일 → 8일
    - TF2 첫 구매 저평점: 12.82% → 11.8% → 11.0% → 10.5%
    - TF1 (셀러) 위험 셀러 4.0점: 0/23 → 5/23 → 15/23
  - Insight: "상단 3행 = TF3 책임. 발표 핵심 KR 모두 TF3에 귀속."

---

### Slide 26: [Type 14 - Action Plan Roadmap] — CTA 4단
- Active Nav: nav_4 Outcome
- Content:
  - Page Title: "<accent>OLIST</accent>  STARTS TOMORROW"
  - Meta: "4-PHASE ROLLOUT  ·  Week 1 → 1년"
  - Roadmap (2D 그리드, X축: Week 1 / Month 1 / BF / Year 1):
    - Row 1 — TF1 DATA: 배송 지연 모니터링 / Fast-Ship 300곳 / BF 검증 / 3PL 5개 지역 (H/H/H/H)
    - Row 2 — TF2 SEGMENT: PDP A/B / Metric Dictionary v1 / 번들 UI 배포 / 셀러 등급제 정착 (M/H/H/M)
    - Row 3 — **TF3 TRIGGER ★**: D+7 시나리오 승인 / D+7·D+30 CRM 런칭 / BF 1.5~2.0% 검증 / **KR1 4.5% 달성** (H/H/H/H)
  - Milestone:
    - ⭐ Week 4: 첫 트리거 캠페인
    - ⭐ BF (Month 6): cohort 1.5~2.0% 검증
    - ⭐ Year 1: KR1 4.5%
  - Bottom Quote: "재구매 구조는 선언이 아니라, 이 박스들의 실행에서 만들어집니다."

---

### Slide 27: [Type 8 - Data Table/Chart] — Looker Studio 대시보드
- Active Nav: nav_4 Outcome
- Content:
  - Page Title: "<accent>LIVE</accent>  DASHBOARD"
  - Meta (우상): "AARRR + KR 통합  ·  자료 URL/QR"
  - Lead: "발표 후 자유롭게 열람 가능 — Looker Studio 대시보드로 실시간 추적."
  - Body: 대시보드 풀 캡처 (8할) + 우상단 QR 카드 (확정 후 삽입)
  - Caption: "URL · 발표 직전 확정"

---

### Slide 28: [Type 4 - Content] — 추가 분석 자료 인덱스
- Active Nav: nav_4 Outcome
- Content:
  - Page Title: "<accent>FURTHER</accent>  READING"
  - Lead: "발표에서 다 못 보여드린 분석들 — Q&A 대응용."
  - 2 Columns:
    - 좌단 — 메인 분석 (목록):
      - 지역×카테고리 교차분석
      - 리뷰 감성분석
      - ARR 상세 지표 테이블
      - H2 가설 검증
      - 코호트 생존 곡선
      - TF4 (셀러 통합) · TF5 (측정 통일)
    - 우단 — 부록 (목록):
      - A-1. AI 파이프라인 + 팀원 R&R
      - A-2. 회고
      - A-4. TF 충돌 사례 카드

---

### Slide 29: [Type 9 - Closing]
- Active Nav: none
- Content:
  - Mega Text: "THANK YOU"
  - Lead: "Never-ending stories start here."
  - Meta (하단): "데2터로말해조  ·  6인 외부 컨설팅"

---

### Slide 30: [Type 9 - Closing 변형] — Q&A
- Active Nav: none
- Content:
  - Mega Text: "Q & A"
  - Lead: "질문 받겠습니다."
  - Meta (하단): "데2터로말해조  ·  growth@olist.com"

---

## 3. 전달 시 사용할 PPT 생성 프롬프트 (한 번에 통째로 복사)

> 이 섹션을 그대로 복사 → 클로드에게 던지면 PPTX 생성됨.

```
당신은 Olist Presentation Design System v1.2를 따르는 PPT 디자이너입니다.
team/디자인시스템/olist-design-system.md 와 team/디자인시스템/olist-ppt-prompt.md 의
모든 규칙(컬러 #1E40FF, Pretendard 단일, 16:9 1920×1080, Page Type 15종, PPTX 무결성)을 준수해
30장 PPTX를 생성해주세요.

[변수 치환]
프로젝트명: OLIST
부제: 재구매 전략
year: 2018
팀명: 데2터로말해조
기간: 2017.01 — 2018.08
footer_tagline: NEVER—ENDING · OLIST 재구매 전략
nav_1: Diagnose
nav_2: Bottleneck
nav_3: Solution
nav_4: Outcome

[슬라이드 명세]
(위 §2 Slide 1 ~ Slide 30 전체 복사 붙여넣기)

[산출 형식]
1. PPTX 파일 생성 (python-pptx 또는 pptxgenjs)
2. 파일명: olist_repurchase_strategy_v1.pptx
3. /mnt/user-data/outputs/ 경로 저장
4. 생성 후 present_files 호출

[QA]
- olist-design-system.md §11 PPTX 구현 주의사항 모두 준수
- LINE 도형 cx>0, cy>0 검증
- 다크 슬라이드(슬2 풀블리드 X — 슬1·29·30만 다크) charSpacing 0
- 우측 정렬 텍스트 rightEdge 12.50" 안쪽
```

---

## 4. 관련 문서

- [슬라이드_구성안_v3.md](슬라이드_구성안_v3.md) — 발표 멘트·스토리 SSOT
- [PPT_제작시트_v1.md](PPT_제작시트_v1.md) — PPT 직제작 시 참고용 콘텐츠 시트
- [슬라이드_산출물_매칭표_v1.md](슬라이드_산출물_매칭표_v1.md) — 산출물 인벤토리
- [_template/tokens.css](_template/tokens.css) — 디자인 토큰 v1.2 정확값
- [_template/page-types.html](_template/page-types.html) — Page Type 15종 입타
- [team/디자인시스템/olist-design-system.md](../디자인시스템/olist-design-system.md) — 디자인 시스템 v1.2 SSOT
- [team/디자인시스템/olist-ppt-prompt.md](../디자인시스템/olist-ppt-prompt.md) — PPT 생성 프롬프트 표준
