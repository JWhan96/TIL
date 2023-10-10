-- 01. Querying data
SELECT LastName --Field
From employees; --Table

SELECT LastName, FirstName
From employees;

SELECT * -- 전체필드 선택
FROM employees;

SELECT FirstName AS '이름' -- 다른 이름으로 import하는 법(출력할 때만 변경)
From employees;

SELECT Name, Milliseconds / 60000 AS '재생 시간(분)'
From tracks;
-- 이것도 동일??
SELECT Name, CAST(Milliseconds / 60000 AS INTEGER) AS '재생 시간(분)'
FROM tracks;

-- 02. Sorting data
-- 오름차순
SELECT FirstName
From employees
ORDER BY FirstName;
--결과는 동일
SELECT FirstName
From employees
ORDER BY FirstName ASC;

--내림차순
SELECT FirstName
From employees
ORDER BY FirstName DESC;


-- Country로 내림차순을 하고 
-- 같은 Country에서는 City내림차순
SELECT Country, City
From customers
ORDER BY Country DESC, City ASC;

-- 지정을 안해주면 지정한 정렬로만 정리
SELECT Name, Milliseconds / 60000 AS '재생 시간(분)'
From tracks
ORDER BY Milliseconds DESC;


-- NULL 정렬 예시
SELECT ReportsTo
From employees
ORDER BY ReportsTo;


-- 03. Filtering data
-- Distinct
-- Distinct 중복된 결과를 제거
SELECT DISTINCT Country
FROM customers
ORDER BY Country;

-- Where
-- Where 조회시 특정 검색 조건을 지정
SELECT LastName, FirstName, City
FROM customers
WHERE City = 'Prague';

SELECT LastName, FirstName, City
FROM customers
WHERE City != 'Prague';
--  NULL값은 IS로 확인 다른 조건들은 '='
SELECT 
  LastName, FirstName, Company, Country
FROM 
  customers
WHERE 
  Company IS NULL 
  AND Country = 'USA';

SELECT 
  LastName, FirstName, Company, Country
FROM 
  customers
WHERE 
  Company IS NULL 
  OR Country = 'USA';
-- ORDER BY
--   Country;

-- 범위지정
SELECT 
  Name, Bytes
FROM
  tracks
WHERE
  -- 10000 <= Bytes <= 500000; --이 문법은 불가
  
  -- Bytes >= 10000
  -- AND Bytes <= 500000;
  Bytes BETWEEN 10000 AND 500000;

-- 정렬까지(순서 중요)
SELECT 
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 10000 AND 500000
ORDER BY
  Bytes;

-- IN
SELECT LastName, FirstName, Country
FROM customers
WHERE
  -- Country = 'Canada' 
  -- OR Country = 'Germany' 
  -- OR Country = 'France';
-- 위 문법도 틀리지는 않지만 IN을 활용하면 더 깔끔
Country IN ('Canada', 'Germany', 'France'); 
-- NOT IN
SELECT LastName, FirstName, Country
from customers
WHERE  
  Country NOT IN ('Canada', 'Germany', 'France');

-- %son 0개이상의 문자열과 일치하는지 확인 
SELECT LastName, FirstName
FROM customers
WHERE LastName LIKE '%son';

SELECT LastName, FirstName
FROM customers
WHERE LastName LIKE 'Jo%';
-- 언더바 갯수만큼 앞에 존재해야함 단일문자와 일치하는지 확인
SELECT LastName, FirstName
FROM customers
WHERE FirstName LIKE '___a';

SELECT LastName, FirstName
FROM customers
WHERE FirstName LIKE 'j___';

-- LIMIT
SELECT TrackId, Name, Bytes
FROM tracks
ORDER BY Bytes DESC
LIMIT 7;

SELECT TrackId, Name, Bytes
FROM tracks
ORDER BY Bytes DESC
LIMIT 3, 4;
-- LIMIT 4 OFFSET 3;
-- offset을 지정해 줄수는 있지만 순서가 변한다.



-- 04. Grouping data
-- 집계함수와 함께 사용(SUM, AVG, MAX, MIN, COUNT)
-- Group by는 중복제거와 정렬가능
-- DISTINCT와의 차별점(각 그룹의 집계값 계산가능)
SELECT Country, COUNT(*)
FROM customers
GROUP BY Country;
-- group by한 기준으로 정렬이 되므로
-- 그 이외의 값으로 정렬하고 싶다면
-- order by(집계함수사용해서)를 이용해서 다시 정렬해야함
SELECT Composer, AVG(bytes) AS avgOfBytes
FROM tracks
GROUP BY Composer
ORDER BY avgOfBytes DESC;

-- 에러
SELECT Composer, AVG(Milliseconds / 60000) AS avgOfBytes
FROM tracks
WHERE avgOfBytes < 10
GROUP BY Composer;


-- 에러 해결
-- Group by에서는 조건문을 where 대신에 HAVING을 사용해야함
SELECT Composer, AVG(Milliseconds / 60000) AS avgOfBytes
FROM tracks
GROUP BY Composer
HAVING avgOfBytes < 10;
