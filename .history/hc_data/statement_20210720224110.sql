SELECT USER_ID, (AMOUNT * rate)
FROM (SELECT Min(CREATED_DATE), USER_ID, TYPE, STATE, CURRENCY, AMOUNT
FROM transactions 
GROUP by USER_ID), fx_rates
WHERE TYPE = 'CARD_PAYMENT' AND STATE = 'COMPLETED' AND CURRENCY = ccy AND base_ccy = 'USD' AND (AMOUNT * rate) >= 10;


S