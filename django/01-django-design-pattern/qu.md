### 장고 프로젝트 생성 루틴
1. 가상환경(venv) 생성
    - python -m venv venv
2. 가상환경 활성화
   - source venv/Scripts/activate   (python interpreter 설정으로도 가능)
3. Django 설치
   - pip install Django
4. 의존성 파일 생성
   - pip freeze > requirements.txt (새로운 패키지 설치시마다 진행)
   - pip install -r requirements.txt(이미 txt파일이 있는경우 바로 설치 가능) 
5. Django 프로젝트 생성
   - django-admin startproject Name .  (. : 현재 디렉토리에 생성)
6. Django 서버 실행
    - python manage.py runserver
7. 앱 생성(앱 이름은 복수형으로 지정 권장)
   - python manage.py startapp articles
   - 앱 등록 (반드시 앱을 생성한후에 등록해야함)
   ```py
   INSTALLED_APPS = [
    'articles',
    'pages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ]
   ```

### 장고 디자인 패턴
#### 프로젝트 구조
1. settings.py
   - 프로젝트의 모든 설정을 관리
2. urls.py
   - URL과 이에 해당하는 적절한 views를 연결

#### 앱구조

1. admin.py
   - 관리자용 페이지 설정
2. models.py
   - DB와 관련된 Model을 정의
   - MTV 패턴의 M
3. views.py
   - HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환(url, mode, template와 연계)
   - MTV 패턴의 V
4. apps.py
5. tests.py


### 요청과 응답
- URLs
- views
- articles/templates/articles -> html파일 생성