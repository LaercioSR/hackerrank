SELECT IF((A+B)<=C or (C+B)<=A or (A+C)<=B, "Not A Triangle", IF(A=B and B=C, "Equilateral", IF(A=B or B=C or A=C, "Isosceles", "Scalene")))
FROM TRIANGLES;