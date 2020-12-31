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
    DataSet = Model.objects.raw('query')
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
        key_id = models.ForeignKey(Model2, on_delete=models.DO_NOTHING)
    ```
     * Then use ```select_related``` keyword on Main model, pass foreign key inside select_related (optional)
     
     ```
     DataSet = Model1.objects.filter(filters).select_related("key_id")     
     ```
     &nbsp;&nbsp;&nbsp;&nbsp; This will return all field and values included in both the Models
     
     &nbsp;&nbsp;&nbsp;&nbsp; Methods to Access values:
     ```
     - FieldValue = DataSet[0].FieldName
     - for Data in DataSet:
          print(Data.FieldName)    # To get Data from Model1
          print(Data.key_id.FieldName)       # To get Data from Model2
     - return DataSet.data   # This will return Data of Model1 Only (Not Prefered)         
     ```
 4. Dynamic filters on any ORM Model
     * Create a python dictionary with a 'key' as a field to look with a parameter(optional) for it (i.e key__in , key__icontains, key) and a value to search
 in the field.  

     ```
     - filters = {}
       filters['name__icontains'] = 'A'
       filters['id'] = '05'
       filters['age__in'] = [5,10,15,20,15]
     ```
     &nbsp;&nbsp;&nbsp;&nbsp; Pass this filter dictionary to ORM as:
     ```
     - DataSet = Model.objects.filter(**filters)
     ```     
