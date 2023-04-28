# Description of change
Updated base_url variable which is used in all http requests.  The previous one no longer worked.

# Manual QA steps
 - Use Postman to try the previous HTTP request:  https://api.exchangeratesapi.io/2022-03-03?base=USD
 - Use Postman to try the current (working) HTTP request: https://api.apilayer.com/exchangerates_data/2022-03-03?base=USD
 NOTE: Any historical date larger than Y2K works in the above examples
 
# Risks
 - base URL now includes a level 1 path.  Not the best practice per se, but as long as every supported endpoint includes that full base URL + level 1 path, the risk is mitigated.  That holds true when checking the endpoint documentation located here https://apilayer.com/marketplace/exchangerates_data-api#endpoints
 
# Rollback steps
 - revert this branch