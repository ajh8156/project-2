# Olist 서비스 성과 개선용 AARRR 지표 선별안

> 최종 수정일: 2026-03-31

## 1. 문서 목적

이 문서는 `Olist의 성장 진단 컨설팅을 통한 액션 플랜 제시` 프로젝트에서,  
**서비스 기획 관점으로 어떤 AARRR 지표를 채택해야 하는지**를 정리한 공유용 기준 문서입니다.

이번 문서는 아래 원칙을 따릅니다.

1. **KPI 트리 문서와 관점을 동일하게 유지한다.**
2. **Raw data로 직접 계산 가능한 지표만 채택한다.**
3. **AARRR 단계별로 Action Plan으로 연결 가능한 지표만 남긴다.**
4. **다른 인원도 이해할 수 있도록, 왜 이 관점을 택했는지까지 함께 설명한다.**

---

## 2. 결론 먼저

이번 프로젝트의 AARRR는 **Buyer 서비스 성과형 AARRR**로 설계하는 것이 맞습니다.

즉, 메인 관점은 아래입니다.

- `Acquisition`: 신규 구매 고객 확보
- `Activation`: 첫 구매가 문제 없이 완료되고 기대 수준의 경험을 제공받는가
- `Retention`: 고객이 다시 구매하는가
- `Revenue`: 실제 거래 규모와 주문당 가치가 증가하는가
- `Referral`: 직접 추천 데이터는 없으므로, 리뷰/고평점 기반의 간접 시그널만 제한적으로 본다

그리고 `마케팅 퍼널 데이터(MQL, Closed Deal)`는 **별도 보조 지표**로 관리하는 것이 맞습니다.

---

## 3. 왜 KPI 트리와 관점을 같게 가져가야 하는가

이미 KPI 트리에서는 아래 관점으로 정리했습니다.

- 메인 관점: `Buyer 서비스 성과`
- 메인 구조: `Delivered GMV -> Orders -> Customers / Frequency / AOV`
- Guardrail: `배송 지연`, `저평점`, `취소/미가용`
- 보조 관점: `Seller acquisition efficiency`

즉, KPI 트리도 이미 **서비스 기획 관점에서 buyer side를 메인**, seller funnel은 **marketplace 특성 설명용 보조**로 사용했습니다.

만약 이번 AARRR에서 갑자기 seller funnel을 메인 Acquisition으로 올리면 문제가 생깁니다.

- KPI 트리와 AARRR의 기준 대상이 달라집니다.
- 발표 메시지가 흔들립니다.
- 팀원마다 "우리가 buyer 문제를 푸는지, seller 확보 문제를 푸는지" 해석이 달라집니다.
- Action Plan의 우선순위가 흐려집니다.

따라서 **KPI 트리와 AARRR는 같은 관점으로 묶어야** 합니다.

---

## 4. "마케팅 퍼널 데이터가 있는데 왜 내부 서비스 지표를 메인으로 보나요?"에 대한 답

이 질문은 팀원 누구나 한 번쯤 할 수 있는 질문입니다.  
그래서 이번 문서에 명확히 남겨 둡니다.

### 4-1. 마케팅 퍼널 데이터는 존재한다

실제로 아래 데이터는 존재합니다.

- `olist_marketing_qualified_leads_dataset.csv`
- `olist_closed_deals_dataset.csv`

이 데이터로 볼 수 있는 것은 아래입니다.

- seller lead 수 (`MQL`)
- seller 계약 완료 수 (`Closed Deal`)
- `MQL → Deal` 전환율
- `origin`별 seller lead 유입 구조

### 4-2. 하지만 이 데이터는 buyer 광고 성과 데이터가 아니다

이 데이터는 **seller 확보용 B2B funnel 데이터**입니다.  
즉, Olist 플랫폼에 입점할 seller를 얼마나 잘 유치하고 계약시키는지 보는 데이터입니다.

반면 우리가 지금 서비스 기획 관점에서 메인으로 봐야 하는 질문은 아래입니다.

- 고객은 첫 구매까지 잘 도달하는가?
- 첫 구매 경험은 좋은가?
- 다시 사는가?
- 주문 가치가 커지는가?
- 서비스 품질이 재구매를 막고 있지는 않은가?

이 질문에 답하는 데이터는 `orders`, `order_items`, `customers`, `payments`, `reviews`입니다.

### 4-3. 따라서 추천하는 해석은 이렇다

> `마케팅 퍼널 데이터`는 버리는 것이 아니라,  
> **marketplace의 supply-side 성장 참고 지표**로 활용한다.  
> 다만 이번 프로젝트의 메인 AARRR는 `Buyer 서비스 성과형`으로 두고,  
> seller funnel은 보조 섹션 또는 appendix 성격으로 붙인다.

