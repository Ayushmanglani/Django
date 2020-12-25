# Django

## Django Filters

 1. Fetching Data from any Model <br/>
    * **To Fetch a Single Record**        
    ```
    DataSet = Model.objects.get(id=id)
    ```
    &nbsp;&nbsp;&nbsp;&nbsp; Methods to Access any value form Dataset:
        
    ```
    FieldValue = DataSet.FieldNameAsMentionedInModel
    ```
    <br/>
    
    * **To Fetch a Set of Records**
    ```
    DataSet = Model.objects.filter(id=id)
    ```
    &nbsp;&nbsp;&nbsp;&nbsp; Methods to Access any value form Dataset:
        
    ```
    - FieldValue = DataSet[0]['FieldNameAsMentionedInModel']
    - FieldValue = DataSet.values('FieldName')
    - for Data in DataSet:
          print(Data.FieldName)
    - return DataSet.data
    ```
    
 2. Applyin SQL Query on Django Model  
     * **To Fetch Records using SQL Query we can Use 'Raw' Keyword on Model** 
    ```     
    DataSet = DModel.objects.raw('query')
    ```
    &nbsp;&nbsp;&nbsp;&nbsp; Methods to Access any value form Dataset:
        
    ```
    - FieldValue = DataSet[0].FieldName
    - for Data in DataSet:
         print(Data.FieldName)
    ```
 
