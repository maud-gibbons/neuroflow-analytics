/*
    Given a database with the following tables and attributes, what percentage of users completed an exercise in their first month per monthly cohort?
    Users: user_id, created_at
    Exercises: exercise_id, user_id, exercise_completion_date
*/

SELECT strftime('%m/%Y', created_at) AS 'Monthly Cohort', 
    count(CASE WHEN strftime('%m/%Y', exercise_completion_date) = strftime('%m/%Y', created_at) THEN 1 ELSE NULL END) / CAST(count(*) AS float) AS 'X% First Month Completion'
FROM users, exercises
WHERE users.user_id = exercises.user_id
GROUP BY strftime('%m/%Y', created_at);