이렇게 해야 서비스 기획 관점과 marketplace 맥락을 동시에 살릴 수 있습니다.

---

## 5. 데이터 범위와 계산 기준

### 분석 기간

- `2017-01-01 ~ 2018-08-31`

### 사용 데이터

- Buyer/서비스 성과: `customers`, `orders`, `order_items`, `payments`, `reviews`
- Seller funnel 보조: `olist_marketing_qualified_leads`, `olist_closed_deals`

### 계산 기준

- 주문 기준은 `delivered`를 우선 사용
- 고객 식별은 반드시 `customer_unique_id`
- 첫 구매는 `고객별 첫 delivered 주문`
- 리뷰 품질은 `1~2점 저평점`, `5점 고평점`으로 구분

---

## 6. 추천 AARRR 구조

```text
A. Acquisition
 -> 신규 구매 고객 수

A. Activation
 -> 첫 구매 완료 고객 수
 -> 첫 구매 배송 지연율
 -> 첫 구매 저평점 비중

R. Retention
 -> 재구매 고객 수
 -> 재구매 고객 비중
 -> 고객당 주문 수
 -> 반복 주문 비중

R. Revenue
 -> Delivered GMV
 -> Delivered Orders
 -> AOV
 -> 주문당 평균 상품 수
 -> 다품목 주문 비중

R. Referral
 -> 직접 추천 데이터 없음
 -> 리뷰 작성률, 5점 리뷰 비중을 대체 참고 지표로 제한적 활용

보조 지표
 -> MQL 수
 -> Closed Deal 수
 -> MQL→Deal 전환율
```

---

## 7. 최종 채택 지표

| 단계 | KPI | 정의 | 목적 | 선정 근거 | 현재 수치 |
|---|---|---|---|---|---|
| Acquisition | 신규 구매 고객 수 | 분석 기간 내 첫 delivered 주문을 만든 고객 수 | 유입된 buyer가 실제 구매 고객으로 전환된 결과 확인 | 방문자/세션이 없으므로 이번 데이터에서 가장 현실적인 Acquisition 지표 | `93,094명` |
| Activation | 첫 구매 완료 고객 수 | 고객별 첫 delivered 주문 고객 수 | 첫 구매 경험의 모수 확인 | 서비스 기획 관점에서 Activation을 `가입`이 아니라 `첫 가치 실현`로 봐야 함 | `93,094명` |
| Activation | 첫 구매 배송 지연율 | 첫 delivered 주문 중 지연 비중 | 첫 구매 경험 품질 진단 | 첫 경험이 나쁘면 Retention으로 이어지지 못함 | `8.16%` |
| Activation | 첫 구매 저평점 비중 | 첫 delivered 주문 리뷰 중 1~2점 비중 | 첫 구매 만족도 진단 | Activation은 단순 구매 완료가 아니라 기대 충족까지 포함해야 함 | `12.82%` |
| Retention | 재구매 고객 수 | 2회 이상 delivered 주문 고객 수 | 재구매 기반 확인 | 성장의 질을 보여주는 핵심 지표 | `2,789명` |
| Retention | 재구매 고객 비중 | `재구매 고객 수 / 신규 구매 고객 수` | 고객 기반의 취약성 진단 | Olist의 가장 큰 구조적 문제를 보여줌 | `3.00%` |
| Retention | 고객당 주문 수 | `Delivered Orders / 신규 구매 고객 수` | 구매 빈도 진단 | 값이 1에 가까우면 대부분 1회 구매에 머문다는 뜻 | `1.0335` |
| Retention | 반복 주문 비중 | `두 번째 주문 이후 주문 수 / Delivered Orders` | 실제 주문 볼륨에서 재구매 기여도 확인 | 고객 수가 아니라 반복 행동이 얼마나 매출을 받치는지 확인 | `3.23%` |
| Revenue | Delivered GMV | delivered 주문의 `price + freight_value` 합 | 전체 거래 규모 확인 | KPI 트리와 동일한 최상위 성과 지표 | `BRL 15,373,120` |
| Revenue | Delivered Orders | delivered 주문 수 | 매출의 주문량 축 설명 | `GMV = Orders × AOV`로 분해 가능 | `96,211건` |
| Revenue | AOV | `Delivered GMV / Delivered Orders` | 주문당 가치 확인 | 주문량 외 매출 성장을 설명하는 핵심 축 | `BRL 159.79` |
| Revenue | 주문당 평균 상품 수 | 주문당 평균 상품 개수 | basket expansion 여지 확인 | cross-sell / bundle 액션과 직결 | `1.1421개` |
| Revenue | 다품목 주문 비중 | 2개 이상 상품 포함 주문 비중 | 단품 주문 구조 여부 확인 | AOV 개선 여지 판단에 유용 | `9.98%` |
| Referral(대체) | 리뷰 작성률 | 리뷰가 존재하는 주문 비중 | 고객의 피드백 참여도 확인 | 직접 추천은 아니지만 만족도 표출 가능성 확인용 | `99.33%` |
| Referral(대체) | 5점 리뷰 비중 | 리뷰 주문 중 5점 비중 | 잠재적 advocacy 신호 확인 | Referral 데이터 부재 시 가장 현실적인 보조 시그널 | `59.18%` |
| Referral(대체) | 저평점 리뷰 비중 | 리뷰 주문 중 1~2점 비중 | 부정적 WOM 리스크 확인 | Referral을 긍정 지표만으로 보면 착시가 생김 | `12.76%` |
| 보조 | MQL 수 | seller lead 수 | supply-side 유입 모수 확인 | marketplace 특성상 참고 가치 있음 | `8,000건` |
| 보조 | Closed Deal 수 | 계약 완료 seller 수 | 공급 전환 성과 확인 | seller 확보 효율을 보여줌 | `842건` |
| 보조 | MQL→Deal 전환율 | `Closed Deals / MQL` | seller funnel 효율 진단 | 서비스 AARRR의 메인은 아니지만 맥락 설명에 유효 | `10.53%` |

