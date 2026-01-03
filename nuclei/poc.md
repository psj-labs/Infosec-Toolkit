# nuclei

- nuclei는 웹 서버 및 웹 애플리케이션을 대상으로 미리 정의된 템플릿을 기반으로 실제 HTTP/HTTPS 요청을 전송하여 취약점을 자동으로 검증하는 웹 취약점 스캐너입니다.
- 웹 서비스 자체의 설정 오류, 정보 노출, 알려진 취약점(cve)을 탐지하는 도구입니다.

---

## 기본 스캔

- nuclei의 기본적인 스캔 문법은 다음과 같습니다.

```text
/root/go/bin/nuclei -u [URL]
```
- 필자는 합법적 스캔이 가능한 `testphp.vulnweb.com` 사이트를 대상으로 스캔을 수행하였으며 사용한 명령어는 다음과 같습니다.

```text
/root/go/bin/nuclei -u http://testphp.vulnweb.com
```
- 잠시 기다리면 웹 서버를 대상으로 템플릿 기반 요청이 전송되며, 의심되는 취약점들이 출력됩니다.

![01](/nuclei/imgs/01.png)

---

# nuclei 스캔 결과 요약

- 대상 URL: http://testphp.vulnweb.com  
- 스캔 방식: HTTP 기반 템플릿 자동 검증  
- 사용 템플릿 수: 약 9,000여 개  
- 스캔 시간: 약 수 분  

---

## 결과

#### 여러개의 결과 중 3가지만 살펴보겠습니다.

- `idea-folder-exposure` 발견  
  -> 개발용 IDE 설정 파일(.idea/workspace.xml) 외부 노출

- `Content-Security-Policy` 헤더 누락  
  -> `XSS 공격` 발생 시 브라우저 단 차단 불가

- `Strict-Transport-Security` 헤더 누락  
  -> HTTPS 미적용으로 중간자 공격 위험 존재

---

## 주요 취약점 상세

### `idea-folder-exposure` (개발용 IDE 설정 파일 노출)

- 해당 URL: http://testphp.vulnweb.com/.idea/workspace.xml

- 개발자가 사용하는 IDE 설정 파일이 웹 루트에 남아 외부에서 접근 가능한 상태
- 프로젝트 구조, 경로 정보 등이 노출되어 정찰 단계에서 공격자에게 유리한 정보 제공

---

### `http-missing-security-headers:content-security-policy` (CSP 누락)

- 브라우저가 허용할 스크립트 및 리소스 출처를 제한하지 못함
- XSS 공격 발생 시 피해 확산을 제어할 수 있는 브라우저 보안 장치 부재

---

### `http-missing-security-headers:strict-transport-security` (HSTS 누락)  

- HTTPS 사용이 강제되지 않아 최초 접속 시 HTTP 다운그레이드 가능
- 공용 네트워크 환경에서 트래픽 탈취 및 변조 위험 증가

---

## nuclei 스캔 동작 원리

- nuclei는 사전에 정의된 YAML 템플릿을 기반으로 HTTP 요청을 생성합니다.
- 서버의 응답 코드, 헤더, 본문을 조건과 비교하여 취약점 여부를 판단합니다.

### 동작 흐름 요약

1. nuclei 실행  
2. 템플릿 로드  
3. HTTP/HTTPS 요청 전송  
4. 서버 응답 분석  
5. 조건 일치 시 취약점 출력  

---

## 진행 상태 확인

- 스캔 진행 상황을 실시간으로 확인하려면 `-stats` 옵션을 사용합니다.

```text
/root/go/bin/nuclei -u http://testphp.vulnweb.com -stats
```
![02](/nuclei/imgs/02.png)

---

## 출력 파일 저장

- 스캔 결과를 파일로 저장할 수 있습니다.

```text
/root/go/bin/nuclei -u http://target.com -o result.txt
```
- JSON 형식으로 저장할 경우 다음과 같이 실행합니다.

```text
/root/go/bin/nuclei -u http://target.com -json -o result.json
```
---

## 옵션 정리

| 옵션 | 이름 | 설명 | 특징 |
| --- | --- | --- | --- |
| -u | URL | 단일 대상 URL 지정 | 기본 스캔 |
| -l | List | URL 목록 파일 입력 | 다중 대상 |
| -t | Template | 템플릿 또는 디렉터리 지정 | 범위 제어 |
| -severity | Severity | 취약점 심각도 필터 | 노이즈 감소 |
| -tags | Tags | 특정 태그 템플릿만 실행 | 목적 스캔 |
| -rate-limit | Rate Limit | 초당 요청 수 제한 | 차단 방지 |
| -c | Concurrency | 동시 실행 수 지정 | 속도 조절 |
| -o | Output | 결과 파일 저장 | 리포트 생성 |
| -json | JSON | JSON 형식 출력 | 자동화 |
| -jsonl | JSONL | JSON Line 출력 | 로그 수집 |
| -silent | Silent | 출력 최소화 | 스크립트용 |

---

## 권장 명령어 예시

```text
/root/go/bin/nuclei -u http://testphp.vulnweb.com -severity medium,high,critical -rate-limit 100 -c 10 -o nuclei_result.txt -silent
```
-> 중요도가 중간 이상인 취약점만 선별하고 요청 수와 동시성을 제한하여 안정적으로 스캔한 뒤 결과를 파일로 저장

---

## 주의사항

- nuclei는 자동화 도구이므로 False Positive가 포함될 수 있어 반드시 수동 검증이 필요합니다
- 과도한 요청은 WAF 또는 IDS/IPS에 의해 차단될 수 있습니다
- 허가 없는 사이트에 대한 스캔 수행은 불법입니다
