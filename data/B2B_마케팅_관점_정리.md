# Olist 프로젝트용 B2B 마케팅 관점 정리

> 작성일: 2026-04-03
> 목적: "커머스인데 왜 B2B 데이터처럼 보이는가?"를 명확히 이해하고, 현재 데이터셋을 seller-side B2B marketing 관점으로 해석하기

---

## 1. 결론 먼저

이번 Olist 데이터는 **일반적인 B2C 커머스 데이터와 B2B seller acquisition 데이터가 함께 있는 hybrid 구조**입니다.

- `orders`, `order_items`, `payments`, `reviews`, `customers`는 **buyer-side B2C 거래 데이터**
- `marketing_qualified_leads`, `closed_deals`는 **seller-side B2B marketing / sales funnel 데이터**

즉, 이 프로젝트는 "커머스"가 맞지만, 동시에 **marketplace의 공급자(seller)를 유치하는 B2B 성장 데이터**도 같이 포함하고 있습니다.

이를 명확히 이해하기 위해 아래 포인트를 참고하면 됩니다.

> Olist는 고객에게 상품을 파는 B2C 서비스이면서,
> 동시에 판매자에게 입점을 제안하고 계약하는 B2B marketplace이기도 하다.

---

## 2. 왜 커머스인데 B2B 데이터처럼 보이는가

일반적인 D2C/B2C 커머스라면 마케팅 데이터는 보통 아래처럼 보입니다.

- 유입 수
- session
- signup
- add-to-cart
- checkout
- purchase
- ROAS / CAC

그런데 이번 데이터에는 이런 buyer traffic 로그보다, 아래처럼 **seller 유치 데이터**가 먼저 보입니다.

- `mql_id`
- `origin`
- `sdr_id`
- `sr_id`
- `won_date`
- `lead_type`
- `business_type`
- `declared_monthly_revenue`

이건 buyer acquisition 데이터가 아니라, **"입점 seller를 어떻게 데려오고 계약시키는가"**를 보는 데이터입니다.

즉 현재 데이터의 마케팅 퍼널은 다음과 같이 읽어야 합니다.

```text
유저 모객 퍼널이 아니라
seller 확보 퍼널이다.

MQL -> Sales Contact -> Closed Deal -> Seller Onboarding -> First Order -> Ongoing Selling
```

---

## 3. B2B 마케팅 개념과 용어 정리

### 3-1. B2B 마케팅이란

B2B 마케팅은 **기업이 다른 기업 또는 사업자에게 제품/서비스를 판매하기 위해 리드를 만들고, 육성하고, 전환시키는 활동**입니다.

이번 데이터에서는 Olist가 seller에게 이렇게 행동한 것으로 볼 수 있습니다.

- Olist가 입점 희망 seller를 모은다
- seller 정보를 확인한다
- sales 조직이 접촉한다
- 계약을 체결한다
- seller가 실제로 플랫폼에서 판매를 시작한다

즉 여기서 "고객"은 최종 구매자(buyer)가 아니라 **입점 seller**입니다.

### 3-2. 핵심 용어

| 용어 | 의미 | 이번 데이터에서 대응 컬럼/테이블 |
|---|---|---|
| Lead | 잠재 고객. 아직 계약하지 않았지만 관심을 보인 사업자 | `olist_marketing_qualified_leads_dataset` |
| MQL | Marketing Qualified Lead. 마케팅 기준으로 "영업에 넘길 만하다"고 판단된 리드 | `mql_id` |
| SDR | Sales Development Representative. 초기 리드 응대/qualification 담당 | `sdr_id` |
| SR | Sales Representative. 실제 계약 성사 담당 | `sr_id` |
| Closed Deal | 계약 완료 상태 | `won_date`, `seller_id` |
| Onboarding | 계약 후 실제 판매 준비를 마치는 과정 | `closed_deals` 이후 `order_items` 발생 전 구간 |
| Activation | seller가 플랫폼에서 실제 판매를 시작한 상태 | `closed_deals.seller_id`가 거래 데이터와 연결되는 시점 |
| Retention | seller가 한 번 팔고 끝나는 게 아니라 반복적으로 판매하는 상태 | seller별 주문 지속성, 활동 개월 수 |
| Revenue | seller가 만든 거래액 또는 플랫폼이 seller로부터 벌어들이는 수익 | `price + freight_value` 합계, commission은 별도 개념 |
| Seller Acquisition | seller를 새로 확보하는 활동 | `MQL`, `Closed Deal` |
| Seller Quality | 계약된 seller의 질 | `business_type`, `lead_type`, `declared_monthly_revenue` 등으로 보조 판단 |