---

## 8. 단계별 상세 설명

## 8-1. Acquisition

### 채택 지표

- 신규 구매 고객 수

### 왜 이렇게 정의했는가

보통 AARRR의 Acquisition은 `방문자`, `유입 사용자`, `회원가입자`를 봅니다.  
하지만 이번 raw data에는 방문자/세션 로그가 없습니다.

따라서 이번 프로젝트에서는 Acquisition을 아래처럼 재정의하는 것이 가장 타당합니다.

> **서비스 기획 관점의 Acquisition = 실제 구매까지 도달한 신규 고객 확보**

### 현재 해석

신규 구매 고객 수는 `93,094명`입니다.  
겉보기에는 신규 유입이 충분해 보이지만, 이후 Retention 단계로 거의 이어지지 않는 것이 핵심 문제입니다.

---

## 8-2. Activation

### 채택 지표

- 첫 구매 완료 고객 수
- 첫 구매 배송 지연율
- 첫 구매 저평점 비중

### 왜 이렇게 정의했는가

서비스 기획 관점에서 Activation은 단순 클릭이나 가입이 아닙니다.  
고객이 **서비스의 첫 핵심 가치를 실제로 경험한 순간**이어야 합니다.

이 프로젝트에서는 그 순간을 아래처럼 정의하는 것이 맞습니다.

> **Activation = 첫 구매가 완료되고, 첫 구매 경험이 문제 없이 전달된 상태**

즉, 첫 구매가 있어도 배송 지연이 크고 저평점이 높다면 Activation이 온전하게 일어난 것으로 보기 어렵습니다.

### 현재 해석

- 첫 구매 배송 지연율: `8.16%`
- 첫 구매 저평점 비중: `12.82%`

첫 구매 단계에서 이미 일정 비율의 고객이 나쁜 경험을 겪고 있을 가능성이 높습니다.  
즉, Retention이 약한 이유를 `유입 품질`만으로 보기 어렵고, **첫 구매 경험 설계 문제**도 함께 의심해야 합니다.

---

## 8-3. Retention

### 채택 지표

- 재구매 고객 수
- 재구매 고객 비중
- 고객당 주문 수
- 반복 주문 비중

### 왜 이렇게 정의했는가

이번 프로젝트의 핵심 병목은 여기에 있습니다.  
서비스 기획 관점에서 Olist의 문제는 "고객이 안 오느냐"보다 **"온 고객이 다시 오지 않느냐"**에 더 가깝습니다.

### 현재 해석

- 재구매 고객 수: `2,789명`
- 재구매 고객 비중: `3.00%`
- 고객당 주문 수: `1.0335`
- 반복 주문 비중: `3.23%`

이 수치는 Olist가 신규 확보형 구조에 과도하게 의존하고 있음을 보여줍니다.  
즉, CRM, 배송 경험 개선, 카테고리 재진입 설계가 핵심 우선순위가 됩니다.

---

## 8-4. Revenue

### 채택 지표

- Delivered GMV
- Delivered Orders
- AOV
- 주문당 평균 상품 수
- 다품목 주문 비중

### 왜 이렇게 정의했는가

