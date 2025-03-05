DROP TABLE IF EXISTS temp_spends_month;
CREATE TEMPORARY TABLE temp_spends_month
AS

SELECT 
      ca.name AS category
    , su.name  AS subcategory
    , SUM(tk.total_price) AS spends
    , DATE_FORMAT(tr.dt_launch, '%Y-%m') AS ym
    
FROM 
	ticket AS tk
    
LEFT JOIN
	transaction as tr
    ON tr.id_transaction = tk.fk_id_transaction

LEFT JOIN
	category AS ca
    ON ca.id_category = tr.fk_id_category
    
LEFT JOIN
	subcategory AS su
    ON su.id_subcategory = tr.fk_id_sub_category
    
WHERE
	tr.fk_id_transaction_type = 1
    
GROUP BY
	  DATE_FORMAT(tr.dt_launch, '%Y-%m')
	, subcategory
    , category

ORDER BY
	   ym
	 , spends DESC;
    
    SELECT  
	*
    FROM
		temp_spends_month;
	
SET @sql = NULL;
SELECT
  GROUP_CONCAT(DISTINCT
    CONCAT(
      'SUM(CASE WHEN subcategory = ''',
      subcategory,
      ''' THEN spends ELSE 0 END) AS ',
      CONCAT('`', subcategory, '`')
    )
  ) INTO @sql
FROM temp_spends_month;

SET @sql = CONCAT('SELECT  ', @sql, ' 
					FROM 
						temp_spends_month
					GROUP BY 
						ym
					ORDER BY ym');

select  @sql;

PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;