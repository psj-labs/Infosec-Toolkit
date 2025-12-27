## DIRB

**DIRB는 웹 서버에 존재할 가능성이 있는 디렉토리와 파일을 사전(Dictionary) 기반으로 탐색하는 웹 정찰(Enumeration) 도구입니다.**

- 웹 서버에 실제로 존재하지만
- 메뉴, 링크, UI에는 노출되지 않은
- 숨겨진 경로 및 파일을 자동으로 탐색합니다.

---

## DIRB 공격 개념

웹 서버에는 다음과 같은 경로들이 남아 있는 경우가 많습니다.

- /admin
- /backup
- /uploads
- /test
- /old
- /config

**DIRB는 이러한 경로를 **워드리스트 기반으로 무차별 대입 요청**하여 HTTP 응답 코드로 존재 여부를 판단합니다.**

- 접근 제한이 없다면 **정보 노출 및 후속 공격으로 이어질 수 있습니다.

---


## 주의
- 실제 서비스나 타인의 서버에 사용하면 불법입니다.
- 반드시 **본인 소유 서버 또는 실습 환경**에서만 사용합니다.

---

## 기본 사용법
```text
dirb http://target.com
```
- 기본 워드리스트 사용
```text
/usr/share/dirb/wordlists/common.txt
```
- GET 요청 기반 디렉토리 및 파일 탐색 수행

---

## 옵션 사용법

###  워드리스트 지정
```text
dirb http://target.com /usr/share/dirb/wordlists/big.txt
```
- 더 많은 경로 후보 시도
- 탐색 시간 증가
- 발견 확률 증가

---

### 파일 확장자 지정 (-X)
```text
dirb http://target.com -X .php,.bak,.old,.txt
```
- 특정 확장자를 가진 파일 탐색
- 백업 파일, 소스 파일 노출 여부 확인에 유용

---

### False Positive 제거 (-f)
```text
dirb http://target.com -f
```
- 존재하지 않는 경로에도 200을 반환하는 서버 대응
- 실제 존재하는 경로만 필터링

---

### User-Agent 변경
```text
dirb http://target.com -a "Mozilla/5.0"
```
- 기본 User-Agent 차단 우회
- 단순한 보안 필터 회피 목적

---

## 결과 출력 예시
```text
+ http://target.com/admin (CODE:200|SIZE:1234)  
+ http://target.com/uploads (CODE:301)
```
---

## 결과 해석

`CODE:200` : 실제 페이지 존재  
`CODE:301` : 디렉토리 존재 (리다이렉션)  
`CODE:403` : 접근 제한 존재  
`SIZE`     : 응답 크기 비교 기준  

- `CODE 200 / 301` 응답은 **직접 접속하여 반드시 확인**

---

## DIRB로 발견 가능한 취약점

- 관리자 페이지 노출
- 업로드 디렉토리 접근 가능
- 백업 파일 다운로드 가능
- 테스트 파일 접근 가능
- 설정 파일 노출 

## 디렉토리 및 파일 노출 예방법
- 불필요한 디렉토리 제거
- 접근 제어 (403)
- 디렉토리 리스팅 비활성화
- 백업 파일 외부 노출 방지
