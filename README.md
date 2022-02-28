# Intro
영화제에서 수상하지 못한 대다수의 영화들은 그 누구에게도 공개되지 않고 버려지게 됩니다.   
짧게는 몇 개월에서 길게는 몇 년이 걸린 영화들이 한 번의 평가로 잊혀지지 않도록, 결과와 과정까지 아카이빙 할 수 있도록 'Directory'를 제작했습니다.   
영화 제작에 참여하는 1) 감독 2) 배우 3) 스태프들이 각각의 필요에 맞춰 자신만의 필모그래피를 만들 수 있습니다.


# Project Status
- 2021.03 ~ 현재 : **배포 중단**
- 2020.12 ~ 2021.02 : 테스트 서버 배포(pythonAnywhere 배포 환경)
- 2020.10 ~ 2020.12 : 서비스 개발 및 테스트 서버 배포


# Development Enviroments

- pip-requirements.txt : 필요한 패키지 작성.

1. 가상환경 설치 & 활성화
2. 패키지 설치 - "pip install pip-requirements.txt"
3. 패키지 추가 설치 or 패키지 업데이트를 했을 경우,
   "pip freeze > pip-requirements.txt"

# Apps

## 1. accounts

사용자 모델과 관련된 역할을 수행하는 App.

logout, login, signup 등의 기능을 수행.

### 모델

1. Profile

   - 로그인 / 인증에 사용하는 기본 모델.
   - Actor, Director, Staff가 연결된 모델.
   - 위 3가지 모델이 모두 갖고있는 기본 정보들
     - email, name, username, 등.
   - u_type을 통해 위 3가지 모델 타입을 구분 (1: director, 2: actor, 3: staff)

2. Actor
   : 배우 모델

   - Profile 모델과 one-to-one relationship.
   - company, height, weight, specialty, 등. - ActorImage, ActorVideo, Movie 모델이 Actor로 연결되어 있음(foreign key).

3. Director
   : 감독 모델

   - Profile 모델과 one-to-one relationship.
   - Movie 모델이 Director로 연결되어 있음(foreign key).

4. Staff
   : 스탭 모델
   - Profile 모델과 one-to-one relationship.
   - SPortfolio, Movie 모델이 Staff로 연결되어 있음(foreign key).
   - 다양한 스탭 역할별 role(조명, 분장 등), 사용하는 tool(에프터이펙트, 포토샵, 카메라 기종 등).

## 2. main

포트폴리오와 관련된 주요 기능을 담당하는 App.

### 모델

1. Movie
   - 영화에 대한 정보를 담는 모델.
   - Director의 포트폴리오
   - 배우, 스탭도 자신의 경력을 기입하기 위해 작성할 수 있다.
1. MovieSection
   - Movie 모델의 하위 섹션.
   - Director가 시나리오, 예산 등 섹션을 나누기 위해 사용할 수 있다.
   - (naver Smarteditor를 사용할 예정)
1. SPortfolio
   - Staff의 포트폴리오
   - (naver Smarteditor를 사용할 예정)
1. ActorVideo
1. ActorImage
   - Actor는 글보다는 시각적인 자료 위주로 포트폴리오를 구성할 수 있도록 설계.
   - ActorVideo, ActorImage 모두 Actor 모델로 Foreign로 연결.
