# first-drf-project
Learning DRF

rest coming soon!

Endpoints:

api/
Method = POST
title = charField(max length = 128,null allowed, blank allowed)
content = charField(null allowed, blank allowed)
price = DecimalField(default value =99.99)


api/products/
Method = GET
Response: all products in product table
'id',
'title',
'content',
'price',
'sale_price',
'my_cost'

api/products/
Method = POST
title = charField(max length = 128,null allowed, blank allowed)
content = charField(null allowed, blank allowed)
price = DecimalField(default value =99.99)

api/products/<int:id>/
Method = GET
Response: product with given id
'id',
'title',
'content',
'price',
'sale_price',
'my_cost'

api/products/<int:id>/update/
Method = PUT
Response: updated details of product with given id
'id',
'title',
'content',
'price',
'sale_price',
'my_cost'

api/products/<int:id>/delete/
Method = DELETE
Response: product with given id deleted