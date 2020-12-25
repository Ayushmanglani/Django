# Django

## Django Filters

 1. Fetching Data from any Model <br/>
    * **To Fetch a Single Record**        
    ```
    DataSet = Model.objects.get(id=id)
    ```
    &nbsp;&nbsp;&nbsp;&nbsp; To Access any value form Dataset:
        
    ```
    FieldValue = DataSet.FieldNameAsMentionedInModel
    ```
    <br/>
    
    * **To Fetch a Set of Record**
    ```
    DataSet = Model.objects.filter(id=id)
    ```
    &nbsp;&nbsp;&nbsp;&nbsp; To Access any value form Dataset:
        
    ```
    - FieldValue = DataSet[0]['FieldNameAsMentionedInModel']
    - FieldValue = DataSet.values('FieldName')
    - for Data in DataSet:
          print(Data.FieldName)
    ```
 
