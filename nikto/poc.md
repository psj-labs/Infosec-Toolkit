# nikto

- Nikto는 웹 서버를 대상으로 취약한 설정, 알려진 취약점, 위험한 파일 및 경로를 자동으로 점검하는 웹 취약점 스캐너입니다.
- 포트 스캔 도구가 아니라 HTTP/HTTPS 웹 서비스 자체를 분석하는 도구입니다.

---

## 기본 스캔

- Nikto의 기본적인 스캔 문법은 다음과 같습니다.
```text
nikto -h [IP or URL]
```
- 필자는 scanme.nmap.org의 IP주소인 `45.33.32.156`을 대상으로 스캔을 수행하였고 사용한 명령어는 다음과 같습니다.
```text
nikto -h 45.33.32.156
```
- 잠시 기다리면 웹 서버의 배너 정보, 취약한 설정, 위험한 파일 및 경로들이 출력됩니다.

![01](/nikto/imgs/01.png)

---

# Nikto 스캔 결과 요약

- **대상 IP:** 45.33.32.156  
- **대상 포트:** 80 (HTTP)  
- **웹 서버:** Apache/2.4.7 (Ubuntu)  
- **스캔 시간:** 약 410초  

---

## 결과

- `X-Frame-Options` 헤더가 설정되어 있지 않음  
  -> 클릭재킹(Clickjacking) 공격에 취약할 가능성 있음

- `X-Content-Type-Options` 헤더가 설정되어 있지 않음  
  -> MIME 타입 스니핑 공격 가능성 있음

- CGI 디렉터리는 발견되지 않음

- Apache 버전이 **구버전(Apache 2.4.7)** 으로 확인됨  
  -> 알려진 취약점 존재 가능성 있음

- `index` 관련 비정상(비표준) 헤더(`tcn`)가 발견됨  
  -> Apache mod_negotiation 활성화 상태

- `index` 파일에 대해 여러 대체 파일 존재  
  -> 파일 이름 브루트포싱 공격에 노출될 가능성 있음

- 허용된 HTTP 메서드 확인됨  
  -> `GET`, `HEAD`, `POST`, `OPTIONS`

---


## Nikto 스캔 동작 원리

- Nikto는 웹 서버에 다양한 경로와 파라미터를 포함한 HTTP 요청을 반복적으로 전송합니다.
- 서버의 응답 코드, 헤더, 페이지 내용을 분석하여 내부 취약점 데이터베이스와 비교합니다.

### 동작 흐름 요약

1. Nikto 실행  
2. 다수의 HTTP 요청 전송  
3. 서버 응답 수신  
4. 취약점 패턴 DB와 비교  
5. 취약 가능 항목 출력

---

## HTTPS 스캔

- HTTPS 웹 서버를 대상으로 스캔할 경우 -ssl 옵션을 사용합니다.
```text
nikto -h https://target.com -ssl
```
---

## 포트 지정 스캔

- 웹 서비스가 기본 포트(80, 443)가 아닌 경우 포트를 직접 지정합니다.
```text
nikto -h http://target.com -p 8080
```
---

## 출력 파일 저장

- 스캔 결과를 파일로 저장할 수 있습니다.
```text
nikto -h http://target.com -o result.txt
```
- HTML 형식으로 저장할 경우 다음과 같이 실행합니다.
```text
nikto -h http://target.com -o result.html -Format html
```
---

## 옵션 정리

| 옵션 | 이름 | 설명 | 특징 |
| --- | --- | --- | --- |
| -h | Host | 대상 URL 또는 IP 지정 | 필수 옵션 |
| -p | Port | 웹 서비스 포트 지정 | 비표준 포트 |
| -ssl | SSL | HTTPS 강제 사용 | HTTPS 스캔 |
| -Tuning | Tuning | 특정 테스트만 수행 | 정밀 분석 |
| -o | Output | 결과 파일 저장 | 리포트 생성 |
| -Format | Format | 출력 포맷 지정 | txt / html |
| -Display | Display | 출력 형식 제어 | 가독성 조절 |

---

## Tuning 옵션

- Tuning 옵션을 사용하여 특정 유형의 테스트만 수행할 수 있습니다.
```text
nikto -h http://target.com -Tuning x
```
| 값 | 의미 |
| --- | --- |
| 1 | 파일 업로드 관련 취약점 |
| 2 | 잘못된 서버 설정 |
| 3 | 정보 노출 |
| 4 | 인증 관련 취약점 |
| x | 모든 테스트 |

---

## 권장 명령어 예시
```text
nikto -h http://target.com -p 80,443 -ssl -Tuning x -o nikto_result.html -Format html
```
-> HTTPS 웹 서비스를 대상으로 모든 테스트를 수행하고 결과를 HTML 리포트로 저장

---

## 주의사항

- Nikto는 매우 공격적인 요청을 다수 전송하므로 IDS/IPS에 쉽게 탐지
- 결과에 False Positive가 포함될 수 있으므로 반드시 수동 검증이 필요
- 허가 없는 사이트를 스캔을 수행하는 것은 불법
