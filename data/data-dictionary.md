# Data Dictionary — Olist Dataset

> 이 파일은 프로젝트에서 사용하는 모든 데이터셋의 컬럼 명세를 통합 관리합니다.
> 새 파일이 추가될 때마다 아래 업데이트 이력과 해당 섹션을 함께 갱신하세요.

---

## 업데이트 이력

| 날짜 | 내용 | 작성자 |
|------|------|--------|
| 2026-03-28 | 최초 작성 — customers, mql, closed_deals 3개 파일 추가 | 주형 |
| 2026-03-28 | 신규 데이터 확보 — orders, order_items, order_payments, order_reviews, products, sellers, geolocation, category_translation 8개 파일 추가 | 주형 |

---

## 데이터셋 목록

| # | 파일명 | 행 수 | 컬럼 수 | 위치 | 최종 확인일 |
|---|--------|-------|---------|------|------------|
| 1 | olist_customers_dataset.csv | 99,441 | 5 | data/olist_customers_dataset/ | 2026-03-28 |
| 2 | olist_marketing_qualified_leads_dataset.csv | 8,000 | 4 | data/Olist Marketing Funnel/ | 2026-03-28 |
| 3 | olist_closed_deals_dataset.csv | 842 | 14 | data/Olist Marketing Funnel/ | 2026-03-28 |
| 4 | olist_orders_dataset.csv | 99,441 | 8 | data/olist_customers_dataset/ | 2026-03-28 |
| 5 | olist_order_items_dataset.csv | 112,650 | 7 | data/olist_customers_dataset/ | 2026-03-28 |
| 6 | olist_order_payments_dataset.csv | 103,886 | 5 | data/olist_customers_dataset/ | 2026-03-28 |
| 7 | olist_order_reviews_dataset.csv | 99,224 | 7 | data/olist_customers_dataset/ | 2026-03-28 |
| 8 | olist_products_dataset.csv | 32,951 | 9 | data/olist_customers_dataset/ | 2026-03-28 |
| 9 | olist_sellers_dataset.csv | 3,095 | 4 | data/olist_customers_dataset/ | 2026-03-28 |
| 10 | olist_geolocation_dataset.csv | 1,000,163 | 5 | data/olist_customers_dataset/ | 2026-03-28 |
| 11 | product_category_name_translation.csv | 71 | 2 | data/olist_customers_dataset/ | 2026-03-28 |

---

## 1. olist_customers_dataset.csv

> 고객 정보 테이블. `customer_id`는 주문마다 새로 생성되므로, 재구매 분석 시 `customer_unique_id` 기준으로 집계해야 함.

| 컬럼명 | 타입 | 고유값 수 | Null | 설명 |
|--------|------|-----------|------|------|
| `customer_id` | string | 99,441 | 0 | 주문별 고객 ID — `orders` 테이블과 JOIN 키 |
| `customer_unique_id` | string | 96,096 | 0 | 실제 고객 식별자 — 재구매·코호트 분석 핵심 키 |
| `customer_zip_code_prefix` | string | 14,994 | 0 | 우편번호 앞 5자리 — `geolocation` 테이블과 연결 가능 |
| `customer_city` | string | 4,119 | 0 | 고객 도시명 (소문자 비정제 상태, 전처리 필요) |
| `customer_state` | string | 27 | 0 | 고객 주(州) — 브라질 27개 주 전체 커버 |

**주요 분포**

| State | 건수 | 비율 |
|-------|------|------|
| SP (상파울루) | 41,746 | 42% |
| RJ (리우데자네이루) | 12,852 | 13% |
| MG (미나스제라이스) | 11,635 | 12% |
| RS | 5,466 | 5% |
| PR | 5,045 | 5% |

**분석 시 유의사항**
- `customer_id` ≠ `customer_unique_id` — 재구매 고객은 주문마다 `customer_id`가 달라짐
- SP 집중도 42% — 지역별 비교 분석 시 편향 주의

---

## 2. olist_marketing_qualified_leads_dataset.csv

