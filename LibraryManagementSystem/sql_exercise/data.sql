
-- Cette requête affiche les noms des étudiants, les cours auxquels ils sont inscrits, ainsi que le nombre de crédits de ces cours.
SELECT 
    Students.name AS student_name,
    Courses.course_name,
    Courses.credits
FROM 
    Students
JOIN 
    Enrollments ON Students.student_id = Enrollments.student_id
JOIN 
    Courses ON Enrollments.course_id = Courses.course_id;

-- Cette requête sélectionne les étudiants qui ne sont inscrits à aucun cours.
SELECT 
    Students.name AS student_name
FROM 
    Students
LEFT JOIN 
    Enrollments ON Students.student_id = Enrollments.student_id
WHERE 
    Enrollments.enrollment_id IS NULL;

-- Cette requête calcule le nombre d'étudiants inscrits à chaque cours, en incluant les cours sans inscription.
SELECT 
    Courses.course_name,
    COUNT(Enrollments.student_id) AS number_of_students
FROM 
    Courses
LEFT JOIN 
    Enrollments ON Courses.course_id = Enrollments.course_id
GROUP BY 
    Courses.course_name;

-- Cette requête trouve les cours ayant plus de la moitié de leur capacité en nombre d'inscriptions.
SELECT 
    Courses.course_name,
    COUNT(Enrollments.student_id) AS number_of_students,
    Courses.capacity
FROM 
    Courses
LEFT JOIN 
    Enrollments ON Courses.course_id = Enrollments.course_id
GROUP BY 
    Courses.course_name
HAVING 
    COUNT(Enrollments.student_id) > Courses.capacity / 2;

-- Cette requête trouve les étudiants inscrits à un nombre maximal de cours.
SELECT 
    Students.name AS student_name,
    COUNT(Enrollments.course_id) AS number_of_courses
FROM 
    Students
JOIN 
    Enrollments ON Students.student_id = Enrollments.student_id
GROUP BY 
    Students.student_id
HAVING 
    COUNT(Enrollments.course_id) = (
        SELECT MAX(course_count)
        FROM (
            SELECT COUNT(course_id) AS course_count
            FROM Enrollments
            GROUP BY student_id
        ) AS course_counts
    );

-- Cette requête calcule le total des crédits pour chaque étudiant inscrit à des cours.
SELECT 
    Students.name AS student_name,
    SUM(Courses.credits) AS total_credits
FROM 
    Students
JOIN 
    Enrollments ON Students.student_id = Enrollments.student_id
JOIN 
    Courses ON Enrollments.course_id = Courses.course_id
GROUP BY 
    Students.student_id;

--Cette requête sélectionne les noms des cours pour lesquels il n'y a aucune inscription dans la table Enrollments.
SELECT 
    Courses.course_name
FROM 
    Courses
LEFT JOIN 
    Enrollments ON Courses.course_id = Enrollments.course_id
WHERE 
    Enrollments.course_id IS NULL;


--Cette requête supprime toutes les inscriptions associées au cours ayant l'identifiant 1.
DELETE FROM Enrollments
WHERE course_id = 1;


-- Cette requête supprime les étudiants qui n'ont aucune inscription associée dans la table
DELETE FROM Students
WHERE student_id IN (
    SELECT Students.student_id
    FROM Students
    LEFT JOIN Enrollments ON Students.student_id = Enrollments.student_id
    WHERE Enrollments.student_id IS NULL
);
