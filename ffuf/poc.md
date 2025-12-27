## FFUF

- **FFUF는 웹 서버에 존재할 가능성이 있는 디렉토리, 파일, 파라미터 등을 워드리스트 기반으로 매우 빠르게 탐색하는 웹 정찰(Enumeration) 도구입니다.**

- 웹 서버에 실제로 존재하지만  
- 메뉴, 링크, UI에는 노출되지 않은  
- 숨겨진 경로, 파일, 파라미터를 자동으로 탐색합니다.

---

## FFUF 공격 개념

### 웹 서버에는 다음과 같은 요소들이 남아 있는 경우가 많습니다.

- 디렉토리: `/admin`, `/backup`, `/uploads`
- 파일: `backup.zip, test.php`
- 파라미터: `?id=, ?page=`
- API 엔드포인트: `/api`, `/v1/users`

### FFUF는 요청 URL 또는 파라미터 위치에 `FUZZ` 키워드를 두고 워드리스트 값을 대입하여 HTTP 요청을 반복 전송하고, 응답 코드, 크기, 내용 차이를 기준으로 존재 여부를 판단합니다.

- 접근 제한이 없다면 **정보 노출 및 후속 공격으로 이어질 수 있습니다.**

---

## 주의

- 실제 서비스나 타인의 서버에 사용하면 불법입니다.  
- 반드시 **본인 소유 서버 또는 실습 환경**에서만 사용합니다.

---

## 기본 사용법
- 다음은 필자의 개인 DVWA주소에 ffuf를 시도해보았으며 명령어는 다음과 같습니다.
```text
ffuf -u http://192.168.64.20/DVWA/FUZZ -w /usr/share/wordlists/dirb/common.txt
```

![ffuf](/ffuf/imgs/ffuf.png)

- ffuf의 기본 사용 명령어 형태는 다음과 같습니다.
```text
ffuf -u http://target.com/FUZZ -w /usr/share/wordlists/dirb/common.txt
```
- `FUZZ` 위치에 워드리스트 값이 하나씩 대입됨  
- GET 요청 기반 디렉토리 및 파일 탐색 수행

---

## 옵션 사용법

### 워드리스트 지정
```text
ffuf -u http://target.com/FUZZ -w /usr/share/wordlists/dirb/big.txt
```
- 더 많은 경로 후보 시도  
- 탐색 시간 증가  
- 발견 확률 증가  

---

### 파일 확장자 지정 (-e)
```text
ffuf -u http://target.com/FUZZ -w wordlist.txt -e .php,.bak,.old,.txt
```
- 특정 확장자를 가진 파일 탐색  
- 백업 파일, 소스 파일 노출 여부 확인에 유용  

---

### 상태 코드 필터링 (-mc)
```text
ffuf -u http://target.com/FUZZ -w wordlist.txt -mc 200,301
```
- 특정 HTTP 상태 코드만 출력  
- 불필요한 결과 제거  

---

### 응답 크기 필터링 (-fs)
```text
ffuf -u http://target.com/FUZZ -w wordlist.txt -fs 1234
```
- 동일한 크기의 응답 제거  
- False Positive 감소  

---

### User-Agent 변경
```text
ffuf -u http://target.com/FUZZ -w wordlist.txt -H "User-Agent: Mozilla/5.0"
```
- 기본 User-Agent 차단 우회  
- 단순한 보안 필터 회피 목적  

---

## 결과 출력 예시
```text
/admin            [Status: 200, Size: 1234]  
/uploads          [Status: 301, Size: 0]  
```
---

## 결과 해석

- `Status 200` : 실제 페이지 또는 파일 존재  
- `Status 301` : 디렉토리 존재 (리다이렉션)  
- `Status 403` : 접근 제한 존재  
- `Size`       : 응답 크기 비교 기준  

- Status 200 / 301 결과는 **직접 접속하여 반드시 확인**

---

## FFUF로 발견 가능한 취약점

- 관리자 페이지 노출  
- 업로드 디렉토리 접근 가능  
- 백업 파일 다운로드 가능  
- 테스트 파일 접근 가능  
- 파라미터 기반 취약점(SQLi, XSS) 탐색 가능  

---

## 디렉토리 및 파일 노출 예방법

- 불필요한 디렉토리 제거  
- 접근 제어 설정 (403)  
- 디렉토리 리스팅 비활성화  
- 백업 파일 외부 노출 방지  

---

## dirb와 ffuf 차이
```text
dirb: 사전 기반으로 웹 서버의 숨겨진 디렉토리, 파일 경로를 탐색하는 전통적인 웹 정찰 도구
ffuf: fuzz 포인트에 워드리스트를 주입해 경로, 파일, 파라미터까지 고속으로 탐색하는 범용 웹 퍼징 도구
```

| 구분 | DIRB | FFUF |
|:---:|:---|:---|
| 도구 성격 | 디렉토리 브루트포싱 특화 | 범용 퍼징(Fuzzing) 도구 |
| 탐색 대상 | 디렉토리, 파일 | 디렉토리, 파일, 파라미터, API |
| 탐색 방식 | 고정 URL에 사전 대입 | `FUZZ` 위치에 자유롭게 대입 |
| 속도 | 느림 | 매우 빠름 |
| 커스터마이징 | 제한적 | 매우 자유로움 |
| 파라미터 퍼징 | 불가능 | 가능 |
| 응답 필터링 | 제한적 | 상태코드·크기·문자열 등 정밀 |
| 실무 사용성 | 낮아지는 추세 | 실무 표준 수준 |
| 학습 난이도 | 낮음 (입문용) | 중간 (정찰 이해 필요) |
| 주 용도 | 기초 디렉토리 탐색 | 정밀 정찰·취약점 탐색 전 단계 |