> MQL(Marketing Qualified Lead) 테이블. Seller 후보가 Olist에 최초 접촉한 기록. `mql_id`로 `closed_deals`와 JOIN해 전환 여부 확인 가능.

| 컬럼명 | 타입 | 고유값 수 | Null | 설명 |
|--------|------|-----------|------|------|
| `mql_id` | string | 8,000 | 0 | MQL 고유 ID — `closed_deals` 테이블과 JOIN 키 |
| `first_contact_date` | date | 336 | 0 | 최초 접촉 날짜 (2017~2018) |
| `landing_page_id` | string | 495 | 0 | 유입된 랜딩 페이지 ID |
| `origin` | string | 11 | 60 | 유입 채널 (예: paid_search, organic_search, social 등) — **분석 핵심 컬럼** |

**origin 주요 값 예시**
`paid_search` / `organic_search` / `social` / `other` / `unknown` 등 11개 채널

**분석 시 유의사항**
- `origin` Null 60건 — 채널 미상 처리 기준 사전 정의 필요
- 8,000건 중 `closed_deals`에 연결되는 건수는 842건 → **전환율 약 10.5%**

---

## 3. olist_closed_deals_dataset.csv

> 계약 완료(Closed Deal) 테이블. MQL 중 실제 계약으로 전환된 Seller 정보. `mql_id`로 MQL과, `seller_id`로 거래 데이터와 연결.

| 컬럼명 | 타입 | 고유값 수 | Null | 설명 |
|--------|------|-----------|------|------|
| `mql_id` | string | 842 | 0 | MQL ID — `mql` 테이블과 JOIN 키 |
| `seller_id` | string | 842 | 0 | Seller ID — E-Commerce 거래 데이터와 JOIN 키 |
| `sdr_id` | string | 32 | 0 | SDR(Sales Dev Rep) 담당자 ID |
| `sr_id` | string | 22 | 0 | SR(Sales Rep) 담당자 ID |
| `won_date` | datetime | 824 | 0 | 계약 완료 일시 |
| `business_segment` | string | 34 | 1 | 사업 카테고리 (예: home_appliances, watches, party 등) |
| `lead_type` | string | 9 | 6 | 리드 유형 (예: online_small, offline, other 등) |
| `lead_behaviour_profile` | string | 10 | 177 | 리드 행동 프로파일 (예: eagle, shark, cat, wolf 조합) |
| `has_company` | boolean | 3 | 779 | 사업자 등록 여부 |
| `has_gtin` | boolean | 3 | 778 | GTIN(상품 바코드) 보유 여부 |
| `average_stock` | string | 7 | 776 | 평균 재고 수준 (예: 20-50, 50-200, unknown 등) |
| `business_type` | string | 4 | 10 | 사업 유형 (manufacturer / reseller / other 등) |
| `declared_product_catalog_size` | float | 34 | 773 | 셀러 신고 상품 수 |
| `declared_monthly_revenue` | float | 27 | 0 | 셀러 신고 월매출 |

**분석 시 유의사항**
- `has_company`, `has_gtin`, `average_stock`, `declared_product_catalog_size` — Null 비율 90%+ → 보조 지표로만 활용
- `lead_behaviour_profile` Null 177건 (21%) — 세그먼트 분석 시 별도 처리 필요
- `declared_monthly_revenue`는 셀러 자기신고값 → 실제 거래 성과와 비교 시 괴리 가능

---

## 4. olist_orders_dataset.csv

> 주문 마스터 테이블. 주문의 전체 라이프사이클(구매→승인→배송→완료)을 담음. `customer_id`로 customers와, `order_id`로 하위 3개 테이블과 JOIN.

| 컬럼명 | 타입 | 고유값 수 | Null | 설명 |
|--------|------|-----------|------|------|
| `order_id` | string | 99,441 | 0 | 주문 고유 ID — 하위 테이블들과 JOIN 키 |
| `customer_id` | string | 99,441 | 0 | 고객 ID — `customers` 테이블과 JOIN 키 |
| `order_status` | string | 8 | 0 | 주문 상태 — 아래 분포 참조 |
| `order_purchase_timestamp` | datetime | 98,875 | 0 | 구매 시각 |
| `order_approved_at` | datetime | 90,733 | 160 | 결제 승인 시각 |
| `order_delivered_carrier_date` | datetime | 81,018 | 1,783 | 배송사 인수 시각 |
| `order_delivered_customer_date` | datetime | 95,664 | 2,965 | 고객 수령 시각 |
| `order_estimated_delivery_date` | datetime | 459 | 0 | 예상 배송 완료 시각 |

