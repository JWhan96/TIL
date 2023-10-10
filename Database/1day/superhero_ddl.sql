-- SQL 문 작성시 주의 사항
-- 세미콜론(;) 기준으로 하나의 SQL문 판별

-- 새로운 테이블을 생성
-- id, 이름, 직업, 능력, 국적, 소속회사, 나이
-- 필드명, 타입, 제약조건 순으로 작성
CREATE TABLE superheroes (
  -- AUTOINCREMENT 값이 하나씩 자동으로 증가
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  -- NOT NULL 이 값은 빈 값이면 안된다 필수 기입사항
  이름 TEXT NOT NULL,
  직업 TEXT NOT NULL,
  능력 TEXT,
  국적 TEXT,
  소속회사 TEXT,
  나이 INTEGER

);

-- 테이블명 변경하기
-- ALTER TABLE -> RENAME TO
ALTER TABLE superheroes
RENAME TO superhero;

-- 새로운 컬럼 추가
-- ALTER TABLE -> ADD COLUMN
ALTER TABLE superhero
ADD COLUMN 가입날짜 DATE;

-- 임시 컬럼 추가
ALTER TABLE superhero
ADD COLUMN 임시 TEXT;
-- 임시 컬럼 -> 곧삭제 컬럼
-- ALTER TABLE -> RENAME COLUMN ~ TO ~
ALTER TABLE superhero
RENAME COLUMN 임시 TO 곧삭제;
-- 곧삭제 컬럼 삭제
ALTER TABLE superhero
DROP COLUMN 곧삭제;

-- 테이블 지우기
DROP TABLE superhero;
