# Olist 성장 진단 KPI 트리 지표 선별안

> 최종 수정일: 2026-03-31

## 1. 문서 목적

이 문서는 `Olist의 성장 진단 컨설팅을 통한 액션 플랜 제시`를 위해, **이번 프로젝트에서 실제로 써야 할 KPI 트리 지표를 선별**한 기준 문서입니다.

핵심 원칙은 아래 3가지입니다.

1. **Raw data로 직접 계산 가능한 지표만 채택한다.**
2. **상위 KPI와 하위 KPI가 수식 또는 명확한 논리로 연결되어야 한다.**
3. **발표용 지표가 아니라, 실제 Action Plan으로 이어질 수 있는 지표만 남긴다.**

이번 문서는 `시니어 데이터분석가` 관점에서, 이커머스 실무에서 바로 설명 가능하고 조직이 납득할 수 있는 KPI 구조로 정리했습니다.

---

## 2. 데이터 범위와 전제

### 분석 범위

- 분석 기간: `2017-01-01 ~ 2018-08-31`
- Raw data 위치: `project-2/data/`
- 사용 테이블:
  - Buyer/Order 관점: `customers`, `orders`, `order_items`, `payments`, `reviews`, `products`, `sellers`
  - Seller funnel 관점: `olist_marketing_qualified_leads`, `olist_closed_deals`

### 이번 프로젝트에서 반드시 알아야 할 데이터 제약

이번 데이터에는 아래 정보가 **없습니다**.

- 방문자 수
- 세션 수
- 상품 상세 조회 수
- 장바구니 이벤트 로그
- checkout step별 이벤트
- 광고비
- buyer side의 paid/organic 유입 데이터

즉, 첨부 이미지처럼 `총매출 = 트래픽 × CR × AOV` 구조를 **그대로** 쓰면 안 됩니다.  
이 트리는 훌륭한 프레임이지만, 현재 Olist raw data로는 `트래픽`과 `세션 기반 CR`을 직접 계산할 수 없기 때문입니다.

따라서 이번 프로젝트에서는 **주문 로그 기반 KPI 트리**로 재구성하는 것이 맞습니다.

---

## 3. 결론 먼저: 이번 프로젝트의 KPI 트리 추천안

### 메인 KPI 트리

이번 프로젝트의 메인 North Star KPI는 **Delivered GMV**로 잡는 것을 추천합니다.

이유는 간단합니다.

- 이번 프로젝트의 주제가 `성장 진단`이기 때문
- `GMV`는 Olist 같은 이커머스 플랫폼의 성장을 가장 직관적으로 설명하는 결과 지표이기 때문
- 현재 raw data에서 가장 안정적으로 계산 가능하기 때문
- 이후 하위 원인을 `고객 수`, `재구매`, `주문 빈도`, `AOV`, `운영 품질`로 자연스럽게 분해할 수 있기 때문

### 메인 KPI 트리 구조

```text
Lv1. Delivered GMV
 = Delivered Orders × AOV

Lv2-1. Delivered Orders
 = Active Purchasing Customers × Orders per Active Customer

Lv2-2. AOV
 = Avg Item Revenue per Order + Avg Freight per Order

Lv3-1. Active Purchasing Customers
 -> One-time Purchasing Customers
 -> Repeat Purchasing Customers

Lv3-2. Orders per Active Customer
 -> Repeat Order Share

Lv3-3. Avg Item Revenue per Order
 -> Avg Items per Order

Lv3-4. 운영 Guardrail
 -> Delivery Delay Rate
 -> Low Review Share
 -> Cancel/Unavailable Rate
```

### 보조 KPI 트리

Olist는 marketplace이므로 buyer growth만 보면 반쪽 분석이 됩니다.  
따라서 발표 본문에서는 메인 트리를 `GMV`로 가져가되, 보조 트리로는 **Seller acquisition efficiency**를 함께 보는 것이 좋습니다.

```text
Lv1. Closed Deals
 = MQL Volume × MQL→Deal Conversion Rate
```

이 보조 트리는 `중장기 공급 확대`와 연결됩니다.  
단, 이번 발표의 메인 스토리는 buyer/order 기반 GMV 트리로 가져가는 것이 더 설득력 있습니다.

---

## 4. 왜 이 구조가 맞는가

### 4-1. 이 프로젝트의 최상위 질문은 "왜 성장하지 못하는가?"이다

성장 진단 컨설팅에서 가장 먼저 답해야 하는 질문은 아래입니다.

- 매출이 어디서 만들어지는가?
- 고객 수가 안 늘어서 문제인가?
- 들어온 고객이 다시 안 사서 문제인가?
- 주문은 생기는데 주문당 가치가 낮은가?
- 운영 품질 문제 때문에 재구매가 막히는가?

이 질문에 가장 잘 답하는 구조가 `Delivered GMV -> Orders -> Customers / Frequency / AOV`입니다.

### 4-2. "재구매가 약하다"는 가설을 수치로 설명할 수 있다

이번 데이터에서 가장 눈에 띄는 수치는 아래입니다.

- Active Purchasing Customers: `93,104명`
- Repeat Purchasing Customers: `2,789명`
- Repeat Customer Share: `3.00%`
- Orders per Active Customer: `1.0334`
- Repeat Order Share: `3.23%`

즉, Olist는 현재 **매출의 대부분을 사실상 1회성 구매 고객에 의존**하고 있습니다.  
이 구조에서는 매달 신규 유입을 계속 태워도 재구매가 받쳐주지 않으면 성장 효율이 급격히 떨어집니다.

### 4-3. 운영 품질 지표를 Guardrail로 반드시 같이 봐야 한다

재구매가 낮을 때 실무에서 흔히 하는 실수는, 광고/유입만 더 늘리면 해결된다고 보는 것입니다.  
하지만 이번 데이터에서는 운영 품질 문제가 분명히 보입니다.

- Delivery Delay Rate: `8.13%`
- Severe Delay Rate (7일 이상): `3.47%`
- Avg Review Score: `4.157`
- Low Review Share(1~2점, reviewed 기준): `12.76%`
- Cancel/Unavailable Rate: `1.19%`

별점 평균만 보면 괜찮아 보이지만, 실제로는 **1~2점 리뷰 비중이 결코 낮지 않고**, 배송 지연도 무시하기 어렵습니다.  
따라서 이 지표들은 메인 North Star는 아니지만, **재구매와 고객 경험을 막는 Guardrail KPI**로 반드시 같이 관리해야 합니다.

---

## 5. 최종 채택 KPI 목록

아래 지표를 이번 프로젝트의 **공유용 공식 KPI 세트**로 추천합니다.

