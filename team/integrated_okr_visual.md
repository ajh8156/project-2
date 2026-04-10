# Olist 전사 통합 OKR — 요약 시각화

> **작성일**: 2026-04-10  
> **상세 문서**: [integrated_okr_plan.md](integrated_okr_plan.md)

---

## 핵심 요약: 전사가 반드시 알아야 할 것

### 우리의 문제

Olist는 고객을 못 데려오는 회사가 아니다. **데려온 고객이 다시 오지 않는 구조**가 문제다.

| 지표 | 수치 | 의미 |
|------|------|------|
| 구매 고객 수 | 93,104명 | 유입은 충분하다 |
| 재구매 고객 수 | 2,789명 (3.00%) | **97%가 한 번 사고 떠난다** |
| 고객당 평균 주문 수 | 1.0334 | 거의 1회로 끝난다 |
| 재구매 주문 비중 | 6.13% | 매출의 94%가 일회성 고객에 의존 |

### 우리의 방향

**"신규 유입 의존형 성장에서 벗어나, 고객이 다시 구매하는 구조를 만든다"**

### 전사 공식 수치 — 모든 팀이 이 숫자를 쓴다

| 지표 | 현재 | 3개월 | 6개월 | 1년 |
|------|------|-------|-------|-----|
| 재구매율 | 3.00% | 3.5% | 4.0% | **4.5%** |
| 고객당 주문 수 | 1.0334 | - | 1.05 | **1.06** |
| 재구매 주문 비중 | 6.13% | 7.0% | 8.0% | **9.0%** |
| 첫 구매 배송 지연율 | 8.16% | 7.0% | 6.5% | **6.0%** |
| 첫 구매 저평점 비중 | 12.82% | 11.8% | 11.0% | **10.5%** |

> **원칙**: 팀별 문서에서 위와 다른 수치를 쓰고 있다면 즉시 수정한다.

### Black Friday는 매출 행사가 아니라 재구매 cohort 확보 행사다

BF에서 아무리 매출을 올려도, 그 고객이 12~1월에 다시 사지 않으면 전사 OKR에 기여하지 못한다.

### 재구매는 한 팀의 문제가 아니다

CRM이 메시지를 보내도, 물류가 지연되거나, 상품 품질이 낮거나, CX가 늦게 대응하면 재구매 구조는 만들어지지 않는다.  
따라서 **각 팀이 혼자 할 것**과 **같이 할 것(TF)**을 명확히 나눠서 움직인다.

---

## 1. 전사 OKR 구조도

```mermaid
flowchart TD
    O["<b>Objective</b><br/>신규 유입 의존형 성장에서 벗어나<br/>고객이 다시 구매하는 구조를 만든다"]

    O --> KR1["<b>KR1 재구매율</b><br/>3.00% → 4.5% (1년)"]
    O --> KR2["<b>KR2 고객당 주문 수</b><br/>1.0334 → 1.06 (1년)"]
    O --> KR3["<b>KR3 재구매 주문 비중</b><br/>6.13% → 9.0% (1년)"]
    O --> KR4["<b>KR4 첫 구매 배송 지연율</b><br/>8.16% → 6.0% (1년)"]
    O --> KR5["<b>KR5 첫 구매 저평점 비중</b><br/>12.82% → 10.5% (1년)"]
    O --> G1["<b>Guardrail 1</b><br/>신규 구매 고객 수 유지"]
    O --> G2["<b>Guardrail 2</b><br/>AOV 하락 방지"]

    KR1 --- T1["CRM · Product · MD"]
    KR2 --- T2["CRM · Product · MD"]
    KR3 --- T3["CRM · MD"]
    KR4 --- T4["물류"]
    KR5 --- T5["Product · CX · Seller Ops"]

    style O fill:#1a73e8,color:#fff,stroke:none
    style KR1 fill:#34a853,color:#fff,stroke:none
    style KR2 fill:#34a853,color:#fff,stroke:none
    style KR3 fill:#34a853,color:#fff,stroke:none
    style KR4 fill:#fbbc04,color:#000,stroke:none
    style KR5 fill:#fbbc04,color:#000,stroke:none
    style G1 fill:#ea4335,color:#fff,stroke:none
    style G2 fill:#ea4335,color:#fff,stroke:none
```

> KR1~3(녹색)은 **재구매 성과 지표**, KR4~5(노란색)은 **선행 품질 지표**, G1~2(빨간색)은 **방어선**이다.

---

## 2. 팀 운영 구조

