csv to xlsx converter using a function app
file is converted with a post http request to the azure function url endpoint 

http post request 
json body 
    {
      "csv_file":"csv file (base64)"
                                      }
Developer's note
Follow guidelines how to setup azure function with python here : https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python