**order_status 분포**

| status | 건수 | 비율 |
|--------|------|------|
| delivered | 96,478 | 97.0% |
| shipped | 1,107 | 1.1% |
| canceled | 625 | 0.6% |
| unavailable | 609 | 0.6% |
| invoiced | 314 | 0.3% |
| processing | 301 | 0.3% |
| created | 5 | — |
| approved | 2 | — |

**분석 시 유의사항**
- 실구매 분석 시 `order_status = 'delivered'` 필터 권장 (97% 해당)
- `order_delivered_customer_date` Null 2,965건 → 미배송(canceled/shipped 등) 포함
- 리드타임: `order_delivered_customer_date - order_purchase_timestamp`

---

## 5. olist_order_items_dataset.csv

> 주문 상세 테이블. 하나의 주문에 여러 상품이 포함될 수 있음. `order_id`로 orders와, `product_id`로 products와, `seller_id`로 sellers와 JOIN.

| 컬럼명 | 타입 | 고유값 수 | Null | 설명 |
|--------|------|-----------|------|------|
| `order_id` | string | 98,666 | 0 | 주문 ID — `orders` 테이블과 JOIN 키 |
| `order_item_id` | int | 21 | 0 | 주문 내 상품 순번 (1~21) — 최대 21개 상품/주문 |
| `product_id` | string | 32,951 | 0 | 상품 ID — `products` 테이블과 JOIN 키 |
| `seller_id` | string | 3,095 | 0 | 판매자 ID — `sellers` 테이블과 JOIN 키 |
| `shipping_limit_date` | datetime | 93,318 | 0 | 배송 기한 |
| `price` | float | 5,968 | 0 | 상품 단가 (BRL) |
| `freight_value` | float | 6,999 | 0 | 배송비 (BRL) |

**price 분포 요약**

| 통계 | 값 |
|------|-----|
| 평균 | R$ 120.7 |
| 중앙값 | R$ 75.0 |
| 25% | R$ 39.9 |
| 75% | R$ 134.9 |
| 최대 | R$ 6,735.0 |

**분석 시 유의사항**
- 총매출 = `SUM(price + freight_value)` — 상품가 + 배송비 합산
- 주문당 평균 상품수: 112,650 / 98,666 ≈ 1.14개 (단품 주문이 대부분)

---

## 6. olist_order_payments_dataset.csv

> 결제 정보 테이블. 1개 주문에 복수 결제수단 사용 가능 (할부+쿠폰 등). `order_id`로 orders와 JOIN.

| 컬럼명 | 타입 | 고유값 수 | Null | 설명 |
|--------|------|-----------|------|------|
| `order_id` | string | 99,440 | 0 | 주문 ID — `orders` 테이블과 JOIN 키 |
| `payment_sequential` | int | 29 | 0 | 결제 순번 (복수 결제수단 시 1, 2, 3 …) |
| `payment_type` | string | 5 | 0 | 결제 수단 — 아래 분포 참조 |
| `payment_installments` | int | 24 | 0 | 할부 개월 수 (1 = 일시불, 최대 24개월) |
| `payment_value` | float | 29,077 | 0 | 실결제 금액 (BRL) |

**payment_type 분포**

| 결제수단 | 건수 | 비율 |
|---------|------|------|
| credit_card | 76,795 | 73.9% |
| boleto (계좌이체) | 19,784 | 19.0% |
| voucher | 5,775 | 5.6% |
| debit_card | 1,529 | 1.5% |
| not_defined | 3 | — |

**분석 시 유의사항**
- 1주문 = 1행이 아님 → 주문별 합산 시 `GROUP BY order_id, SUM(payment_value)` 필요
- `payment_value`는 `order_items.price + freight_value`와 미세 차이 가능 (쿠폰/할인 반영)