```mermaid
flowchart TD
    TOP["<b>전사 OKR</b><br/>1년 방향"]

    TOP --> SHORT["<b>단기 실행 그룹</b><br/>3개월 rolling"]
    TOP --> LONG["<b>구조 개선 그룹</b><br/>6개월~1년"]
    TOP --> TF["<b>협업 TF</b><br/>팀 간 교차 실행"]

    SHORT --> CRM["CRM/마케팅"]
    SHORT --> PROD["Product/UX"]
    SHORT --> MD["MD"]
    SHORT --> CX["CX"]

    LONG --> LOG["물류/SCM"]
    LONG --> SELL["Seller Ops"]

    TF --> TF1["<b>TF1</b> BF 통합 전략<br/><i>리드: CRM</i>"]
    TF --> TF2["<b>TF2</b> 첫 구매 경험 개선<br/><i>리드: Product</i>"]
    TF --> TF3["<b>TF3</b> 재구매 Lifecycle<br/><i>리드: CRM</i>"]
    TF --> TF4["<b>TF4</b> 셀러 품질 통합<br/><i>리드: Seller Ops</i>"]
    TF --> TF5["<b>TF5</b> 측정 체계 통일<br/><i>리드: Data/BI</i>"]

    style TOP fill:#1a73e8,color:#fff,stroke:none
    style SHORT fill:#34a853,color:#fff,stroke:none
    style LONG fill:#fbbc04,color:#000,stroke:none
    style TF fill:#ea4335,color:#fff,stroke:none
```

> **단기 실행**(녹색): 캠페인·UX·프로모션 등 빠른 피드백 가능  
> **구조 개선**(노란색): 인프라·제도 변경으로 시간 필요, 억지로 3개월에 맞추지 않음  
> **협업 TF**(빨간색): 여러 팀이 맞물려야 실행 가능한 과제

---

## 3. BF 3단계 타임라인

```mermaid
gantt
    title Black Friday 통합 타임라인 (9월~1월)
    dateFormat YYYY-MM-DD
    axisFormat %m월

    section 선결 조건
    Phase 0 · Free Shipping · Metric Dict    :crit, pre, 2026-09-01, 2026-09-14

    section CRM/마케팅
    통합 캠페인 캘린더 확정                     :crm1, 2026-09-15, 2026-10-31
    유입 캠페인 + 바우처 예고                   :crm2, 2026-11-01, 2026-11-30
    D+7 추천 · D+30 재구매 · 1/1 바우처 해금   :crm3, 2026-12-01, 2027-01-31

    section Product/UX
    Phase 0 완료 · Thank-you 페이지            :prod1, 2026-09-15, 2026-10-31
    전환 UX · 구매완료 팝업                     :prod2, 2026-11-01, 2026-11-30
    재진입 UX · 재방문 추천                     :prod3, 2026-12-01, 2027-01-31

    section MD
    번들/세트 확정 · Free Shipping 반영         :md1, 2026-09-15, 2026-10-31
    BF 프로모션 실행                            :md2, 2026-11-01, 2026-11-30
    2차 구매 연관 상품 · 시즌 전환              :md3, 2026-12-01, 2027-01-31

    section 물류
    지연 다발 셀러 점검 · 물량 분산             :log1, 2026-09-15, 2026-10-31
    BF 배송 품질 방어                           :crit, log2, 2026-11-01, 2026-11-30
    배송 완료 데이터 → CRM 연동                :log3, 2026-12-01, 2027-01-31

    section CX
    Recovery flow 구축                         :cx1, 2026-09-15, 2026-10-31
    실시간 VOC 대응                             :cx2, 2026-11-01, 2026-11-30
    BF 저평점 고객 Recovery                     :cx3, 2026-12-01, 2027-01-31

    section Seller Ops
    위험 셀러 경고 · 출고 기준 확인             :so1, 2026-09-15, 2026-10-31
    출고 모니터링                               :so2, 2026-11-01, 2026-11-30
    BF 성과 기반 셀러 평가                      :so3, 2026-12-01, 2027-01-31

    section 핵심 측정
    BF cohort 30일 재구매 측정                  :crit, m1, 2026-12-25, 2027-01-05
    BF cohort 60일 재구매 측정                  :crit, m2, 2027-01-25, 2027-02-05
```

> **9월 첫 2주**(선결 조건)를 놓치면 전체 일정이 밀린다.  
> **12~1월**(사후)이 진짜 승부다 — BF cohort가 재구매로 이어지는지가 전사 OKR 기여의 본질.

---

## 4. 저평점 원인 비중 — 왜 한 팀이 못 고치는가

