# DOVAHKIIN

기본적으로 2개의 스크립트가 경쟁하는  시스템이다.

2차원 탑뷰로 시각화되는 전장에서, 각 팀당 5명의 유닛이 주어지는 팀이 2팀 존재한다.
이 두 팀의 유닛들은 Black, White 둘 중의 하나의 색깔 특성을 가지게 된다.
이 색깔은 반전되면 Black -> White, White -> Black으로 바뀔 수 있다.

이 두 팀의 유닛들에게 두 개의 AI Script가 각각 적용된다.

이 유닛들은 다음과 같은 행동을 취한다.

* 상하좌우로의 2차원 운동
* 상하좌우로의 탄환 생성 및 발사

유닛들에게 적용되는 물리법칙은 다음과 같은 성질을 가진다

* 충돌 무시
* 회전관성, 각속도등의 회전운동은 없음
* 선속도만 존재

탄환은 다음과 같은 성질을 가진다

* 유닛에 의해 생성됨
* 한 유닛당 필드에 동시에 구현가능한 탄환은 B개로 제한
* 탄환은 필드밖으로 벗어나거나 어떠한 유닛과 충돌했을 경우 파괴됨
* 유닛과 충돌할경우 충돌한 유닛은 색깔이 반전됨

위와 같은 규칙에서, AI Script의 목적은 모든 유닛들의 색깔을 특정 색깔로 바꾸는 것이다.

예를 들어, 초기에 White인 유닛들에게 적용되는 Script의 목적은 모든 유닛을 White로 바꾸는 것이다.

![asdf](static/screenshot.png)

AI Script에게 주어지는 정보는 다음과 같다.

* Phase ID: 게임 시작으로부터 몇번째로 이 정보를 사용하고 있는지
* array of Units: 각 유닛들에 대한 정보
  * Position: 현재 위치
  * Velocity: 현재 속도
  * Color: 현재 색깔
* array of Bullets: 각 탄환들에 대한 정보
  * Position: 현재 위치
  * Velocity: 현재 속도
* Screen size: 필드의 크기

AI Script는 각 상황에 대해 위에 주어진 정보를 가지고 Greedy하게 판단해야 하고 글로벌 변수 사용을 최대한 자제해야 한다.
모든 유닛들은 색깔이 반전되더라도 적용되는 AI Script는 유지된다.

AI Script가 처음부터 자신이 White에 적용되는 Script임을 상정하고 만들어진 것이라면, 운 좋게 White에 걸렸을 때는 상대방에 비해 너무 유리하고, 자신의 원래 팀이 어느 쪽인지 헷갈리게 하는 것이 게임의 주요 목적이므로 Script간의 평가는 양쪽 색깔을 번갈아가면서 4번 정도 진행하는 것으로 해야한다.

위와 같은 상황에서 Script에 기대할 수 있는 행동은 이렇다.

만약 자신의 색깔이 주어진다고 해도, 자신의 초기 색깔은 알 수가 없다. 그러므로, 어떤 방식으로든 자신의 원래 색깔을 게임 시작시에 필드에 남길 수 있어야 하는데, 가장 간단한 방법은 뭉쳐다니는 것일 것이다. 뭉쳐다니게 되면, 탄환에 맞아 색깔이 변하더라도 주변 유닛들의 색깔 양상을 보고 자신의 원래 색깔을 판단할 수 있을 것이다. 혹은 유닛끼리 3명 이상의 셀 단위로 행동하게 되면, 한 명이 맞는 순간 나머지 팀원들이 색깔을 반전시켜주고, 반전될 유닛은 주변 상황을 보고 일부러 탄환을 맞아준다면 셀의 모든 팀원들이 각자의 색깔을 유지할 수 있을 것이다.
다만, 위와 같은 전략은 유닛들간의 협업이 생겨야 가능한데, 이런 일이 강화학습으로 일어날 수 있는지 실험하는 것이 최종 목적이다.



### Agent specification


	Arguments:
		phase_id: Auto-incremented id of each phase
	    units: array of information of each units
	        pos: position (Vector2)
	        vel: velocity (Vector2)
	        color
	    bullets: array of information of each bullets in screen
	        pos: position (Vector2)
	        vel: velocity (Vector2)
	
	Returns:
	    One-hot encoding informations of below
	    1. Move right (1 if right, 0 if not move, -1 if left)
	    2. Move down  (1 if down,  0 if not move, -1 if up  )
	    3. shoot (1 if shoot, 0 if not shoot)
	    4. shoot velocity x (-1 ~ 1)
	    5. shoot velocity y (-1 ~ 1)
### Basic game configurations

``` python

'''
Configurations
'''
DISPLAY_SIZE = (128, 128)
DISPLAY_CAPTION = 'Dovakin'
STATIC_FPS = 30
BG_COLOR = (0, 0, 0)

'''
Game factor
'''
BULLET_PER_UNIT = 3
DEFAULT_UNIT_SIZE = (5, 5)
DEFAULT_BULLET_SIZE = (1, 1)
UNIT_SPEED = 1
BULLET_SPEED = 10
UNIT_STOP_THRESHOLD = 0.5
LIN_DRAG = 0.9
UNIT_NUM = 6
```