### 3-3. 데이터에 자주 나오는 seller 관련 용어

| 용어 | 의미 | 해석 포인트 |
|---|---|---|
| `origin` | seller lead가 들어온 채널 | buyer 유입 채널이 아니라 seller acquisition channel |
| `lead_type` | seller 리드 유형 | seller 규모/디지털 성숙도 차이를 보는 segmentation 힌트 |
| `business_segment` | seller 업종/카테고리 | 어떤 카테고리 seller가 많이 유입/전환되는지 판단 가능 |
| `business_type` | `reseller`, `manufacturer`, `other` 등 | 공급 구조와 가격 경쟁력 해석에 중요 |
| `declared_monthly_revenue` | seller 자기신고 월매출 | 실제 거래액이 아니라 self-reported value |

---

## 4. B2B 마케팅과 B2C 유저 모객의 차이

| 구분 | B2C 유저 모객 | B2B seller acquisition |
|---|---|---|
| 누구를 데려오나 | 최종 구매자 | 판매자, 파트너사, 사업자 |
| 퍼널 길이 | 상대적으로 짧음 | 상대적으로 김 |
| 핵심 전환 | 구매, 회원가입, 앱 설치 | 계약, 입점, onboarding 완료 |
| 의사결정자 | 개인 | 사업자/회사 |
| 주요 지표 | CTR, CVR, Purchase, ROAS | MQL, Deal Conversion, Activation, Seller GMV |
| 성공 기준 | buyer 수와 구매액 증가 | seller 확보, seller 활성화, 공급 확대 |

이를 한 줄로 정리하면 아래가 가장 명확합니다.

> B2C는 "사람을 데려와서 사게 만드는 것"이고,
> B2B seller acquisition은 "사업자를 데려와서 입점시키고 실제로 팔게 만드는 것"이다.

---

## 5. 셀러 수수료(Commission) 개념 정리

### 5-1. 왜 중요한가

Marketplace에서 seller 수수료는 매우 중요합니다.

이유는 플랫폼 매출이 보통 아래 구조에서 나오기 때문입니다.

- 판매 수수료(commission / take rate)
- 광고 상품
- 물류/fulfillment 수수료
- 정산/금융 부가수익

즉, buyer가 많이 사는 것도 중요하지만, 플랫폼 입장에서는 결국 **seller 거래액 중 얼마를 플랫폼이 가져가는가**가 중요합니다.

### 5-2. 핵심 개념

| 용어 | 의미 |
|---|---|
| Commission Fee | seller가 주문 발생 시 플랫폼에 내는 판매 수수료 |
| Take Rate | 거래액(GMV) 대비 플랫폼 수익 비율 |
| Seller Payout | seller에게 정산되는 금액 |
| Net Revenue | 플랫폼이 실제로 가져가는 매출 |

간단한 구조는 아래처럼 이해하면 됩니다.

```text
Platform Revenue = GMV x Commission Rate
Seller Payout = GMV - Commission - 기타 비용
```

예를 들어 commission rate가 12%라면,

- GMV 100만 원 발생
- 플랫폼 수익 12만 원
- seller 정산금은 기타 비용 차감 전 88만 원

### 5-3. 이번 데이터에서 주의할 점

현재 Olist raw data에는 아래 정보가 **직접적으로 없습니다**.

- commission rate
- seller별 fee
- payout
- 정산액
- 광고비

즉, 이번 데이터로는 **실제 플랫폼 수수료 매출을 직접 계산할 수 없습니다.**

따라서 이번 프로젝트에서는 수수료를 아래처럼 다뤄야 합니다.

1. **개념 설명은 반드시 포함**
2. 하지만 **실측 KPI로는 채택하지 않음**
3. seller GMV를 기준으로 "commission rate가 있다면 플랫폼 revenue로 확장 가능"하다고 설명

정리하면:

> seller 수수료는 marketplace에서 매우 중요한 monetization KPI이지만,
> 현재 데이터에는 fee/take rate 정보가 없으므로 개념적으로만 연결하고 실측치는 계산 불가하다고 말하는 것이 맞다.

---

## 6. 현재 데이터셋을 B2B 마케팅 관점으로 읽는 방법

### 6-1. `olist_marketing_qualified_leads_dataset`

이 테이블은 buyer 유입 데이터가 아니라 **seller lead acquisition 데이터**입니다.

핵심 질문:

- seller 리드는 얼마나 들어오는가?
- 어느 채널에서 많이 들어오는가?
- 어떤 채널이 계약 전환이 잘 되는가?

주요 컬럼:

- `mql_id`
- `first_contact_date`
- `landing_page_id`
- `origin`

### 6-2. `olist_closed_deals_dataset`

이 테이블은 seller sales funnel의 하단입니다.

핵심 질문:

- MQL 중 실제 계약된 seller는 몇 명인가?
- 어떤 seller 타입이 많이 계약되는가?
- 계약 후 실제 판매로 이어지는가?

주요 컬럼:

- `seller_id`
- `won_date`
- `business_segment`
- `lead_type`
- `business_type`
- `declared_monthly_revenue`

### 6-3. `orders`, `order_items`, `sellers`

이 구간부터는 seller 확보 이후의 **post-onboarding performance**를 봅니다.

핵심 질문:

- 계약된 seller가 실제 거래를 만들었는가?
- 첫 주문까지 오래 걸리는가?
- 몇 개월 동안 계속 활동하는가?
- seller당 거래 기여도는 얼마나 되는가?

즉 B2B 관점에서는 거래 데이터도 buyer 데이터가 아니라, **seller activation / seller retention / seller monetization의 결과 데이터**로 해석할 수 있습니다.

---

## 7. 지금 데이터에서 바로 설명 가능한 B2B 핵심 지표

아래 지표들은 실제 데이터로 다시 확인한 값입니다.

### 7-1. Acquisition: seller lead 확보

| 지표 | 값 | 해석 |
|---|---:|---|
| MQL 수 | 8,000 | seller lead 모수 |
| Closed Deal 수 | 842 | 계약 완료 seller 수 |
| MQL -> Deal 전환율 | 10.52% | lead 10개 중 약 1개가 계약으로 전환 |

`origin` 기준 seller lead 유입 규모:

| origin | MQL 수 | Closed Deal 수 | Deal Conversion |
|---|---:|---:|---:|
| `organic_search` | 2,296 | 271 | 11.80% |
| `paid_search` | 1,586 | 195 | 12.30% |
| `social` | 1,350 | 75 | 5.56% |
| `unknown` | 1,099 | 179 | 16.29% |
| `direct_traffic` | 499 | 56 | 11.22% |
| `email` | 493 | 15 | 3.04% |
| `referral` | 284 | 24 | 8.45% |

해석:

- `organic_search`, `paid_search`, `social`이 lead volume은 큼
- 하지만 `social`, `email`은 계약 전환율이 상대적으로 낮음
- `unknown` 비중이 커서 attribution 해석에는 주의 필요
- 즉 seller acquisition은 **볼륨과 전환 효율을 함께 봐야 함**

### 7-2. Activation: 계약 seller가 실제 판매를 시작했는가

