/* 보호소에 들어올 당시에는 중성화되지 않았는데, 보호소를 나갈 때에는 중성화된 동물 찾기
	중성화를 거친 동물은 Spayed 또는 Neutered가 적혀 있음
    거치지 않은 동물은 Intact가 적혀 있음
    아이디 순으로 정렬하기 
    intake와 outcome이 다른 것들을 뽑는다는 식으로 확인도 가능함*/

SELECT	ANIMAL_ID, ANIMAL_TYPE, NAME
FROM	ANIMAL_INS AS I
WHERE	I.SEX_UPON_INTAKE LIKE '%Intact%'
AND		ANIMAL_ID IN (
			SELECT	O.ANIMAL_ID
            FROM	ANIMAL_OUTS AS O
            WHERE	O.SEX_UPON_OUTCOME LIKE '%Spayed%'
            OR		O.SEX_UPON_OUTCOME LIKE '%Neutered%')
ORDER BY ANIMAL_ID;