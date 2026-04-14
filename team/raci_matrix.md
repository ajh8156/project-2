# KR별 RACI 매트릭스

> 최종 수정: 2026-04-14

---

## RACI란 무엇인가?

RACI는 프로젝트에서 **"이 일은 누가 하는 거야?"**라는 질문에 답하기 위한 역할 분담 도구다.

여러 팀이 하나의 목표를 함께 추진할 때, 역할이 모호하면 두 가지 문제가 생긴다.
- **모두가 한다고 생각하지만 아무도 안 하는 것** (책임 공백)
- **여러 팀이 같은 일을 각자 하는 것** (중복 낭비)

RACI는 모든 업무 항목에 대해 각 팀의 역할을 4가지 중 하나로 명확히 지정한다.

### 4가지 역할

| 역할 | 영어 | 의미 | 쉬운 비유 |
|------|------|------|----------|
| **R** | Responsible (실행) | 실제로 **손을 움직여서 일하는** 팀 | 요리사 — 직접 요리를 만든다 |
| **A** | Accountable (최종 책임) | 결과에 대해 **최종 결정권과 책임**을 지는 팀 | 주방장 — 메뉴를 결정하고 맛의 최종 책임을 진다 |
| **C** | Consulted (협의) | 실행 전에 **의견을 묻는** 팀. 전문 지식을 제공한다 | 식재료 전문가 — "이 재료는 이렇게 써야 해"라고 조언한다 |
| **I** | Informed (통보) | 결과를 **사후에 전달받는** 팀. 결정에 관여하지 않는다 | 홀 매니저 — 메뉴가 정해지면 알림을 받는다 |

### 핵심 규칙

```
규칙 1: 하나의 항목에 A(최종 책임)는 반드시 1팀만
         → "공동 책임 = 무책임". 누가 최종 결정권자인지 명확해야 한다.

규칙 2: R(실행)은 여러 팀이 될 수 있다
         → 단, 이때는 TF(Task Force)를 통해 조율한다.

규칙 3: C(협의)로 지정된 팀은 의견을 줄 수 있지만 결정권은 없다
         → A가 최종 판단한다.

규칙 4: I(통보)로 지정된 팀은 결과를 전달받기만 한다
         → 사전에 의견을 구할 필요 없다.
```

### 왜 지금 이것이 필요한가?

우리 프로젝트에서 실제로 발생한 문제:

| 문제 | RACI가 없어서 생긴 일 |
|------|---------------------|
| BF 쿠폰을 4팀이 각자 설계 | R이 4곳, A가 없음 → 중복 설계 |
| 저평점(KR5) 책임이 모호 | Product가 A인데 원인의 82%가 타팀 영역 → A 재지정 필요 |
| 무료배송 정책이 MD vs Logistics 충돌 | 둘 다 A라고 생각 → 결정이 안 남 |

RACI를 정하면 이런 충돌이 사전에 방지된다.

### 읽는 예시

> **KR4 (배송 지연율 8.2% → 6.0%)** 의 RACI를 보면:
> - **Logistics = R/A** → 배송 지연율 개선을 직접 실행하고 최종 책임을 진다
> - **Seller Ops = R** → 셀러 귀책 출고 지연을 줄이는 실행을 한다
> - **Product = C** → 배송 예정일 UI를 구현할 때 의견을 구한다
> - **CX = C** → 지연 발생 시 고객 대응 방식에 대해 의견을 구한다
> - **CRM, 프로모션, MD = I** → 지연율 개선 결과를 전달받는다

---

## 전사 KR RACI

| KR | Marketing (CRM) | Marketing (프로모션) | Product/UX | MD | Logistics | CX | Seller Ops |
|----|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **KR1** 재구매율 3%→4.5% | **R/A** | R | C | C | I | I | C |
| **KR2** 주문수/인 1.03→1.06 | R | C | C | **R/A** | I | I | I |
| **KR3** 재구매비중 6.1%→9% | **R/A** | R | C | R | I | I | I |
| **KR4** 배송지연율 8.2%→6% | I | I | C | I | **R/A** | C | R |
| **KR5** 저평점 12.8%→10.5% | I | I | R | I | C | **R/A** | R |
| **G1** 신규고객 유지 | R | **R/A** | C | C | I | I | I |
| **G2** AOV 하락방지 | C | R | C | **R/A** | I | I | I |

---

## TF별 RACI

| TF | 리드 (A) | 실행 (R) | 협의 (C) | 통보 (I) |
|----|---------|---------|---------|---------|
| **TF1** BF 통합 전략 | CRM | CRM, 프로모션, MD | Product, Logistics | CX, Seller Ops |
| **TF2** 첫 구매 품질 | Product | Product, CX, Seller Ops | Logistics | CRM, MD |
| **TF3** 재구매 Lifecycle | CRM | CRM, MD, Product | 프로모션 | Logistics, CX, Seller Ops |
| **TF4** 셀러 품질 통합 | Seller Ops | Seller Ops, Logistics | CX | CRM, MD, Product |
| **TF5** 북동부 확장 | Seller Ops | Seller Ops, Logistics | — | CRM, MD, Product, CX |

---

## BF 핵심 항목 RACI

| 항목 | R | A | C | I |
|------|---|---|---|---|
| BF 쿠폰 설계 (단일 체계) | CRM | CRM | 프로모션, MD | Product, Logistics |
| BF 번들 상품 기획 | MD | MD | Product, CRM | Logistics |
| BF 배송 Capacity 확보 | Logistics | Logistics | 프로모션 | CRM, MD |
| BF 코호트 D+30 추적 | CRM | CRM | 프로모션 | MD, Product |
| BF 기간 지연율 모니터링 | Logistics | Logistics | Seller Ops | CRM, Product |
| BF 저평점 즉시 대응 | CX | CX | Product | CRM, Logistics |
| BF 얼리버드 프로모션 | 프로모션 | 프로모션 | MD, CRM | Product, Logistics |

---

## 읽는 법

- **하나의 KR에 A(최종 책임)는 반드시 1팀만** — 공동 책임은 무책임
- R이 여러 팀이면 TF를 통해 조율
- C로 지정된 팀은 의견을 줄 수 있지만 결정권 없음
- I로 지정된 팀은 결과를 전달받기만 함

> *이 매트릭스는 `project_one_pager.md`의 팀×KR 기여 매트릭스와 함께 봅니다.*
