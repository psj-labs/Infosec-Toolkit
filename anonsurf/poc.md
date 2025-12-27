# anonsurf

- **anonsurf는 시스템의 모든 네트워크 트래픽을 Tor 네트워크로 강제 라우팅하여 익명성을 제공하는 도구입니다.**

---

## anonsurf 시작

- 다음은 Tor 네트워크를 실행한 모습이며 명령어는 다음과 같습니다.
```text
anonsurf start
```
![01](/anonsurf/imgs/01.png)

- 출력 중 나타나는 `Tor is not running! starting it for you` 라는 문구는 **Tor 데몬이 실행 중이 아니어서 AnonSurf가 자동으로 Tor를 실행했다는 의미**입니다.  

---

## anonsurf 상태 확인

anonsurf와 Tor가 정상적으로 작동 중인지 확인하기 위해 다음 명령어를 사용합니다.

```text
anonsurf status
```

![02](/anonsurf/imgs/02.png)

- 출력 결과에서 `Active: active (exited)` 라고 파란색 글씨로 표시되면 **anonsurf가 정상적으로 활성화되어 있는 상태**임을 의미합니다.

---

## 외부에서 보이는 IP 주소 확인

- 현재 Tor 네트워크를 통해 외부에 노출되는 IP 주소를 확인할 수 있습니다.

```text
anonsurf myip
```

![03](/anonsurf/imgs/03.png)

- 출력되는 IP 주소는 **실제 로컬 IP가 아니라 Tor Exit Node의 IP 주소**입니다.

---

## Tor IP 변경 (회선 변경)

- 현재 연결된 Tor 네트워크의 회선을 끊고 새로운 Tor 노드(IP)로 강제 변경할 수 있습니다.

```text
anonsurf change
```

![10](/anonsurf/imgs/10.png)

- IP 변경 후 다시 `anonsurf myip` 명령어를 실행하면 **IP 주소가 변경된 것을 확인할 수 있습니다.**

---

## Tor IP 자동 변경 (주기적 변경)

- 매번 수동으로 IP를 변경하는 것은 번거롭기 때문에 `watch` 명령어를 사용해 일정 주기로 Tor IP를 자동 변경할 수 있습니다.

- 필자는 **5초마다 Tor IP가 변경되도록 설정**하였습니다.

```text
watch -n 5 "sudo anonsurf change"
```

![04](/anonsurf/imgs/04.png)

- 엔터를 누르면 `Every 5.0s: sudo anonsurf change` 라는 문구가 출력되며 **5초마다 자동으로 Tor 회선이 변경**됩니다.

![05](/anonsurf/imgs/05.png)

---

## 외부 사이트를 통한 IP 및 국가 확인

- Tor를 통해 외부에서 보이는 IP와 국가 정보를 확인할 수 있는 사이트는 다음과 같습니다.

```text
https://www.dnsleaktest.com
```

![06](/anonsurf/imgs/06.png)

- 해당 사이트에서는 현재 사용 중인 IP 주소와 해당 IP가 속한 국가 정보를 확인할 수 있습니다.

---

## IP 변경 확인 테스트

- 5초마다 Tor IP가 변경되도록 설정했으므로 아래 명령어를 여러 번 실행하면 **매번 다른 IP 주소가 출력되어야 합니다.**

```text
anonsurf myip
```

![07](/anonsurf/imgs/07.png)

- 여러 차례 실행 결과 IP가 정상적으로 변경되는 것을 확인할 수 있습니다.

---

## anonsurf 종료

- anonsurf를 종료하고 싶을 경우 다음 명령어를 실행합니다.

```text
anonsurf stop
```

![08](/anonsurf/imgs/08.png)

---

## 종료 상태 확인

- 정상적으로 종료되었는지 확인하기 위해 다음 명령어를 실행합니다.

```text
anonsurf status
```

![09](/anonsurf/imgs/09.png)

- `Active: inactive (dead)` 라고 출력되면 **anonsurf가 정상적으로 종료된 상태**입니다.
