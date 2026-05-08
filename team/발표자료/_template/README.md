# Olist 발표 — 디자인 토큰 + HTML 입타

> 작성일: 2026-05-08
> 출처: [team/디자인시스템/olist-design-system-sample_260508.pdf](../../디자인시스템/olist-design-system-sample_260508.pdf) (단순 톤 샘플)
> 목적: 클로드에서 만드는 모든 슬라이드 이미지(슬2 이메일 / 슬4 100명 그리드 / 슬6 RFM / 슬9 5점 편향 / 색상 교체 산출물 7장)의 **공통 베이스**

## 폴더 안 파일

| 파일 | 용도 |
|---|---|
| [`tokens.css`](tokens.css) | 디자인 토큰 SSOT (컬러·폰트·여백·캔버스 모든 값) |
| [`template.html`](template.html) | 빈 슬라이드 입타 (헤더·푸터·콘텐츠 영역 골격) |
| [`export.js`](export.js) | Playwright PNG export (1920×1080 @2x Retina) |

## 추출된 디자인 토큰 요약

| 항목 | 값 | 비고 |
|---|---|---|
| 메인 블루 | `#1A3DF0` | OLIST 로고·강조·풀블리드 디바이더 |
| 옅은 라벤더 | `#EBEEFF` | RESOLUTION 카드 배경 |
| 본문 검정 | `#0B0F19` | 거의 검정 |
| 차콜 회색 | `#6B7280` | 부제·캡션 |
| 옅은 회색 | `#9CA3AF` | 푸터·비활성 네비 |
| 비활성 카드 | `#F3F4F6` | OUR APPROACH 01~04 |
| 보더 | `#E5E7EB` | 카드 보더 |
| 캔버스 | 1920×1080 | 16:9 |
| 좌우 여백 | 80px | |
| 상단 여백 | 50px | |
| 폰트 (한글) | Pretendard | |
| 폰트 (영문) | Inter | |
| 거대 디스플레이 | 240px / 800 | OLIST·6.42% |
| 섹션 디바이더 | 120~160px / 800 | BLIEVED COMMON·02. |
| H1 | 64px / 800 | 슬라이드 헤딩 |
| H2 | 40px / 800 | 카드 헤딩 |
| H3 | 28px / 600 | 서브 |
| Body | 18px / 400 | |
| Caption | 14px / 600 + 자간 0.12em | DATA SOURCE 등 |
| 카드 모서리 | 0px (직각) | |

## 사용 흐름

### 1) 새 슬라이드 이미지 만들기

```bash
# template.html 복사해서 새 파일 생성
cp template.html ../slides/slide-02-email.html

# 콘텐츠 갈아끼우고 (헤더 .active 위치 + 본문 + 푸터 페이지 번호)
# 브라우저로 열어 확인 후 export
node export.js ../slides/slide-02-email.html ../exports/slide-02-email.png
```

### 2) PPT에 삽입

- PPT의 빈 슬라이드 = 16:9
- 삽입 → 그림 → `exports/slide-XX.png` 선택
- `Ctrl + Shift + 드래그`로 슬라이드 전체 채우기 (비율 유지)
- 결과: PPT 마스터 직제작 슬라이드와 시각적 차이 없음 (해상도 @2x 덕분)

## 일관성 체크리스트 (이미지 export 전 확인)

- [ ] 헤더 olist 로고 + 4섹션 네비 위치/색
- [ ] 푸터 좌측 "NEVER—ENDING · OLIST 재구매 전략" / 우측 "2026 · NN"
- [ ] 페이지 번호(NN) 슬# 일치
- [ ] 헤더 네비 `.active` 클래스가 현재 Act에 맞음
  - Act 1·2 = DIAGNOSE
  - Act 3·3.5·4 = BOTTLENECK
  - Act 5·6 = SOLUTION
  - Act 7·8·9 = OUTCOME
- [ ] 색상은 `tokens.css` 변수만 사용 (직접 HEX 입력 금지)
- [ ] 폰트는 Pretendard(한글)·Inter(영문)
- [ ] 모서리는 `--radius-card: 0` (직각)
- [ ] 그림자 안 씀

## 다음 작업 (우선순위)

| # | 작업 | 출력 |
|---|---|---|
| 1 | 슬2 이메일 카드 | `slides/slide-02-email.html` → `exports/slide-02-email.png` |
| 2 | 슬4 100명 그리드 | `slides/slide-04-grid.html` → `exports/slide-04-grid.png` |
| 3 | 슬6 RFM 4분면 | Python matplotlib (별도) → `exports/slide-06-rfm.png` |
| 4 | 슬9 5점 편향 시각 | `slides/slide-09-peak.html` → `exports/slide-09-peak.png` |
| 5 | CX SLA 재제작 | `slides/asset-cx-sla.html` → `tf2-cx-sla-90percent.png` (덮어쓰기) |
| 6 | 셀러 다각화 재제작 | `slides/asset-seller-diversification.html` → `tf3-seller-diversification.png` |
| 7 | BF 코호트 추적 재제작 | `slides/asset-bf-cohort.html` → `tf3-bf-cohort-tracking.png` |
| 8 | 번들 3장 재제작 | `slides/asset-bundle-*.html` → `bundle_*.png` |
| 9 | 분석 차트 3장 (Python 재export) | matplotlib + tokens.css 컬러 → `tf2-data-*.png` |

## 관련 문서

- [../슬라이드_구성안_v3.md](../슬라이드_구성안_v3.md) — 스토리 SSOT
- [../PPT_제작시트_v1.md](../PPT_제작시트_v1.md) — 슬라이드별 콘텐츠 SSOT
- [../슬라이드_산출물_매칭표_v1.md](../슬라이드_산출물_매칭표_v1.md) — 산출물 매핑
