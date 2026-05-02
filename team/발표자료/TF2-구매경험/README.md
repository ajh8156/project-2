# TF2 구매 경험 — 발표 산출물 폴더

> 담당: **Product/UX 리드** · 참여 Logistics · CX · Seller Ops
> 공동 KR: 첫 구매 저평점 비중 **12.82% → 10.5%**
> 발표 시간: **1분** (15초 × 산출물 4종)
> SSOT: `team/doc/산출물/TF2_산출물_구상안_v1.md`

최종 수정일: 2026-05-02

### 수정 내역

| 날짜 | 내용 |
|------|------|
| 2026-05-02 | 폴더 정리 v1 — Thank-you 시안 7장 + CX 분석 자료 3장 + 설득 포인트 문서 추가, 워크플로우 §0-2 네이밍 적용, 이미지는 `assets/` 하위로 분리 |

---

## 📁 폴더 안 파일 한눈에

> 모든 이미지 산출물은 `assets/` 하위에 보관. 폴더 루트는 텍스트 문서(README · talking-points)만.

### 산출물 ③ Thank-you 페이지 — 5시안 + 콜아웃 2장 (Pencil 완성 ✅)

| 파일 (`assets/` 하위) | 시안 | 시점 · 채널 | 비고 |
|---|---|---|---|
| `assets/tf2-thankyou-before.png` | ① Before | D+0 In-page (결핍) | 변수 통제 |
| **`assets/tf2-thankyou-after.png` ★** | ② After 메인 | D+0 In-page (7블록 트리거) | TF3 핸드오프 시각 정점 |
| `assets/tf2-thankyou-push-d7.png` | ③ Push | D+7 iOS 잠금화면 | 리뷰 요청 + 5% 쿠폰 |
| `assets/tf2-thankyou-email-d30.png` | ④ Email | D+30 Gmail | 쿠폰 + 침구 크로스셀 |
| `assets/tf2-thankyou-kakao-d60.png` | ⑤ Kakao | D+60 카카오 플친 | Buy Again 시크릿 혜택 |
| `assets/tf2-thankyou-callout-before.png` | 콜아웃 | Before 결핍 4종 | 외부 어노테이션 |
| `assets/tf2-thankyou-callout-after.png` | 콜아웃 | After TF3 핸드오프 | 외부 어노테이션 |

### 분석 데이터 — 발표 데이터 근거 3장

| 파일 (`assets/` 하위) | 내용 | 발표 활용 |
|---|---|---|
| `assets/tf2-data-rating-by-category.png` | 카테고리별 리뷰 점수 분포 | 카테고리별 위험도 차이 시각 |
| `assets/tf2-data-low-rating-by-category.png` | 카테고리별 저평점 빈도 | KR 12.82%→10.5% 핵심 타겟 |
| `assets/tf2-data-avg-vs-low-pct.png` | 평균 점수 vs 저평점 비중 | TF2 개입 ROI 산점도 |

> 추가 정성 자료(워드클라우드 등) 필요 시: `team/cx/images/cx_03_*` ~ `cx_05_*`

### 문서

- [`tf2-talking-points.md`](tf2-talking-points.md) — 설득 포인트 5개 + 1분 멘트 + Q&A 대비

---

## 📋 TF2 산출물 4종 진행 상태

| # | 산출물 | 상태 | 본 폴더 위치 |
|---|---|---|---|
| ① | **PDP Before/After** (호텔식 베개·G마켓 톤) | 📝 컨셉 완료 / 시안 PNG 미export ⚠️ | (제작 진행 중) |
| ② | **CX 48h SLA + 프로세스 카드** | 📝 컨셉만 | (Figma/Pencil 작업 필요) |
| ③ | **Thank-you 페이지 + 4채널 목업** | ✅ Pencil 시안 5+2장 완성 | `assets/tf2-thankyou-*.png` |
| ④ | **블프 프로모션 랜딩 5단** | 📝 컨셉만 | (Figma/Pencil 작업 필요) |

> ⚠️ **PDP 시안 export 필요**: 산출물 ① 컨셉·카피는 SSOT 문서에 정의 완료(`TF2_산출물_구상안_v1.md` §1)되었으나, 폴더에는 시안 부품(thumb / seller_avatar / pillow_after_main)만 있고 본 시안 5장(pdp_before_main, pdp_after_main 등)이 아직 export되지 않음. **5/5까지 export 완료 필요**.

---

## 🎯 네이밍 규칙 (워크플로우 §0-2 적용)

```
tf2-{유형}-{설명}.{ext}
```

| prefix | 용도 |
|---|---|
| `tf2-pdp-*` | 산출물 ① PDP 시안 |
| `tf2-cx-*` | 산출물 ② CX 48h SLA |
| `tf2-thankyou-*` | 산출물 ③ Thank-you (현재 7장) |
| `tf2-bf-*` | 산출물 ④ 블프 랜딩 |
| `tf2-data-*` | 발표 데이터 근거 (분석 자료) |

**원칙**:
- 모든 경로는 프로젝트 루트 기준 **상대경로**만 사용 (절대 경로 금지)
- 슬라이드 번호는 사용 X — 파트명만으로 식별
- 새 시안 추가 시 본 README의 표에 한 줄 추가

---

## 🔗 관련 문서

- `team/doc/산출물/TF2_산출물_구상안_v1.md` — 산출물 SSOT (컨셉·카피·발표 멘트)
- `team/doc/산출물/TF2_md.md` — 산출물 2~4 상세 실행 방안
- `team/발표자료/슬라이드_구성안_v2.md` §4-7 — 발표 슬라이드 SSOT
- `team/발표자료/claude-code-pptx-hybrid-workflow.md` §0 — 우리 프로젝트 적용 가이드 (네이밍·디자인 시스템)
- `team/cx/cx.md` §5, §7 — 분석 데이터 원본 + UX 개선안
