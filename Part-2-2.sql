/*
    Given a database with the following tables and attributes, which organizations have the most severe patient population?
    Providers: provider_id, organization_id, organization_name
    Phq9: patient_id, provider_id, score, datetime_created
*/

SELECT organization_name AS 'Severe Patient Organizations', avg(score) AS 'Phq9 Score'
FROM providers, phq9
WHERE providers.provider_id = phq9.provider_id
GROUP BY organization_name
HAVING avg(score) >= 20
ORDER BY 'Phq9 Score' ASC
LIMIT 5;