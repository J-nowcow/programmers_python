/*  이름에 el 들어가는 강아지 찾기
	대소문자 무시하기: lower 씌워주고 확인
    NAME 순으로 정렬 */

SELECT	ANIMAL_ID, NAME
FROM	ANIMAL_INS
WHERE	LOWER(NAME) LIKE '%el%' AND ANIMAL_TYPE = "Dog"
ORDER BY NAME;