| 구분 | KPI | 정의 | 목적 | 선정 근거 | 현황 |
|---|---|---|---|---|---|
| Lv1 | Delivered GMV | `sum(price + freight_value)` for delivered orders | 전체 성장 규모를 가장 직관적으로 설명 | 현재 데이터에서 가장 안정적으로 계산 가능한 최종 성과 지표 | `BRL 15,373,120` |
| Lv2 | Delivered Orders | delivered 주문 수 | GMV를 주문량 관점에서 분해 | `GMV = Orders × AOV`로 수식 분해 가능 | `96,211건` |
| Lv3 | Active Purchasing Customers | delivered 주문을 만든 `customer_unique_id` 수 | 주문량의 기반인 구매 고객 풀 확인 | `Orders = Customers × Frequency` 구조에 필수 | `93,104명` |
| Lv4 | Repeat Purchasing Customers | 2회 이상 delivered 주문한 고객 수 | 성장의 질 확인, CRM/Retention 타겟 정의 | Olist의 핵심 병목이 신규 확보가 아니라 재구매 부재인지 확인 가능 | `2,789명` |
| 진단 | Repeat Customer Share | `Repeat Purchasing Customers / Active Purchasing Customers` | 재구매 기반의 취약성 진단 | 이번 프로젝트에서 가장 중요한 구조적 진단 지표 | `3.00%` |
| Lv3 | Orders per Active Customer | `Delivered Orders / Active Purchasing Customers` | 구매 빈도 파악 | 재구매 구조가 약하면 이 값이 1에 수렴 | `1.0334` |
| 진단 | Repeat Order Share | `두 번째 주문 이후 주문 수 / Delivered Orders` | 빈도 성장의 실질 기여 확인 | 고객 수가 아니라 실제 반복 주문이 얼마나 매출을 받치는지 확인 가능 | `3.23%` |
| Lv2 | AOV | `Delivered GMV / Delivered Orders` | 주문당 가치 파악 | 주문량 외 매출 성장을 설명하는 핵심 축 | `BRL 159.79` |
| Lv3 | Avg Item Revenue per Order | `sum(price) / Delivered Orders` | 상품 매출 중심 AOV 해석 | AOV 중 실질 상품 가치 파악에 가장 중요 | `BRL 137.00` |
| Lv4 | Avg Items per Order | 주문당 평균 상품 수 | bundle/cross-sell 여지 진단 | AOV 개선 Action과 직접 연결 가능 | `1.1421개` |
| Lv3 | Avg Freight per Order | `sum(freight_value) / Delivered Orders` | AOV 구성 해석 보조 | 현재 GMV 정의상 포함되므로 수식상 필요 | `BRL 22.78` |
| Guardrail | Delivery Delay Rate | 실제 도착일 > 예상 도착일 비중 | 운영 품질이 재구매를 막는지 확인 | 리뷰/이탈 악화의 대표 선행지표 | `8.13%` |
| Guardrail | Low Review Share | 1~2점 리뷰 비중 (reviewed 주문 기준) | 고객 경험 악화 감지 | 평균 별점만 보면 놓치는 리스크를 보완 | `12.76%` |
| Guardrail | Cancel/Unavailable Rate | canceled + unavailable / 전체 주문 | 구매 경험 손실 모니터링 | acquisition이 주문으로 이어져도 fulfillment 실패 시 성장 손실 | `1.19%` |
| 보조 Lv1 | Closed Deals | 계약 완료 seller 수 | marketplace supply 확대 성과 확인 | buyer side 외 supply side 성장 진단 필요 | `842건` |
| 보조 Lv2 | MQL Volume | seller lead 수 | seller acquisition pool 확인 | 공급 확대의 모수 | `8,000건` |
| 보조 Lv2 | MQL→Deal Conversion Rate | `Closed Deals / MQL` | seller funnel 효율 확인 | 공급 확장의 질을 설명하는 핵심 전환율 | `10.53%` |

---

## 6. 지표별 상세 설명

## 6-1. Delivered GMV

### 정의

`Delivered GMV = delivered 주문의 (price + freight_value) 합`

### 왜 선정했는가

- 경영진/멘토/팀원이 가장 빠르게 이해할 수 있는 최상위 성과 지표입니다.
- 광고, CRM, 상품, 배송, 셀러 확장 등 모든 활동이 최종적으로 반영되는 결과 값입니다.
- 이번 raw data 기준으로 가장 신뢰도 높게 계산할 수 있습니다.

### 무엇을 알려주는가

이 지표는 "Olist가 현재 실제로 만들어내고 있는 거래 규모"를 보여줍니다.  
다만 이 값 하나만 보면 성장이 왜 느린지 알 수 없기 때문에, 반드시 `Orders`, `Customers`, `Frequency`, `AOV`로 쪼개야 합니다.

### 현재 해석

현재 분석 기간의 Delivered GMV는 `BRL 15.37M`입니다.  
문제는 이 GMV가 높은 재구매 기반이 아니라, 대부분 단발성 구매에 기대고 있다는 점입니다.

---

## 6-2. Delivered Orders

### 정의

`delivered 상태 주문 수`

### 왜 선정했는가

- GMV의 첫 번째 직접 분해 축입니다.
- 취소/미배송 주문을 제외하고 실제 고객에게 전달된 거래만 보므로 해석이 명확합니다.

### 목적

- 매출이 "주문 수" 부족 때문인지, "주문당 가치" 부족 때문인지 구분합니다.
- 운영 품질 KPI와 함께 보면 누수 구간을 더 정확히 파악할 수 있습니다.

