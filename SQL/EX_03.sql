SELECT 
    GREATEST(
        (a * (b + c)), 
        (a * b * c), 
        (a + (b * c)), 
        ((a + b) * c), 
        ((a * b) + c), 
        (a + b + c)
    ) AS res
FROM 
    expression_matter;