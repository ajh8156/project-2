# Olist 프로젝트 ERD (Entity-Relationship Diagram)

> 작성일: 2026-04-14
> 목적: 프로젝트에서 사용하는 전체 데이터셋의 구조와 테이블 간 관계를 시각적으로 이해하기

---

## 1. 전체 구조 한눈에 보기

우리 프로젝트 데이터는 크게 **3개 영역**으로 나뉩니다.

```text
┌─────────────────────────────────────────────────────────┐
│                    우리 프로젝트 데이터                      │
│                                                         │
│  ┌───────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  Olist B2C    │  │ Olist B2B    │  │  Kaggle      │  │
│  │  (거래 데이터)  │  │ (셀러 유치)   │  │ (CRM/쿠폰)   │  │
│  │  9개 테이블    │  │  2개 테이블   │  │  8개 테이블   │  │
│  └───────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
```

---

## 2. Olist B2C 거래 데이터 ERD (메인)

> 고객이 상품을 검색하고, 주문하고, 결제하고, 리뷰를 남기는 흐름

```mermaid
erDiagram
    customers {
        string customer_id PK
        string customer_unique_id
        string customer_zip_code_prefix FK
        string customer_city
        string customer_state
    }

    orders {
        string order_id PK
        string customer_id FK
        string order_status
        datetime order_purchase_timestamp
        datetime order_approved_at
        datetime order_delivered_carrier_date
        datetime order_delivered_customer_date
        datetime order_estimated_delivery_date
    }

    order_items {
        string order_id FK
        int order_item_id
        string product_id FK
        string seller_id FK
        datetime shipping_limit_date
        float price
        float freight_value
    }

    order_payments {
        string order_id FK
        int payment_sequential
        string payment_type
        int payment_installments
        float payment_value
    }

    order_reviews {
        string review_id PK
        string order_id FK
        int review_score
        string review_comment_title
        string review_comment_message
        datetime review_creation_date
        datetime review_answer_timestamp
    }

    products {
        string product_id PK
        string product_category_name FK
        int product_name_lenght
        int product_description_lenght
        int product_photos_qty
        float product_weight_g
        float product_length_cm
        float product_height_cm
        float product_width_cm
    }

    sellers {
        string seller_id PK
        string seller_zip_code_prefix FK
        string seller_city
        string seller_state
    }

    geolocation {
        string geolocation_zip_code_prefix PK
        float geolocation_lat
        float geolocation_lng
        string geolocation_city
        string geolocation_state
    }

    product_category_translation {
        string product_category_name PK
        string product_category_name_english
    }

    customers ||--o{ orders : "1명이 여러 주문"
    orders ||--o{ order_items : "1주문에 여러 상품"
    orders ||--o{ order_payments : "1주문에 여러 결제"
    orders ||--o| order_reviews : "1주문에 1리뷰"
    products ||--o{ order_items : "1상품이 여러 주문에"
    sellers ||--o{ order_items : "1셀러가 여러 상품 판매"
    products }o--|| product_category_translation : "카테고리 번역"
    geolocation ||--o{ customers : "우편번호로 위치 연결"
    geolocation ||--o{ sellers : "우편번호로 위치 연결"
```

### 관계 읽는 법

| 기호 | 의미 | 예시 |
|------|------|------|
| `\|\|--o{` | 1 : N (일대다) | 고객 1명 → 주문 여러 개 |
| `\|\|--o\|` | 1 : 1 (일대일) | 주문 1개 → 리뷰 1개 |
| `}o--\|\|` | N : 1 (다대일) | 여러 상품 → 1개 카테고리 |
| PK | Primary Key | 그 테이블의 고유 식별자 |
| FK | Foreign Key | 다른 테이블을 참조하는 키 |

### 데이터 흐름 (고객 여정 순서)

```mermaid
flowchart LR
    subgraph 고객["👤 고객"]
        C[customers\n99,441건]
    end

    subgraph 주문["🛒 주문"]
        O[orders\n99,441건]
    end

    subgraph 상세["📦 주문 상세"]
        OI[order_items\n112,650건]
        OP[order_payments\n103,886건]
        OR[order_reviews\n99,224건]
    end

    subgraph 공급["🏪 공급"]
        P[products\n32,951건]
        S[sellers\n3,095건]
    end

    subgraph 참조["📍 참조"]
        G[geolocation\n1,000,163건]
        T[category_translation\n71건]
    end

    C -->|customer_id| O
    O -->|order_id| OI
    O -->|order_id| OP
    O -->|order_id| OR
    P -->|product_id| OI
    S -->|seller_id| OI
    G -.->|zip_code| C
    G -.->|zip_code| S
    T -.->|category_name| P

    style 고객 fill:#e8f4f8,stroke:#4a90e2,color:#000
    style 주문 fill:#e8f8e8,stroke:#28a745,color:#000
    style 상세 fill:#fff8e8,stroke:#f0a500,color:#000
    style 공급 fill:#f8e8f8,stroke:#9b59b6,color:#000
    style 참조 fill:#f0f0f0,stroke:#999,color:#000
```

---

## 3. Olist B2B 셀러 유치 데이터 ERD

> 셀러를 마케팅으로 모집하고, 영업을 통해 계약하는 흐름

```mermaid
erDiagram
    marketing_qualified_leads {
        string mql_id PK
        datetime first_contact_date
        string landing_page_id
        string origin
    }

    closed_deals {
        string mql_id FK
        string seller_id FK
        string sdr_id
        string sr_id
        datetime won_date
        string business_segment
        string lead_type
        string lead_behaviour_profile
        boolean has_company
        boolean has_gtin
        string average_stock
        string business_type
        float declared_product_catalog_size
        float declared_monthly_revenue
    }

    marketing_qualified_leads ||--o| closed_deals : "MQL이 계약으로 전환"
    closed_deals }o--|| sellers : "계약 셀러가 거래 시작"
```

### B2B 퍼널 흐름

```mermaid
flowchart LR
    MQL["📢 MQL\n마케팅 리드\n8,000건"]
    CD["🤝 Closed Deals\n계약 완료\n842건"]
    SEL["🏪 Sellers\n활성 셀러\n3,095건"]
    OI2["📦 Order Items\n실제 판매\n112,650건"]

    MQL -->|"전환율 10.5%"| CD
    CD -->|"seller_id 연결"| SEL
    SEL -->|"판매 시작"| OI2

    style MQL fill:#ffe8e8,stroke:#e74c3c,color:#000
    style CD fill:#fff8e8,stroke:#f0a500,color:#000
    style SEL fill:#f8e8f8,stroke:#9b59b6,color:#000
    style OI2 fill:#e8f8e8,stroke:#28a745,color:#000
```

---

## 4. Kaggle CRM/쿠폰 데이터 ERD

> 가구(household) 단위의 구매 행동, 쿠폰 사용, 캠페인 효과 분석용 데이터

```mermaid
erDiagram
    hh_demographic {
        int household_key PK
        string AGE_DESC
        string MARITAL_STATUS_CODE
        string INCOME_DESC
        string HOMEOWNER_DESC
        string HH_COMP_DESC
        string HOUSEHOLD_SIZE_DESC
        string KID_CATEGORY_DESC
    }

    transaction_data {
        int household_key FK
        int BASKET_ID
        int DAY
        int PRODUCT_ID FK
        int QUANTITY
        float SALES_VALUE
        int STORE_ID
        float RETAIL_DISC
        int TRANS_TIME
        int WEEK_NO
        float COUPON_DISC
        float COUPON_MATCH_DISC
    }

    product_kaggle {
        int PRODUCT_ID PK
        int MANUFACTURER
        string DEPARTMENT
        string BRAND
        string COMMODITY_DESC
        string SUB_COMMODITY_DESC
        string CURR_SIZE_OF_PRODUCT
    }

    campaign_desc {
        int CAMPAIGN PK
        string DESCRIPTION
        int START_DAY
        int END_DAY
    }

    campaign_table {
        int household_key FK
        int CAMPAIGN FK
        string DESCRIPTION
    }

    coupon {
        int COUPON_UPC PK
        int PRODUCT_ID FK
        int CAMPAIGN FK
    }

    coupon_redempt {
        int household_key FK
        int DAY
        int COUPON_UPC FK
        int CAMPAIGN FK
    }

    causal_data {
        int PRODUCT_ID FK
        int STORE_ID
        int WEEK_NO
        string display
        string mailer
    }

    hh_demographic ||--o{ transaction_data : "가구별 구매 내역"
    hh_demographic ||--o{ campaign_table : "가구별 캠페인 대상"
    hh_demographic ||--o{ coupon_redempt : "가구별 쿠폰 사용"
    product_kaggle ||--o{ transaction_data : "상품별 거래"
    product_kaggle ||--o{ coupon : "상품별 쿠폰"
    product_kaggle ||--o{ causal_data : "상품별 프로모션"
    campaign_desc ||--o{ campaign_table : "캠페인 정보"
    campaign_desc ||--o{ coupon : "캠페인별 쿠폰"
    coupon ||--o{ coupon_redempt : "쿠폰 사용 내역"
```

### Kaggle 데이터 흐름