### 현재 해석

전체 주문 `99,092건` 중 delivered는 `96,211건`, 비중은 `97.09%`입니다.  
상단 숫자만 보면 나쁘지 않지만, 주문을 만든 고객의 재구매 구조가 약해서 성장의 질이 떨어집니다.

---

## 6-3. Active Purchasing Customers

### 정의

`delivered 주문을 만든 고유 customer_unique_id 수`

### 왜 선정했는가

- 주문 수의 기반이 되는 고객 모수를 설명합니다.
- `customer_id`가 아니라 반드시 `customer_unique_id`를 써야 재구매 분석이 가능합니다.

### 목적

- Olist가 얼마나 넓은 구매 고객 풀을 확보했는지 파악
- 이후 `Repeat Purchasing Customers`와 함께 고객 구조를 진단

### 현재 해석

Active Purchasing Customers는 `93,104명`입니다.  
겉으로는 고객 풀 규모가 작지 않아 보이지만, 대부분이 1회 구매로 끝나고 있다는 점이 핵심 문제입니다.

---

## 6-4. Repeat Purchasing Customers / Repeat Customer Share

### 정의

- `Repeat Purchasing Customers = 2회 이상 delivered 주문 고객 수`
- `Repeat Customer Share = Repeat Purchasing Customers / Active Purchasing Customers`

### 왜 선정했는가

이번 프로젝트에서 가장 중요한 지표입니다.

- 이커머스 성장의 질은 결국 "다시 사는 고객"이 결정합니다.
- CRM, 리텐션, 제품/배송 경험 개선의 성과가 가장 직접적으로 반영됩니다.
- 신규 확보만으로 버티는 구조인지, 고객 기반이 쌓이는 구조인지 구분해 줍니다.

### 목적

- 단기 매출이 아니라 장기 성장 체력 진단
- 발표에서 "왜 액션 플랜이 Retention 중심이어야 하는가"를 설명하는 근거

### 현재 해석

- Repeat Purchasing Customers: `2,789명`
- Repeat Customer Share: `3.00%`

즉, active customer 100명 중 97명은 사실상 1회 구매 고객입니다.  
이 수치는 Olist의 핵심 병목이 **유입 자체보다 재방문·재구매 구조의 부재**에 있음을 강하게 시사합니다.

---

## 6-5. Orders per Active Customer / Repeat Order Share

### 정의

- `Orders per Active Customer = Delivered Orders / Active Purchasing Customers`
- `Repeat Order Share = 두 번째 주문 이후 주문 수 / Delivered Orders`

### 왜 선정했는가

- 고객 기반이 있어도 주문 빈도가 낮으면 성장 효율은 올라가지 않습니다.
- 이 두 지표는 "재구매 고객이 실제 주문 볼륨에 얼마나 기여하는가"를 보여줍니다.

### 목적

- CRM과 상품/배송 개선의 타깃을 빈도 문제로 연결
- 1회 구매 고객을 반복 주문 구조로 전환해야 하는 이유 설명

### 현재 해석

- Orders per Active Customer: `1.0334`
- Repeat Order Share: `3.23%`

주문 빈도가 거의 `1`에 붙어 있다는 것은, 고객 풀은 존재하지만 **구매가 이어지지 않는다**는 뜻입니다.  
실무적으로는 `재구매 유도 캠페인`, `첫 구매 이후 경험 개선`, `카테고리 재진입 설계`가 핵심 과제가 됩니다.

---

## 6-6. AOV / Avg Item Revenue per Order / Avg Items per Order

### 정의

- `AOV = Delivered GMV / Delivered Orders`
- `Avg Item Revenue per Order = sum(price) / Delivered Orders`
- `Avg Items per Order = 주문당 평균 상품 수`

### 왜 선정했는가

- 주문 수만큼 중요한 매출 축이 주문당 가치입니다.
- AOV는 높은데 재구매가 낮은지, AOV 자체가 낮은지 구분해야 액션 우선순위가 달라집니다.
- 특히 `Avg Items per Order`는 bundle, cross-sell, cart build-up 같은 실무 액션과 직접 연결됩니다.

### 목적

- 매출 개선이 고객 수 확대형인지, 장바구니 가치 확대형인지 구분
- `상품 추천`, `묶음 제안`, `카테고리 조합` 실험의 방향 제시

### 현재 해석

- AOV: `BRL 159.79`
- Avg Item Revenue per Order: `BRL 137.00`
- Avg Freight per Order: `BRL 22.78`
- Avg Items per Order: `1.1421개`

주문당 상품 수가 `1.14개`라는 것은, 대다수 주문이 사실상 단품 구매라는 의미입니다.  
즉, AOV 개선의 여지는 `고가 상품 확대`보다는 **다품목 구매 유도와 basket expansion** 쪽에서 찾는 것이 현실적입니다.

---

## 6-7. Delivery Delay Rate

### 정의

`실제 도착일 > 예상 도착일`인 주문 비중

### 왜 선정했는가

- 배송 지연은 구매 후 경험의 핵심 리스크입니다.
- 특히 marketplace에서는 배송 경험이 셀러/플랫폼 신뢰 전체에 영향을 줍니다.
- 재구매율이 낮을 때 가장 먼저 같이 봐야 하는 운영 품질 지표입니다.

### 목적

- "왜 다시 사지 않는가?"를 설명하는 운영 측 원인 포착
- 후속 Action Plan에서 배송 SLA, 지연 seller, 지연 카테고리 분석으로 연결

### 현재 해석

- Delivery Delay Rate: `8.13%`
- Severe Delay Rate (7일 이상): `3.47%`
- Avg Delivery Days: `12.54일`

약 12건 중 1건이 예상 배송일을 넘기고 있습니다.  
이 수준이면 단순 운영 노이즈가 아니라, 리뷰와 재구매를 실제로 훼손할 수 있는 구조적 문제로 봐야 합니다.

---

## 6-8. Low Review Share

### 정의

`1~2점 리뷰 주문 수 / 리뷰가 존재하는 주문 수`

### 왜 선정했는가

- 평균 별점 하나만 보면 "괜찮다"는 착시가 생깁니다.
- 실제로는 낮은 점수의 tail risk가 얼마나 큰지 봐야 합니다.
- 지연 배송, 제품 기대 불일치, 고객 경험 악화와 연결 가능한 선행 시그널입니다.

### 목적

- 고객 경험 저하를 평균값이 아닌 분포 관점에서 설명
- 발표에서 `심슨의 역설`처럼 평균에 속지 않기 위한 보완 지표로 사용

### 현재 해석

- Avg Review Score: `4.157`
- Low Review Share(1~2점): `12.76%`

평균 별점은 나쁘지 않지만, 리뷰 100개 중 약 13개가 저평점입니다.  
즉, Olist는 "전반적으로 무난"한 것이 아니라 **강한 만족과 강한 불만이 함께 존재하는 구조**로 해석하는 것이 더 정확합니다.

---

## 6-9. Cancel / Unavailable Rate

### 정의

`(canceled + unavailable) / 전체 주문 수`

### 왜 선정했는가

- acquisition과 주문 생성 이후에도 fulfillment 단계에서 매출이 누수될 수 있습니다.
- 특히 unavailable은 공급/재고/운영 문제와도 연결됩니다.

### 목적

- 구매 전환 이후의 손실 구간 확인
- seller 운영 품질과 공급 안정성 이슈를 추적

### 현재 해석

Cancel / Unavailable Rate는 `1.19%`입니다.  
절대값만 보면 높지 않지만, marketplace 구조에서는 반복적으로 발생할 경우 신뢰 하락과 CS 비용 증가로 이어질 수 있습니다.

---

## 6-10. Closed Deals / MQL Volume / MQL→Deal Conversion Rate

### 정의

- `Closed Deals = 계약 완료 seller 수`
- `MQL Volume = seller lead 수`
- `MQL→Deal Conversion Rate = Closed Deals / MQL`

### 왜 선정했는가

- Olist는 buyer side와 seller side가 함께 돌아가는 marketplace입니다.
- buyer 매출만 보면 현재 매출은 해석되지만, 중장기 공급 확장성은 보이지 않습니다.
- seller pipeline이 약하면 카테고리 확장, 상품 다양성, 가격 경쟁력까지 함께 약해질 수 있습니다.

### 목적

- 중장기 공급 측 성장 여력 진단
- buyer growth와 별개로 supply-side action의 필요성 설명

### 현재 해석

- MQL Volume: `8,000건`
- Closed Deals: `842건`
- MQL→Deal Conversion Rate: `10.53%`

seller funnel은 분명 존재하지만, 계약 전환율이 매우 높은 구조라고 보기는 어렵습니다.  
즉, Olist의 성장은 buyer retention뿐 아니라 **seller acquisition efficiency 개선**도 함께 봐야 합니다.

---

## 7. 이번 프로젝트에서 제외해야 할 KPI

아래 KPI는 일반적인 이커머스 KPI로는 중요하지만, **이번 raw data로는 직접 계산이 불가능하거나 오해를 부를 가능성이 높아 제외**하는 것이 맞습니다.

| 제외 KPI | 제외 이유 |
|---|---|
| 방문자 수, 세션 수 | raw data 부재 |
| PDP View Rate | 상품 조회 이벤트 로그 부재 |
| Add-to-Cart Rate | 장바구니 이벤트 로그 부재 |
| Checkout Conversion Rate | checkout step 이벤트 로그 부재 |
| Paid / Organic buyer traffic mix | buyer acquisition source 부재 |
| CAC, ROAS, ROI | 광고비 데이터 부재 |
| Referral Rate | 추천/초대 데이터 부재 |
| Buyer cohort별 CRM open/click/conversion | CRM 발송 로그 부재 |

즉, 이번 프로젝트에서 무리하게 "퍼포먼스 마케팅 KPI 트리"를 만드는 것은 정확하지 않습니다.  
대신 **주문·고객·리뷰·배송·seller funnel 기반의 성장 진단 트리**가 현재 데이터셋에 가장 적합합니다.

---

## 8. 발표용 추천 메시지

발표에서는 아래처럼 정리하는 것이 가장 깔끔합니다.

> Olist의 현재 성장 문제는 단순히 주문이 적어서가 아니라,  
> **재구매 고객 비중이 3%에 불과한 구조적 취약성**에 있습니다.  
> 따라서 이번 KPI 트리는 `Delivered GMV`를 최상위에 두고,  
> 이를 `고객 수`, `주문 빈도`, `AOV`로 분해했으며,  
> 재구매를 막는 원인으로 `배송 지연`, `저평점 비중`, `공급 전환 효율`을 Guardrail 및 보조 트리로 함께 관리합니다.

---

## 9. 최종 추천

이번 프로젝트에서 팀 공통 KPI로 먼저 합의해야 하는 것은 아래 8개입니다.

1. Delivered GMV
2. Delivered Orders
3. Active Purchasing Customers
4. Repeat Customer Share
5. Orders per Active Customer
6. AOV
7. Delivery Delay Rate
8. MQL→Deal Conversion Rate

이 8개를 먼저 합의하면, 이후 세부 분석은 아래처럼 분업하기 좋습니다.

- CRM/Retention: `Repeat Customer Share`, `Orders per Active Customer`, `Low Review Share`
- 상품/머천다이징: `AOV`, `Avg Items per Order`
- 운영/물류: `Delivery Delay Rate`, `Cancel/Unavailable Rate`
- 공급/셀러: `MQL→Deal Conversion Rate`, `Closed Deals`

---

## 10. 수치 산출 기준 메모

- 기간 필터: `2017-01-01 ~ 2018-08-31`
- Delivered GMV: delivered 주문 기준 `price + freight_value`
- Repeat customer: delivered 주문 `2회 이상`
- Low review share: 리뷰가 존재하는 주문 중 `1~2점` 비중
- Delay rate: 실제 도착일이 예상 도착일보다 늦은 주문 비중
