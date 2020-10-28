/* 아직 입양을 못 간 동물 중 가장 오래 보호소에 있었던 동물 3마리 출력하기 
	ANIMAL_ID가 INS에는 있지만 OUTS에 없는 것들 추린 다음 정렬하기
    최대 3개만 출력: 가장 마지막에 LIMIT 3*/
SELECT	NAME, DATETIME 
FROM	ANIMAL_INS AS I
WHERE	I.ANIMAL_ID NOT IN(
			SELECT	O.ANIMAL_ID
            FROM	ANIMAL_OUTS AS O)
ORDER BY I.DATETIME
LIMIT 3;