```mermaid
pie title 첫 구매 저평점(12.82%) 원인 분포
    "미배송/배송 지연 — 물류" : 42
    "CS 무응답 — CX" : 20
    "상품 기대 불일치 — Seller Ops" : 20
    "UX 문제 — Product/UX" : 18
```

> Product/UX가 혼자 목표를 잡으면 18%만 통제 가능하다.  
> 나머지 82%는 물류·CX·Seller Ops가 함께 움직여야 한다 → **TF2 공동 OKR**

---

## 5. 재구매 Lifecycle Journey

```mermaid
flowchart TD
    A["<b>첫 구매 완료</b>"] --> B["<b>[즉시]</b> Thank-you 페이지<br/>연관 상품 추천"]
    B --> C["<b>[D+3]</b> 배송 완료 확인<br/>만족도 + 카테고리 추천"]
    C --> D["<b>[D+7]</b> 리뷰 작성 유도<br/>다음 구매 할인 제공"]
    D --> E["<b>[D+30]</b> 재구매 주기 캠페인<br/>보충 상품 추천"]
    E --> F["<b>[D+60]</b> 재진입 캠페인<br/>미방문 고객 타겟"]
    F --> G["<b>[D+90]</b> 이탈 방지<br/>마지막 터치포인트"]

    B -.- P1["Product/UX + MD"]
    C -.- P2["물류 → CRM"]
    D -.- P3["CRM"]
    E -.- P4["CRM + MD"]
    F -.- P5["CRM + Product/UX"]
    G -.- P6["CRM"]

    style A fill:#1a73e8,color:#fff,stroke:none
    style B fill:#34a853,color:#fff,stroke:none
    style C fill:#34a853,color:#fff,stroke:none
    style D fill:#34a853,color:#fff,stroke:none
    style E fill:#fbbc04,color:#000,stroke:none
    style F fill:#fbbc04,color:#000,stroke:none
    style G fill:#ea4335,color:#fff,stroke:none
```

> 녹색(D+0~7): **첫 경험 확보** 구간 — 여기서 실패하면 재구매 가능성 급락  
> 노란색(D+30~60): **재구매 유도** 구간 — 적극적 개입 필요  
> 빨간색(D+90): **이탈 방지** — 이 시점까지 안 오면 사실상 이탈

---

## 6. 혼자 할 것 vs 같이 할 것

```mermaid
flowchart LR
    subgraph 독립["각 팀이 혼자 할 것"]
        CRM_S["<b>CRM</b><br/>Lifecycle CRM<br/>Cohort 세그먼트"]
        PROD_S["<b>Product</b><br/>PDP 신뢰 요소<br/>장바구니 UX"]
        MD_S["<b>MD</b><br/>번들/세트 기획<br/>Accessory attach"]
        CX_S["<b>CX</b><br/>저평점 Recovery<br/>VOC 태깅"]
        LOG_S["<b>물류</b><br/>Lead Time 단축<br/>3PL 파트너십"]
        SELL_S["<b>Seller Ops</b><br/>위험 셀러 코칭<br/>온보딩 완주율"]
    end

    subgraph 협업["TF — 같이 할 것"]
        TF1["<b>TF1</b><br/>BF 통합 전략"]
        TF2["<b>TF2</b><br/>첫 구매 경험<br/>품질 개선"]
        TF3["<b>TF3</b><br/>재구매<br/>Lifecycle"]
        TF4["<b>TF4</b><br/>셀러 품질<br/>관리 통합"]
        TF5["<b>TF5</b><br/>측정 체계<br/>통일"]
    end

    CRM_S --> TF1
    CRM_S --> TF3
    PROD_S --> TF1
    PROD_S --> TF2
    PROD_S --> TF3
    MD_S --> TF1
    MD_S --> TF3
    CX_S --> TF1
    CX_S --> TF2
    LOG_S --> TF2
    LOG_S --> TF4
    SELL_S --> TF2
    SELL_S --> TF4

    style 독립 fill:#f8f9fa,stroke:#dadce0
    style 협업 fill:#e8f0fe,stroke:#1a73e8
```

> 왼쪽은 팀이 자기 영역 안에서 독립 추진. 오른쪽은 여러 팀이 맞물려야 실행 가능한 과제.  
> 화살표가 많은 팀(CRM, Product)이 TF에서 가장 많은 교차점을 갖는다.

---

> **상세 내용**: 각 팀별 독립 과제, TF별 설계 내용, 선결 조건, 수치 조정 사항은  
> [integrated_okr_plan.md](integrated_okr_plan.md)를 참고한다.