---

## 7. olist_order_reviews_dataset.csv

> 구매 후기 테이블. 주문 완료 후 고객이 남긴 별점·텍스트 리뷰. `order_id`로 orders와 JOIN.

| 컬럼명 | 타입 | 고유값 수 | Null | 설명 |
|--------|------|-----------|------|------|
| `review_id` | string | 98,410 | 0 | 리뷰 고유 ID |
| `order_id` | string | 98,673 | 0 | 주문 ID — `orders` 테이블과 JOIN 키 |
| `review_score` | int | 5 | 0 | 별점 (1~5) |
| `review_comment_title` | string | 4,527 | 87,656 | 리뷰 제목 — **Null 88.3%** (사실상 미사용) |
| `review_comment_message` | string | 36,159 | 58,247 | 리뷰 본문 — Null 58.7% |
| `review_creation_date` | datetime | 636 | 0 | 리뷰 작성 시각 |
| `review_answer_timestamp` | datetime | 98,248 | 0 | 리뷰 응답 시각 |

**review_score 분포**

| 별점 | 건수 | 비율 |
|------|------|------|
| 5 | 57,328 | 57.8% |
| 4 | 19,142 | 19.3% |
| 3 | 8,179 | 8.2% |
| 2 | 3,151 | 3.2% |
| 1 | 11,424 | 11.5% |

**분석 시 유의사항**
- `review_comment_title` Null 88% → 분석 제외 권장
- 별점 분포 J-curve (5점 최다, 1점 2위) — 양극화 패턴
- 1점 리뷰(11.5%)와 배송 지연 상관관계 분석 가치 있음

---

## 8. olist_products_dataset.csv

> 상품 정보 테이블. `product_id`로 `order_items`와 JOIN. 카테고리명은 포르투갈어 → `category_translation`으로 영문 매핑.

| 컬럼명 | 타입 | 고유값 수 | Null | 설명 |
|--------|------|-----------|------|------|
| `product_id` | string | 32,951 | 0 | 상품 고유 ID |
| `product_category_name` | string | 73 | 610 | 상품 카테고리 (포르투갈어) — `category_translation`으로 영문 변환 |
| `product_name_lenght` | float | 66 | 610 | 상품명 글자수 (오타: lenght) |
| `product_description_lenght` | float | 2,960 | 610 | 상품 설명 글자수 |
| `product_photos_qty` | float | 19 | 610 | 상품 이미지 수 |
| `product_weight_g` | float | 2,204 | 2 | 상품 무게 (g) |
| `product_length_cm` | float | 99 | 2 | 상품 길이 (cm) |
| `product_height_cm` | float | 102 | 2 | 상품 높이 (cm) |
| `product_width_cm` | float | 95 | 2 | 상품 너비 (cm) |

**카테고리 Top 10 (포르투갈어)**

| 카테고리 | 건수 |
|---------|------|
| cama_mesa_banho (침구/욕실) | 3,029 |
| esporte_lazer (스포츠/레저) | 2,867 |
| moveis_decoracao (가구/인테리어) | 2,657 |
| beleza_saude (뷰티/건강) | 2,444 |
| utilidades_domesticas (주방용품) | 2,335 |
| automotivo (자동차용품) | 1,900 |
| informatica_acessorios (IT악세서리) | 1,639 |
| brinquedos (완구) | 1,411 |
| relogios_presentes (시계/선물) | 1,329 |
| telefonia (통신기기) | 1,134 |

**분석 시 유의사항**
- Null 610건 — `category_name` 포함 전체 스펙 컬럼 일괄 누락 (동일 product_id 그룹)
- `product_name_lenght` 오타 주의 (lenght → length 아님)
- 크기/무게는 배송비(`freight_value`) 결정 요인

---

## 9. olist_sellers_dataset.csv

> 판매자 정보 테이블. `seller_id`로 `order_items`, `closed_deals`와 JOIN. 지역 분포 분석 가능.