Revenue는 단순 매출 총액만 보면 안 됩니다.  
서비스 기획 관점에서도 결국 `무엇이 매출을 만들고 있는가`를 봐야 합니다.

이번 프로젝트에서는 KPI 트리와 동일하게 아래 구조가 가장 안정적입니다.

`Delivered GMV = Delivered Orders × AOV`

그리고 AOV는 다시 `basket size` 관점으로 해석해야 Action이 나옵니다.

### 현재 해석

- Delivered GMV: `BRL 15.37M`
- Delivered Orders: `96,211건`
- AOV: `BRL 159.79`
- 주문당 평균 상품 수: `1.1421개`
- 다품목 주문 비중: `9.98%`

즉, 현재 Revenue 구조는 고빈도·고장바구니 구조가 아니라 **단품 위주의 단발 주문 구조**에 가깝습니다.

---

## 8-5. Referral

### 채택 방식

Referral은 **정식 KPI로 채택하지 않고, 대체 참고 지표만 제한적으로 사용**하는 것을 추천합니다.

### 이유

이번 raw data에는 아래가 없습니다.

- 추천 코드 사용 데이터
- 친구 초대 데이터
- 공유 이벤트
- 바이럴 유입 식별 로그

즉, **진짜 Referral은 측정할 수 없습니다.**

그래서 이번 프로젝트에서는 아래처럼 처리하는 것이 가장 정직합니다.

> Referral 단계는 직접 측정 불가  
> 단, 고객 만족과 자발적 구전 가능성을 간접적으로 보기 위해  
> `리뷰 작성률`, `5점 리뷰 비중`, `저평점 리뷰 비중`을 참고 지표로만 활용

### 현재 해석

- 리뷰 작성률: `99.33%`
- 5점 리뷰 비중: `59.18%`
- 저평점 리뷰 비중: `12.76%`

즉, 긍정적인 목소리도 충분하지만, 동시에 부정적 경험도 무시하기 어렵습니다.  
Referral을 낙관적으로만 해석하면 안 됩니다.

---

## 9. 이번 프로젝트에서 제외해야 할 AARRR 지표

| 단계 | 제외 지표 | 제외 이유 |
|---|---|---|
| Acquisition | 방문자 수, 세션 수, 신규 회원가입 수 | raw data 부재 |
| Acquisition | paid / organic / direct buyer 유입 구성 | buyer traffic source 부재 |
| Activation | 회원가입 완료율, PDP 조회율, Add-to-Cart Rate | event log 부재 |
| Activation | checkout step별 이탈률 | checkout event 부재 |
| Retention | 앱 재방문율, DAU/WAU/MAU | app/web event 부재 |
| Revenue | CAC, ROAS, ROI | 광고비 데이터 부재 |
| Referral | 초대 전환율, 추천 코드 사용률, 공유 전환율 | referral 데이터 부재 |

---

## 10. 발표용 추천 메시지

발표에서는 아래 문장을 그대로 써도 됩니다.

> KPI 트리와 동일하게, 이번 AARRR도 `Buyer 서비스 성과 관점`으로 설계했습니다.  
> Olist raw data에는 seller 마케팅 퍼널 데이터가 존재하지만, 이는 buyer 광고 성과가 아니라 seller 확보용 B2B funnel 데이터입니다.  
> 따라서 본 프로젝트의 메인 프레임은 `신규 구매 -> 첫 구매 경험 -> 재구매 -> 매출` 흐름으로 잡고,  
> seller funnel은 marketplace 특성을 설명하는 보조 지표로만 활용했습니다.

---

## 11. 최종 추천

팀이 먼저 합의해야 할 핵심 AARRR 지표는 아래 8개입니다.

1. 신규 구매 고객 수
2. 첫 구매 배송 지연율
3. 첫 구매 저평점 비중
4. 재구매 고객 비중
5. 고객당 주문 수
6. Delivered GMV
7. AOV
8. 5점 리뷰 비중(Referral 대체 참고)

그리고 seller funnel은 아래 1줄로 보조 관리하면 충분합니다.

> `Seller Funnel Reference = MQL 수 / Closed Deal 수 / MQL→Deal 전환율`

---

## 12. 수치 산출 기준 메모

- 기간: `2017-01-01 ~ 2018-08-31`
- 신규 구매 고객: 기간 내 첫 delivered 주문 고객
- Activation: 첫 delivered 주문 및 첫 구매 경험 품질
- Retention: 2회 이상 delivered 주문 기준
- Revenue: delivered 주문 기준 `price + freight_value`
- Referral: 직접 측정 불가, 리뷰 기반 대체 참고 지표만 사용