```mermaid
flowchart LR
    subgraph 고객CRM["👥 고객(가구)"]
        HH[hh_demographic\n801가구]
    end

    subgraph 캠페인["📣 캠페인"]
        CD2[campaign_desc\n30개 캠페인]
        CT[campaign_table\n7,208건]
    end

    subgraph 쿠폰["🎫 쿠폰"]
        CP[coupon\n124,548건]
        CR[coupon_redempt\n2,318건]
    end

    subgraph 거래["💰 거래"]
        TX[transaction_data\n2,595,732건]
        CA[causal_data\n36,786,524건]
    end

    subgraph 상품CRM["📦 상품"]
        PK[product\n92,353건]
    end

    HH -->|household_key| CT
    HH -->|household_key| TX
    HH -->|household_key| CR
    CD2 -->|CAMPAIGN| CT
    CD2 -->|CAMPAIGN| CP
    CP -->|COUPON_UPC| CR
    PK -->|PRODUCT_ID| TX
    PK -->|PRODUCT_ID| CP
    PK -->|PRODUCT_ID| CA

    style 고객CRM fill:#e8f4f8,stroke:#4a90e2,color:#000
    style 캠페인 fill:#ffe8e8,stroke:#e74c3c,color:#000
    style 쿠폰 fill:#fff8e8,stroke:#f0a500,color:#000
    style 거래 fill:#e8f8e8,stroke:#28a745,color:#000
    style 상품CRM fill:#f8e8f8,stroke:#9b59b6,color:#000
```

---

## 5. 전체 데이터셋 요약표

### Olist B2C (거래) — 9개 테이블

| 테이블 | 건수 | PK | 주요 FK | 역할 |
|--------|-----:|-----|---------|------|
| **customers** | 99,441 | customer_id | zip_code_prefix | 고객 정보 |
| **orders** | 99,441 | order_id | customer_id | 주문 정보 (상태, 일시) |
| **order_items** | 112,650 | order_id + order_item_id | product_id, seller_id | 주문 내 개별 상품 |
| **order_payments** | 103,886 | order_id + payment_sequential | order_id | 결제 수단/금액 |
| **order_reviews** | 99,224 | review_id | order_id | 리뷰 점수/코멘트 |
| **products** | 32,951 | product_id | product_category_name | 상품 속성 |
| **sellers** | 3,095 | seller_id | zip_code_prefix | 셀러 위치 정보 |
| **geolocation** | 1,000,163 | zip_code_prefix | — | 우편번호별 위경도 |
| **category_translation** | 71 | product_category_name | — | 포르투갈어→영어 번역 |

### Olist B2B (셀러 유치) — 2개 테이블

| 테이블 | 건수 | PK | 주요 FK | 역할 |
|--------|-----:|-----|---------|------|
| **marketing_qualified_leads** | 8,000 | mql_id | — | 셀러 마케팅 리드 |
| **closed_deals** | 842 | mql_id | seller_id | 계약 완료 셀러 |

### Kaggle CRM/쿠폰 — 8개 테이블

| 테이블 | 건수 | PK | 주요 FK | 역할 |
|--------|-----:|-----|---------|------|
| **hh_demographic** | 801 | household_key | — | 가구 인구통계 |
| **transaction_data** | 2,595,732 | BASKET_ID + PRODUCT_ID | household_key, PRODUCT_ID | 구매 거래 내역 |
| **product** | 92,353 | PRODUCT_ID | — | 상품 마스터 |
| **campaign_desc** | 30 | CAMPAIGN | — | 캠페인 정의 |
| **campaign_table** | 7,208 | household_key + CAMPAIGN | household_key, CAMPAIGN | 캠페인 대상 가구 |
| **coupon** | 124,548 | COUPON_UPC | PRODUCT_ID, CAMPAIGN | 쿠폰-상품 매핑 |
| **coupon_redempt** | 2,318 | household_key + COUPON_UPC | household_key, COUPON_UPC | 쿠폰 사용 내역 |
| **causal_data** | 36,786,524 | PRODUCT_ID + STORE_ID + WEEK_NO | PRODUCT_ID | 매장 프로모션 데이터 |

---

## 6. 자주 쓰는 JOIN 경로

데이터 분석할 때 테이블을 연결하는 핵심 경로입니다.

### Olist B2C

```text
"고객별 구매 분석"
customers → orders → order_items → products
    (customer_id)  (order_id)   (product_id)

"셀러별 성과 분석"
sellers → order_items → orders → order_reviews
  (seller_id)    (order_id)    (order_id)

"지역별 분석"
geolocation → customers (또는 sellers)
    (zip_code_prefix)

"카테고리 영문 변환"
products → product_category_translation
    (product_category_name)
```

### Olist B2B → B2C 연결

```text
"셀러 유치 → 실제 판매 연결"
marketing_qualified_leads → closed_deals → sellers → order_items
         (mql_id)            (seller_id)    (seller_id)
```

### Kaggle CRM

```text
"가구별 쿠폰 효과 분석"
hh_demographic → coupon_redempt → coupon → campaign_desc
  (household_key)   (COUPON_UPC)   (CAMPAIGN)

"가구별 구매 패턴"
hh_demographic → transaction_data → product
  (household_key)    (PRODUCT_ID)
```