| 지표 | 값 | 해석 |
|---|---:|---|
| 계약 seller 중 delivered order 발생 seller | 376명 | 거래 데이터와 연결되는 activated seller |
| Closed Deal seller activation rate | 44.66% | 계약 seller의 절반 이하만 실제 판매로 이어짐 |
| 첫 order까지 평균 소요일 | 51.49일 | 계약 후 판매 개시까지 시간이 긴 편 |
| 첫 order까지 median 소요일 | 44.33일 | 대표값도 1달 이상 |

해석:

- B2B seller marketing에서 계약은 끝이 아니라 **중간 전환**
- 실제로 중요한 것은 seller가 상품을 올리고, 판매를 시작하고, 거래를 만드는 것
- 이 데이터에서는 계약 완료 842명 중 376명만 실제 delivered order로 이어짐
- 즉 seller funnel의 큰 병목은 `Lead -> Deal`보다도 `Deal -> Activated Seller`일 수 있음

### 7-3. Retention: seller가 계속 파는가

| 지표 | 값 | 해석 |
|---|---:|---|
| 거래 발생 closed seller 수 | 376명 | activation 완료 seller 모수 |
| 2개월 이상 활동 seller 수 | 266명 | 반복 활동 seller |
| 2개월 이상 활동 비율 | 70.74% | activated seller 기준 반복 활동은 나쁘지 않음 |
| 평균 활동 개월 수 | 2.72개월 | seller lifespan이 아주 길지는 않음 |
| median 활동 개월 수 | 2개월 | 절반은 2개월 수준 활동 |

해석:

- seller B2B에서는 Retention을 buyer 재구매가 아니라 **seller의 지속 판매 여부**로 봐야 함
- 계약된 seller 전체가 아니라, activation에 성공한 seller 안에서는 일정 수준의 반복 활동이 있음
- 따라서 seller-side에서는 `Deal -> Activation`이 먼저 핵심 병목이고, 그 다음이 장기 유지로 보임

### 7-4. Revenue: seller가 얼마의 거래를 만드는가

| 지표 | 값 | 해석 |
|---|---:|---|
| closed seller 중 거래 발생 seller 수 | 376명 | seller revenue 분석 모수 |
| closed seller 평균 GMV | BRL 2,027.89 | 평균은 소수 고성과 seller 영향 가능 |
| closed seller median GMV | BRL 676.01 | typical seller는 평균보다 작음 |
| closed seller 평균 delivered orders | 11.87건 | seller별 성과 편차 존재 |
| closed seller GMV 비중 | 4.94% | 전체 delivered GMV 중 closed_deals seller 기여분 |

해석:

- 평균과 median 차이가 커서 seller 성과 분산이 큼
- 즉 몇몇 seller가 거래를 많이 만들고, 다수는 작은 거래만 만드는 구조일 가능성이 높음
- seller acquisition은 단순히 많이 계약시키는 것보다 **활성화와 성과 품질**이 중요함
- commission rate가 있다면 이 seller GMV를 기반으로 플랫폼 revenue를 추정할 수 있음

### 7-5. Segmentation: 어떤 seller가 들어오고 있는가

`lead_type` 상위 분포:

| lead_type | count |
|---|---:|
| `online_medium` | 332 |
| `online_big` | 126 |
| `industry` | 123 |
| `offline` | 104 |
| `online_small` | 77 |

`business_type` 분포:

| business_type | count |
|---|---:|
| `reseller` | 587 |
| `manufacturer` | 242 |
| `other` | 3 |

해석:

- 계약 seller의 다수는 `reseller`
- `manufacturer` 비중도 의미 있게 존재
- seller acquisition 전략에서는 "누가 더 많이 전환되느냐"보다도 "누가 더 오래 팔고 더 큰 GMV를 만드는가"까지 함께 봐야 함

---

## 8. 지금 데이터를 B2B AARRR로 다시 매핑하면

현재 `reference` 문서는 buyer-side AARRR 중심입니다.  
하지만 seller-side를 보조 프레임으로 붙이려면 아래처럼 재정의할 수 있습니다.

| AARRR 단계 | seller-side 해석 | 현재 데이터에서 가능한 지표 |
|---|---|---|
| Acquisition | seller lead 확보 | MQL 수, `origin`별 lead 수 |
| Activation | seller 계약 및 첫 판매 시작 | Closed Deal 수, MQL->Deal 전환율, activation rate, days to first order |
| Retention | seller의 반복 판매 유지 | 2개월 이상 활동 비율, 활동 개월 수 |
| Revenue | seller가 만드는 거래액, 플랫폼 monetization 기반 | seller GMV, seller당 orders, commission 개념 연결 |
| Referral | seller 추천/재유치 | 직접 측정 불가, 일부 `origin=referral`만 참고 가능 |

중요한 점:

- buyer-side AARRR의 `Activation`은 첫 구매 경험
- seller-side AARRR의 `Activation`은 계약 이후 실제 판매 개시

같은 AARRR라도 **대상이 buyer인지 seller인지에 따라 정의가 달라집니다.**

---

## 9. KPI Tree와 어떻게 엮을 것인가

현재 `reference`의 KPI tree는 buyer 중심입니다.

```text
Delivered GMV
 = Delivered Orders x AOV
```

이 구조는 buyer-side 성과 설명에는 적합합니다.  
하지만 seller-side B2B 맥락을 붙이면 아래처럼 **upstream layer**를 하나 더 얹을 수 있습니다.

```text
Seller MQL
 -> Closed Deals
 -> Activated Sellers
 -> Active Sellers
 -> Seller GMV
 -> Platform Revenue (Commission, 개념상)

그리고 이 공급 구조가 Buyer GMV를 떠받친다.
```

### 실무적으로 연결하는 방법

| 프레임워크 | buyer-side 메인 해석 | seller-side 보조 해석 |
|---|---|---|
| KPI Tree | GMV를 Orders와 AOV로 분해 | Seller MQL -> Deal -> Activated Seller -> Seller GMV |
| AARRR | 신규 구매 -> 첫 구매 경험 -> 재구매 -> 매출 | Seller Lead -> 계약 -> 판매 시작 -> 반복 판매 -> monetization |

즉 팀 발표에서는 아래처럼 정리하는 것이 가장 깔끔합니다.

1. **메인 스토리**는 buyer-side KPI tree + buyer-side AARRR
2. **보조 스토리**로 seller-side B2B funnel을 붙인다
3. marketplace 구조상 seller acquisition이 결국 buyer 거래 성과의 upstream driver라고 설명한다

---

## 10. `reference` 문서와의 연결 포인트

### 10-1. AARRR와의 연결

현재 `01_AARRR_Framework_Guide.md`와 `olist_aarrr_metric_selection.md`는 buyer 중심입니다.

이 관점은 유지하는 것이 맞습니다. 이유는 아래와 같습니다.

- 실제 주문/리뷰/재구매 분석의 중심은 buyer data
- buyer retention 3%가 프로젝트의 메인 병목으로 이미 정의돼 있음
- seller funnel은 buyer journey를 직접 설명하는 데이터가 아니라 supply-side context

즉 seller-side B2B 관점은 AARRR를 대체하는 게 아니라, **AARRR의 바깥 upstream layer**로 붙는다고 이해하면 됩니다.

### 10-2. KPI tree와의 연결

현재 `02_KPI_Tree_Guide.md`는 buyer revenue decomposition에 초점이 있습니다.

seller 관점을 붙이면 다음 한 줄이 추가됩니다.

> buyer GMV를 만드는 앞단에는 seller acquisition / activation funnel이 존재한다.

즉,

- buyer KPI tree는 "매출이 어떻게 만들어지는가"
- seller B2B funnel은 "그 매출을 만들 seller 공급이 어떻게 확보되는가"

를 설명합니다.

### 10-3. 발표에서 추천하는 문장

