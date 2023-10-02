1. models부분에서 클래스들 외워야 하는것인지?
    - 그냥 CharField(max_length=10), TextField()이런것들만 외우면 되는것 같긴함
2. DB에 수정하면서 0002이후로 3 4가 생겼는데 복구는 어떻게 하는건지
    - 그냥 지우면 되는건지 아니면 일련의 과정이 필요한건지
    - 하고 나니까 오류가 생겼었음

# 그냥 알고리즘 질문
# K = 가지고 있는 랜선의 개수, N = 필요한 랜선의 개수
K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
start, end = 1, max(arr)  # 이분탐색 처음과 끝위치

while start <= end:  # 적절한 랜선의 길이를 찾는 알고리즘
    mid = (start + end) // 2  # 중간 위치
    lines = 0  # 랜선 수
    for i in arr:
        lines += i // mid  # 분할 된 랜선 수

    if lines >= N:  # 랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1
print(end)


### 방법
1. articles/models.py에 article클래스 등록
2. admin 계정 생성 (python manage.py createsuperuser)
3. articles/admin.py 를 통해 Article 모델 클래스를 admin site에 등록

### 데이터 베이스 이용
1. model 클래스를 기반으로 최종설계도 작성(python manage.py makemigrations)
2. 최종설계도를 DB에 전달하여 반영(python manage.py migrate)
3. migrate후 db.sqlite에서 테이블 확인
4. 추가할경우 변경후 1~2 반복
#### 참고
1. 데이터 베이스 초기화 방법
   1. migration파일 삭제(0001, 0002 등등)
   2. db.sqlite3 파일삭제
      - __init__.py와 migrations 폴더를 지우지 않도록 주의
2. migrations이 제대로 되었는지 확인하는 명령어(python manage.py showmigrations) ([x]표시가 되어있으면 제대로 된 것)
3. 해당 migrations 파일이 SQL언어로 어떻게 번역되어 DB에 전달되는지 확인하는 명령어

#### 참고자료
- 안전한 패스워드 저장(검색)
- 네이버에서 만든 자료 참고하면 도움