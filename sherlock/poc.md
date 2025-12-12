# Sherlock

## Sherlock은 특정 유저네임(username)이 여러 웹 서비스에 존재하는지 여부를 자동으로 탐색하는 OSINT(Open Source Intelligence) 기반 도구입니다.

- GitHub, Twitter, Instagram 등 수백 개의 공개 웹 서비스를 대상으로 동일한 유저네임이 사용되고 있는지를 검사하며, 존재하는 경우 해당 서비스명과 프로필 URL을 함께 출력합니다.


## 목적

- 본 실습에서는 필자의 GitHub 유저네임인 psj-labs를 대상으로 검색을 수행합니다.


## Sherlock 설치 확인

- Sherlock이 정상적으로 설치되었는지 확인하기 위해
버전 정보를 출력하는 명령어를 사용합니다.

```text
sherlock --version
```

![sherlock --version](./sherlock/imgs/sherlock%20--version.png)

- 출력 결과는 다음과 같습니다.

```text
Sherlock v0.15.0
```

- 버전 정보가 정상적으로 출력되므로 Sherlock이 올바르게 설치되었음을 확인할 수 있습니다.


## 사용 방법

- Sherlock의 기본 사용법은 다음과같이 매우 단순합니다.

```text
sherlock [검색할 유저네임]
```

- 입력한 문자열을 기준으로 Sherlock이 지원하는 여러 웹 서비스에 대해 해당 유저네임의 존재 여부를 순차적으로 검사합니다.


## 실제 문자열 검색

- 필자의 GitHub 유저네임인 `psj-labs`를 검색하기 위해
다음 명령어를 실행합니다.

```text
sherlock psj-labs
```

- 명령어 실행 후 잠시 대기하면, Sherlock은 각 웹 서비스에 대해 유저네임 존재 여부를 검사하고 결과를 터미널에 출력합니다.

![searching](./sherlock/imgs/searching.png)

- 출력 결과 중 GitHub 항목에서 psj-labs 유저네임이 발견되었으며, 해당 계정으로 접근 가능한 URL이 함께 출력됩니다.

![github result](./sherlock/imgs/github%20result.png)


## 결과 검증

- 출력된 GitHub URL을 `Ctrl` 키를 누른 상태로 클릭하여 실제 페이지에 접근하였습니다.

![github page](./sherlock/imgs/github%20page.png)

- 접속 결과 Sherlock이 출력한 URL이 실제 필자가 찾고자하는 GitHub 프로필 페이지와 정확히 일치함을 확인합니다

- 이를 통해 Sherlock이 공개 웹 서비스를 대상으로 유저네임 존재 여부를 정확히 탐색하고 있음을 증명합니다.


## 요약

- Sherlock을 활용하면 특정 유저네임이 인터넷 상 여러 서비스에 분산되어 존재하는지를 빠르고 효율적으로 확인할 수 있습니다.

- 해당 도구는 OSINT 관점에서 계정 조사, 정보 수집, 침투 테스트 초기 정찰 단계에서 유용하게 활용될 수 있습니다.
