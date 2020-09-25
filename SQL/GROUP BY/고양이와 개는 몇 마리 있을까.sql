/*  ANIMAL_TYPE으로 GROUP BY 해주면 cat과 dog 두 종류로 묶인다.
	COUNT를 해서 각각 몇마리인지 구하고, 고양이를 먼저 조회하라고 했으므로 ORDER BY로 정렬해준다. */
SELECT		ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS 'count'
FROM		ANIMAL_INS
GROUP BY	ANIMAL_TYPE
ORDER BY	ANIMAL_TYPE;