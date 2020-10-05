/*	갑분 렙4
	(1)과 다르게, 입양된 기록이 하나도 없는 시간대에 0을 출력해줘야 한다.
	0부터 23까지 전부 0인 값을 가지는 테이블을 하나 만들어 준 다음, LEFT JOIN 해준다.
    테이블을 노가다로 만들 수도 있지만, RECURSIVE 구문을 활용하면 깔끔해진다.
	WITH RECURSIVE에서는 반드시 UNION을 사용하고, 1개 이상의 비 반복문을 사용해야 한다.
    또한, 반복문은 반드시 정지 조건이 들어가야 한다. (WHERE n < 23)
    timeset이라는 이름을 가진 테이블에, n이라는 이름을 가진 열을 만들어서 거기에 0부터 23까지 값을 0으로 채워준다.
*/
WITH RECURSIVE timeset AS
(
    SELECT 0 AS n
    UNION
    SELECT n + 1 FROM timeset WHERE n < 23
)
SELECT		timeset.n AS 'HOUR', COUNT(HOUR(ANIMAL_OUTS.DATETIME)) AS 'COUNT'
FROM		timeset
LEFT JOIN	ANIMAL_OUTS ON timeset.n = HOUR(ANIMAL_OUTS.DATETIME)
GROUP BY	timeset.n;