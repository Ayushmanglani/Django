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
    
 2. Applying SQL Query on Django Model  
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
 
 3. Inner Join on two Django Model  
     * First Step is to Declare ForeignKey in Main Model, which is primary key in another Model
    ```
    class Model2(models.Model):
        id = models.IntegerField(primary_key=True)
   
    class Model1(models.Model):
        id = models.IntegerField(primary_key=True)
        emp_id = models.ForeignKey(Model2, on_delete=models.DO_NOTHING)
    ```
    &nbsp;&nbsp;&nbsp;&nbsp; Methods to Access any value form Dataset:
