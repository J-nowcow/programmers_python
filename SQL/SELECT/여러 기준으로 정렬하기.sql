-- ORDER BY 에 인자 여러 개 넣을 수 있음: 콤마로 연결, 앞에 오는걸로 먼저 정렬하고 동일할 때만 뒤 조건으로 정렬
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC