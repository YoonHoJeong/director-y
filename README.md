# 환경

- pip-requirements.txt : 필요한 패키지 작성.

1. 가상환경 설치 & 활성화
2. 패키지 설치 - "pip install pip-requirements.txt"
3. 패키지 추가 설치 or 패키지 업데이트를 했을 경우,
   "pip freeze > pip-requirements.txt"

# 진행 상황

- register 페이지에서 회원가입 가능
- 모델 기본 구조 생성

# Apps

## 1. accounts

사용자 모델과 관련된 역할을 수행하는 App.

logout, login, signup 등의 기능을 수행.

### 모델

1. Profile

   - Actor, Director, Staff가 상속하는 모델.
   - 3가지 모델이 모두 갖고있는 기본 정보들
     - email, name, username, 등.

2. Actor
   : 배우 모델 - Profile 모델을 상속. - company, height, weight, specialty, 등. - ActorImage, ActorVideo, Movie 모델이 Actor로 연결되어 있음(foreign key).

3. Director
   : 감독 모델 - Profile 모델을 상속. - Movie 모델이 Director로 연결되어 있음(foreign key).

4. Staff
   : 스탭 모델 - Profile 모델을 상속. - SPortfolio, Movie 모델이 Staff로 연결되어 있음(foreign key). - 다양한 스탭 역할별 role(조명, 분장 등), 사용하는 tool(에프터이펙트, 포토샵, 카메라 기종 등).

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
