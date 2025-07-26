# Azure Function app to convert csv to xlsx </br>
## Setup and configure azure function 
[MS Documentation to setup function app with python](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python) </br>

## File Conversion 
App converts a base 64 csv file to a base 64 xlsx file
## Post Request
body</br>
```json
{
"csv_file":"<bas64csvfile>"
                            }
```

