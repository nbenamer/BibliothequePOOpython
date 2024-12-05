-- Ces requêtes insèrent des informations sur les étudiants, les cours et leurs inscriptions respectives dans les tables Students, Courses et Enrollments.

INSERT INTO Students (student_id, name, age, gender)
VALUES
(1, 'Alice Johnson', 21, 'Femme'),
(2, 'Bob Smith', 22, 'Homme'),
(3, 'Carol White', 20, 'Femme'),
(4, 'David Brown', 23, 'Homme'),
(5, 'Eva Davis', 22, 'Femme');

INSERT INTO Courses (course_id, course_name, credits, capacity)
VALUES
(1, 'Introduction à l\informatique', 3, 30),
(2, 'Mathématiques avancées', 4, 25),
(3, 'Physique pour ingénieurs', 3, 20),
(4, 'Structures de données et algorithmes', 3, 30);


INSERT INTO Enrollments (student_id, course_id)
VALUES
(1, 1),
(1, 2), 
(1, 3); 


INSERT INTO Enrollments (student_id, course_id)
VALUES
(2, 1), 
(2, 4); 


INSERT INTO Enrollments (student_id, course_id)
VALUES
(3, 2), 
(3, 4); 


INSERT INTO Enrollments (student_id, course_id)
VALUES
(4, 1), 
(4, 2), 
(4, 3); 


INSERT INTO Enrollments (student_id, course_id)
VALUES
(5, 1), 
(5, 2), 
(5, 4);