> 이번 Olist 프로젝트는 buyer-side 커머스 분석이 메인입니다.
> 다만 raw data에는 seller acquisition용 B2B funnel이 포함되어 있어,
> marketplace의 공급자 확보 관점도 함께 설명할 수 있습니다.
> 따라서 KPI tree와 AARRR는 buyer 중심으로 유지하되,
> seller-side B2B funnel은 공급 확보와 monetization 맥락을 설명하는 보조 프레임으로 연결하는 것이 적절합니다.

---

## 11. 특히 주의가 필요한 포인트 (자주 혼동되는 개념)

### 11-1. `origin`은 buyer 유입 채널이 아니다

`origin`은 seller lead 유입 채널입니다.  
즉 `paid_search`, `organic_search`, `social`은 buyer acquisition 성과가 아니라 **seller acquisition 성과**입니다.

### 11-2. `closed_deals`는 구매 전환이 아니다

`closed_deals`는 "buyer가 결제했다"는 뜻이 아니라, **seller 계약이 완료됐다**는 뜻입니다.

### 11-3. `declared_monthly_revenue`는 실거래 매출이 아니다

이 값은 seller self-reported value이므로, 실제 GMV와 동일하게 보면 안 됩니다.

### 11-4. 수수료는 중요하지만 현재 데이터로 계산할 수 없다

commission / take rate / payout 데이터가 없으므로,  
seller GMV를 곧바로 플랫폼 revenue로 읽으면 안 됩니다.

---

## 12. 팀 내 합의용 추천 정리

### 한 줄 요약

> 이번 Olist 데이터는 buyer-side B2C 거래 데이터와 seller-side B2B acquisition 데이터가 함께 있는 marketplace 데이터다.

### 프로젝트 관점 정리

- 메인 분석 축: buyer KPI tree + buyer AARRR
- 보조 설명 축: seller B2B funnel
- seller 수수료: marketplace monetization의 핵심 개념이지만, 현재 데이터에서는 실측 불가

### 지금 데이터로 가장 설득력 있게 말할 수 있는 메시지

1. seller lead는 8,000건 들어왔지만 계약은 842건, 전환율은 10.52%
2. 계약 seller 중 실제 판매까지 이어진 seller는 376명으로 activation rate 44.66%
3. activated seller 중 70.74%는 2개월 이상 활동해 retention은 activation 이후엔 상대적으로 나쁘지 않음
4. 따라서 seller-side에서는 `Lead -> Deal`보다 `Deal -> First Sale` 구간이 핵심 병목일 가능성이 높음
5. buyer-side 프로젝트와 연결하면, seller acquisition은 결국 buyer 거래를 떠받치는 공급 확보 활동으로 해석 가능

---

## 13. 데이터 한계

이번 문서 해석에는 아래 한계가 있습니다.

- buyer traffic/session 데이터 없음
- 광고비/CAC/ROAS 데이터 없음
- commission / take rate / payout 데이터 없음
- seller onboarding 완료 이벤트 없음
- seller referral 데이터 없음

따라서 현재는 아래 수준까지 설명하는 것이 가장 정확합니다.

- seller lead acquisition
- seller deal conversion
- seller first-sale activation
- seller repeat activity
- seller GMV
- platform commission은 개념 연결만 가능

---

## 14. 프로젝트 공유 시 핵심 메시지

> "이 프로젝트가 커머스인 건 맞는데, Olist는 marketplace라서 buyer 데이터만 있는 게 아니라 seller 확보용 B2B funnel도 같이 들어 있습니다. 그래서 `marketing_qualified_leads`와 `closed_deals`는 유저 모객 데이터가 아니라 seller acquisition 데이터로 읽어야 합니다. 이 데이터를 보면 seller를 얼마나 데려왔는지, 계약까지 얼마나 전환되는지, 계약 후 실제 판매까지 얼마나 이어지는지를 볼 수 있습니다. 다만 KPI tree와 AARRR의 메인 축은 여전히 buyer 쪽에 두고, seller funnel은 공급자 확보와 수수료 구조를 설명하는 보조 프레임으로 붙이는 것이 가장 자연스럽습니다."
