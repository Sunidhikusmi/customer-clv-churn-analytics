-- Churn summary
SELECT
    churned,
    COUNT(customerid) AS customers
FROM churn
GROUP BY churned;

--Revenue impact of churn
SELECT
    c.churned,
    SUM(cl.total_revenue) AS revenue
FROM churn c
JOIN clv cl
    ON c.customerid = cl.customerid
GROUP BY c.churned;
