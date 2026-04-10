# Git & GitHub 팀 협업 가이드

## 목차
1. [전체 프로세스 요약](#1-전체-프로세스-요약)
2. [최초 1회 설정](#2-최초-1회-설정-팀원-전원)
3. [일상 작업 흐름](#3-일상-작업-흐름-매일-반복)
4. [주의사항](#4-주의사항)
5. [자주 쓰는 명령어 모음](#5-자주-쓰는-명령어-모음)
6. [문제 상황별 해결법](#6-문제-상황별-해결법)

---

## 1. 전체 프로세스 요약

```
[내 PC에서 작업] → [저장(commit)] → [업로드(push)] → [GitHub] ← [다운로드(pull)] ← [팀원 PC]
```

### 폴더 구조 (각자 담당 폴더에서만 작업)
```
team/
├── cx/            ← CX 담당자
├── logistics/     ← 물류 담당자
├── marketing/     ← 마케팅 담당자
├── merchandising/ ← MD 담당자
├── product/       ← 상품 담당자
└── seller_ops/    ← 셀러운영 담당자
```

### 핵심 규칙
> **자기 폴더에서만 작업하고, 작업 전에 항상 pull 먼저!**

---

## 2. 최초 1회 설정 (팀원 전원)

### Step 1: Git 설치 확인
```bash
git --version
```
버전이 나오면 OK. 안 나오면 https://git-scm.com 에서 설치

### Step 2: 사용자 정보 등록
```bash
git config --global user.name "본인이름"
git config --global user.email "본인깃헙이메일@example.com"
```

### Step 3: 저장소 복제 (clone)
작업할 폴더 위치에서:
```bash
git clone https://github.com/ajh8156/project-2.git
```
→ `project-2` 폴더가 생성됨

### Step 4: 작업 폴더로 이동
```bash
cd project-2
```

### Step 5: Collaborator 초대 (저장소 소유자만)
1. GitHub → `project-2` 저장소 → **Settings**
2. 왼쪽 메뉴 **Collaborators** 클릭
3. **Add people** → 팀원 GitHub 아이디 또는 이메일 입력
4. 팀원은 이메일로 온 초대를 **Accept** 해야 push 가능

---

## 3. 일상 작업 흐름 (매일 반복)

### 전체 흐름도

```
① pull (최신화)
    ↓
② 내 폴더에서 작업
    ↓
③ add (변경 파일 선택)
    ↓
④ commit (저장 + 메시지)
    ↓
⑤ pull (혹시 모를 변경 확인)
    ↓
⑥ push (업로드)
```

### ① 최신 상태 가져오기 (pull)
```bash
git pull origin main
```
> 작업 시작 전에 **반드시** 실행! 팀원이 올린 최신 내용을 받아옵니다.

### ② 내 담당 폴더에서 작업
- 자기 폴더 안의 파일만 수정/추가
- 예: `team/marketing/` 담당자는 이 폴더에서만 작업

### ③ 변경된 파일 확인 및 선택 (add)
```bash
# 변경 내용 확인
git status

# 내 폴더 파일만 선택 (예: marketing 담당자)
git add team/marketing/
```

### ④ 변경 내용 저장 (commit)
```bash
git commit -m "marketing: 4월 프로모션 분석 추가"
```

> 커밋 메시지 작성 규칙:
> - `담당폴더: 작업내용` 형식 권장
> - 예: `cx: 고객여정 지도 초안 작성`
> - 예: `logistics: 배송 데이터 분석 수정`

### ⑤ push 전 한번 더 pull
```bash
git pull origin main
```

### ⑥ GitHub에 업로드 (push)
```bash
git push origin main
```

---

## 4. 주의사항

### 반드시 지켜야 할 것

| 규칙 | 이유 |
|------|------|
| **작업 전 pull 먼저** | 안 하면 충돌(conflict) 발생 |
| **자기 폴더에서만 작업** | 다른 사람 파일 건드리면 충돌 |
| **commit 메시지 명확하게** | 누가 뭘 했는지 추적 가능 |
| **큰 파일(100MB+) 올리지 않기** | GitHub 용량 제한 |
| **.env, 비밀번호 파일 올리지 않기** | 보안 위험 |

### 절대 하지 말 것

- `git push --force` → 다른 사람 작업이 사라질 수 있음
- 다른 사람 폴더 파일 수정 → 반드시 해당 담당자에게 말하고 진행
- commit 없이 pull → 내 작업이 날아갈 수 있음 (먼저 commit 후 pull)

---

## 5. 자주 쓰는 명령어 모음

```bash
# 상태 확인
git status                    # 변경된 파일 목록
git log --oneline -5          # 최근 커밋 5개 보기
git diff                      # 변경 내용 상세 보기

# 기본 작업
git pull origin main          # 최신화
git add team/내폴더/          # 파일 선택
git commit -m "메시지"         # 저장
git push origin main          # 업로드

# 실수했을 때
git checkout -- 파일명         # 수정 전으로 되돌리기 (commit 전)
git log --oneline             # 커밋 이력 확인
```

---

## 6. 문제 상황별 해결법

### 상황 1: push가 거부됨 (rejected)
```
! [rejected] main -> main (fetch first)
```
**원인**: 팀원이 먼저 push 해서 내 로컬이 뒤처짐
**해결**:
```bash
git pull origin main
# 충돌이 없으면 자동 병합됨
git push origin main
```

### 상황 2: 충돌 발생 (conflict)
```
CONFLICT (content): Merge conflict in team/marketing/marketing.md
```
**원인**: 같은 파일을 두 사람이 동시에 수정
**해결**:
1. 충돌 파일 열기
2. `<<<<<<<` 와 `>>>>>>>` 사이에서 원하는 내용 선택
3. 표시 기호 삭제 후 저장
```bash
git add 충돌파일
git commit -m "marketing: 충돌 해결"
git push origin main
```

### 상황 3: 실수로 다른 폴더 파일을 수정함
```bash
# commit 전이라면
git checkout -- team/다른폴더/파일명

# 이미 commit 했다면 담당자에게 알리기
```

### 상황 4: git clone 후 push 권한이 없음
```
remote: Permission to ajh8156/project-2.git denied
```
**원인**: Collaborator 초대를 받지 않았거나 수락하지 않음
**해결**: 저장소 소유자(ajh8156)에게 초대 요청 → 이메일에서 수락

---

## Quick Reference Card (출력용)

```
┌─────────────────────────────────────┐
│     Git 작업 순서 (매일 반복)         │
│                                     │
│  1. git pull origin main   ← 최신화  │
│  2. 내 폴더에서 파일 작업             │
│  3. git status             ← 확인    │
│  4. git add team/내폴더/   ← 선택    │
│  5. git commit -m "메시지"  ← 저장   │
│  6. git pull origin main   ← 재확인  │
│  7. git push origin main   ← 업로드  │
└─────────────────────────────────────┘
```