| 컬럼명 | 타입 | 고유값 수 | Null | 설명 |
|--------|------|-----------|------|------|
| `seller_id` | string | 3,095 | 0 | 판매자 고유 ID |
| `seller_zip_code_prefix` | int | 2,246 | 0 | 우편번호 앞 5자리 — `geolocation`과 연결 가능 |
| `seller_city` | string | 611 | 0 | 판매자 도시 |
| `seller_state` | string | 23 | 0 | 판매자 주(州) |

**seller_state 상위 5개**

| State | 건수 | 비율 |
|-------|------|------|
| SP (상파울루) | 1,849 | 59.7% |
| PR | 349 | 11.3% |
| MG | 244 | 7.9% |
| SC | 190 | 6.1% |
| RJ | 171 | 5.5% |

**분석 시 유의사항**
- SP 집중도 59.7% — 판매자도 고객과 마찬가지로 SP 편중
- `closed_deals.seller_id`와 JOIN 시 B2B 온보딩 Seller 특성 파악 가능

---

## 10. olist_geolocation_dataset.csv

> 우편번호 → 위경도 매핑 테이블. `customers/sellers`의 zip_code_prefix와 JOIN해 지도 시각화에 활용. 1개 우편번호에 복수 좌표 포함.

| 컬럼명 | 타입 | 고유값 수 | Null | 설명 |
|--------|------|-----------|------|------|
| `geolocation_zip_code_prefix` | int | 19,015 | 0 | 우편번호 앞 5자리 — JOIN 키 |
| `geolocation_lat` | float | 717,360 | 0 | 위도 |
| `geolocation_lng` | float | 717,613 | 0 | 경도 |
| `geolocation_city` | string | 8,011 | 0 | 도시명 |
| `geolocation_state` | string | 27 | 0 | 주(州) |

**분석 시 유의사항**
- 총 100만 행 — 1개 zip_code_prefix당 평균 53개 좌표 → JOIN 시 **반드시 집계(평균/대표값) 후 사용**, 그대로 JOIN하면 행 폭발
- 지도 시각화 전 `groupby(zip_code_prefix).mean()` 처리 필수

---

## 11. product_category_name_translation.csv

> 포르투갈어 카테고리명 → 영어 번역 테이블. `products.product_category_name`과 LEFT JOIN해 영문 분석에 활용.

| 컬럼명 | 타입 | 고유값 수 | Null | 설명 |
|--------|------|-----------|------|------|
| `product_category_name` | string | 71 | 0 | 포르투갈어 카테고리명 — `products` 테이블과 JOIN 키 |
| `product_category_name_english` | string | 71 | 0 | 영어 카테고리명 |

**분석 시 유의사항**
- `products`의 73개 카테고리 중 71개만 번역 수록 → LEFT JOIN 후 Null 2개 별도 처리
- 분석 리포트에서 카테고리명 표기 시 이 테이블 사용 권장

---

## 테이블 관계도

```
[B2B 마케팅 퍼널]
olist_marketing_qualified_leads
        │
        │ mql_id
        ▼
olist_closed_deals ──── seller_id ─────────────────────────┐
                                                            │
[E-Commerce 거래]                                           │
olist_customers_dataset ◀── customer_id ── olist_orders_dataset ──── order_id ──▶ olist_order_items_dataset
        │                                          │                                        │
        │ zip_code_prefix                           │ order_id                               │ product_id / seller_id
        ▼                                          ▼                                        ▼
olist_geolocation_dataset          olist_order_payments_dataset          olist_products_dataset
                                   olist_order_reviews_dataset           olist_sellers_dataset
                                                                                  │
                                                                                  │ zip_code_prefix
                                                                                  ▼
                                                                    olist_geolocation_dataset

[보조]
olist_products_dataset ──── product_category_name ──▶ product_category_name_translation
```

**핵심 JOIN 경로**
- 주문 성과 분석: `orders → order_items → products (+ category_translation)`
- 결제 분석: `orders → order_payments`
- 고객 만족도: `orders → order_reviews`
- Seller 연결: `order_items.seller_id = sellers.seller_id`
- B2B↔거래 연결: `closed_deals.seller_id = order_items.seller_id`
