-- ============================================================
-- CUSTOMER TREND DATA ANALYSIS
-- SQL ANALYSIS
-- ============================================================

USE customer_trends;


-- ============================================================
-- 1. TOTAL SALES
-- ============================================================

SELECT
    SUM(purchase_amount_usd) AS total_sales
FROM customer_shopping;


-- ============================================================
-- 2. AVERAGE PURCHASE AMOUNT
-- ============================================================

SELECT
    AVG(purchase_amount_usd) AS average_purchase_amount
FROM customer_shopping;


-- ============================================================
-- 3. SALES BY PRODUCT CATEGORY
-- ============================================================

SELECT
    category,
    SUM(purchase_amount_usd) AS total_sales,
    COUNT(*) AS total_purchases,
    AVG(purchase_amount_usd) AS average_purchase
FROM customer_shopping
GROUP BY category
ORDER BY total_sales DESC;


-- ============================================================
-- 4. TOP 10 PRODUCTS BY SALES
-- ============================================================

SELECT
    item_purchased,
    SUM(purchase_amount_usd) AS total_sales,
    COUNT(*) AS total_purchases,
    AVG(purchase_amount_usd) AS average_purchase
FROM customer_shopping
GROUP BY item_purchased
ORDER BY total_sales DESC
LIMIT 10;


-- ============================================================
-- 5. SALES BY GENDER
-- ============================================================

SELECT
    gender,
    COUNT(*) AS total_purchases,
    SUM(purchase_amount_usd) AS total_sales,
    AVG(purchase_amount_usd) AS average_purchase
FROM customer_shopping
GROUP BY gender
ORDER BY total_sales DESC;


-- ============================================================
-- 6. SUBSCRIPTION ANALYSIS
-- ============================================================

SELECT
    subscription_status,
    COUNT(*) AS total_customers,
    SUM(purchase_amount_usd) AS total_sales,
    AVG(purchase_amount_usd) AS average_purchase
FROM customer_shopping
GROUP BY subscription_status
ORDER BY total_sales DESC;


-- ============================================================
-- 7. SALES BY SEASON
-- ============================================================

SELECT
    season,
    COUNT(*) AS total_purchases,
    SUM(purchase_amount_usd) AS total_sales,
    AVG(purchase_amount_usd) AS average_purchase
FROM customer_shopping
GROUP BY season
ORDER BY total_sales DESC;


-- ============================================================
-- 8. PAYMENT METHOD ANALYSIS
-- ============================================================

SELECT
    payment_method,
    COUNT(*) AS total_transactions,
    SUM(purchase_amount_usd) AS total_sales,
    AVG(purchase_amount_usd) AS average_purchase
FROM customer_shopping
GROUP BY payment_method
ORDER BY total_sales DESC;


-- ============================================================
-- 9. AVERAGE RATING BY CATEGORY
-- ============================================================

SELECT
    category,
    AVG(review_rating) AS average_rating,
    COUNT(*) AS total_reviews
FROM customer_shopping
GROUP BY category
ORDER BY average_rating DESC;


-- ============================================================
-- 10. SALES BY LOCATION
-- ============================================================

SELECT
    location,
    COUNT(*) AS total_purchases,
    SUM(purchase_amount_usd) AS total_sales,
    AVG(purchase_amount_usd) AS average_purchase
FROM customer_shopping
GROUP BY location
ORDER BY total_sales DESC;


-- ============================================================
-- 11. DISCOUNT IMPACT ANALYSIS
-- ============================================================

SELECT
    discount_applied,
    COUNT(*) AS total_purchases,
    SUM(purchase_amount_usd) AS total_sales,
    AVG(purchase_amount_usd) AS average_purchase
FROM customer_shopping
GROUP BY discount_applied
ORDER BY total_sales DESC;


-- ============================================================
-- 12. PROMO CODE ANALYSIS
-- ============================================================

SELECT
    promo_code_used,
    COUNT(*) AS total_purchases,
    SUM(purchase_amount_usd) AS total_sales,
    AVG(purchase_amount_usd) AS average_purchase
FROM customer_shopping
GROUP BY promo_code_used
ORDER BY total_sales DESC;


-- ============================================================
-- 13. PURCHASE FREQUENCY ANALYSIS
-- ============================================================

SELECT
    frequency_of_purchases,
    COUNT(*) AS total_customers,
    SUM(purchase_amount_usd) AS total_sales,
    AVG(purchase_amount_usd) AS average_purchase
FROM customer_shopping
GROUP BY frequency_of_purchases
ORDER BY total_customers DESC;


-- ============================================================
-- 14. SHIPPING TYPE ANALYSIS
-- ============================================================

SELECT
    shipping_type,
    COUNT(*) AS total_orders,
    SUM(purchase_amount_usd) AS total_sales,
    AVG(purchase_amount_usd) AS average_purchase
FROM customer_shopping
GROUP BY shipping_type
ORDER BY total_orders DESC;


-- ============================================================
-- 15. PREVIOUS PURCHASE HISTORY ANALYSIS
-- ============================================================

SELECT
    CASE
        WHEN previous_purchases = 0 THEN '0 Purchases'
        WHEN previous_purchases BETWEEN 1 AND 10 THEN '1-10 Purchases'
        WHEN previous_purchases BETWEEN 11 AND 20 THEN '11-20 Purchases'
        WHEN previous_purchases BETWEEN 21 AND 30 THEN '21-30 Purchases'
        ELSE '31+ Purchases'
    END AS purchase_history_group,
    COUNT(*) AS total_customers,
    SUM(purchase_amount_usd) AS total_sales,
    AVG(purchase_amount_usd) AS average_purchase
FROM customer_shopping
GROUP BY purchase_history_group
ORDER BY total_customers DESC;