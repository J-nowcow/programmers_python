/*  DISTINCT를 쓰면 중복되는 원소는 하나만 계산해 준다.
	NULL인 경우는 집계하지 말라고 하였으므로 WHERE에 NOT NULL을 넣어서 처리해준다. */
SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL