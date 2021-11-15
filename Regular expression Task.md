# 2. Regular expressions

### 2.1 Write the python code that uses regular expressions to extract the numerical product count from the variable product_count_text below, and converts it to integer (int) format


```python
import re
product_count_text = "381 Products found"
product_count_int = int(re.match('\d+', product_count_text).group())
```


```python
product_count_int
```




    381



### 2.2 Write the python code that uses a single search pattern to extract the sequence of characters after the final "/", before the "-" character, in each url.


```python
import re

generic_urls = ["https://www.genericdomain.com/abc/def/1290aodwb23-ghi.img", "https://www.genericdomain.com/ab-c/31287bdwakj-jkl.img", "https://www.genericdomain.com/19unioawd02-jkl.img"]

for url in generic_urls:
    special_sequence = re.search('(?<=/)\d+\w+(?=-)', url).group()
    print(special_sequence)


```

    1290aodwb23
    31287bdwakj
    19unioawd02


### 2.3 Assume that you have extracted the below string from the ‘script’ tag of a web page. Use python regular expressions (i.e the ‘re’ library) to convert the string into a format that can be loaded via the python json library. I.e the below code should not throw any errors after the code is formatted properly.


```python
import json
import re
```


```python
product_storage_string_raw = '''
<script> 
var products_storage=[];
products_storage= [{"price":19.0,"name":"House & Home Hooded Blanket - Charcoal","id":"671282","position":1,"list":"Product Category - Level 2","category":"Home/Bedding/Blankets","brand":"House & Home"},{"price":5.0,"name":"House & Home 225TC Pillowcase -  Dance All Night - White","id":"649566","position":2,"list":"Product Category - Level 2","category":"Home/Bedding/Pillow Cases","brand":"House & Home"},{"price":59.0,"name":"House & Home Linen Cotton Quilt Cover Set - Frayed Edge - Charcoal - Queen","id":"659975","position":3,"list":"Product Category - Level 2","category":"Home/Bedding/Quilt Covers"},{"price":59.0,"name":"House & Home Linen Cotton Quilt Cover Set - Frayed Edge - Navy - Queen","id":"659976","position":4,"list":"Product Category - Level 2","category":"Home/Bedding/Quilt Covers","brand":"House & Home"},{"price":10.0,"name":"Tontine Winter Comfort Medium Pillow","id":"668702","position":5,"list":"Product Category - Level 2","category":"Home/Bedding/Pillows","brand":"Tontine"},{"price":15.0,"name":"House & Home Woven Cushion - Grey","id":"662158","position":6,"list":"Product Category - Level 2","category":"Home/Bedding/Pillows","brand":"House & Home"},{"price":25.0,"name":"House & Home Melange Plush Blanket - Grey Blue - Queen","id":"656994","position":7,"list":"Product Category - Level 2","category":"Home/Bedding/Blankets","brand":"House & Home"},{"price":24.0,"name":"House & Home Polar Fleece Sheet Set - Silver Grey","id":"BIGW659721","position":8,"list":"Product Category - Level 2","category":"Home/Bedding/Sheets","brand":"House & Home"},{"price":39.0,"name":"Incredibles Quilt Cover Set - Red - Single","id":"675844","position":9,"list":"Product Category - Level 2","category":"Home/Bedding/Kids Bedding","brand":"Disney"},{"price":27.0,"name":"House & Home Plain Blush Flannelette Sheet Set","id":"BIGW660776","position":10,"list":"Product Category - Level 2","category":"Home/Bedding/Sheets","brand":"House & Home"},{"price":89.0,"name":"House & Home Marilyne 7 Piece Comforter Set","id":"BIGW659777","position":11,"list":"Product Category - Level 2","category":"Home/Bedding/Comforters","brand":"House & Home"},{"price":39.0,"name":"House & Home Kids Foxy 180 Thread Count Comforter Set","id":"BIGW662598","position":12,"list":"Product Category - Level 2","category":"Home/Bedding/Comforters","brand":"House & Home Kids"},{"price":39.0,"name":"House & Home Kids Comforter Set - Dakota","id":"BIGW662602","position":13,"list":"Product Category - Level 2","category":"Home/Bedding/Comforters","brand":"House & Home Kids"},{"price":39.0,"name":"House & Home Kids Comforter Set - Xavier","id":"BIGW662604","position":14,"list":"Product Category - Level 2","category":"Home/Bedding/Comforters","brand":"House & Home Kids"},{"price":39.0,"name":"House & Home Kids Pia 180 Thread Count Comforter Set","id":"BIGW662606","position":15,"list":"Product Category - Level 2","category":"Home/Bedding/Comforters","brand":"House & Home Kids"},{"price":35.0,"name":"House & Home Waffle Blanket - Taupe - Queen","id":"429199","position":16,"list":"Product Category - Level 2","category":"Home/Bedding/Blankets","brand":"House & Home"},{"price":59.0,"name":"House & Home Blue Washed Pinstripe Coverlet - Queen","id":"660111","position":17,"list":"Product Category - Level 2","category":"Home/Bedding/Quilt Covers","brand":"House & Home"},{"price":9.0,"name":"Smart Value Quilt Cover Set - Iron Gate - King","id":"554307","position":18,"list":"Product Category - Level 2","category":"Home/Bedding/Quilt Covers"},{"price":9.0,"name":"Smart Value Quilt Cover Set - Iron Gate - Single","id":"554304","position":19,"list":"Product Category - Level 2","category":"Home/Bedding/Quilt Covers","brand":"Smart Value"},{"price":39.0,"name":"Trolls Quilt Cover Set - Pink - Single","id":"630753","position":20,"list":"Product Category - Level 2","category":"Home/Bedding/Kids Bedding","brand":"Trolls"},{"price":29.0,"name":"House & Home 225 TC Quilt Cover Set - Holly - Queen","id":"660472","position":21,"list":"Product Category - Level 2","category":"Home/Bedding/Quilt Covers","brand":"House & Home"},{"price":59.0,"name":"House & Home Faux Velvet Coverlet Set - Blush - Queen","id":"660200","position":22,"list":"Product Category - Level 2","category":"Home/Bedding/Quilt Covers","brand":"House & Home"},{"price":49.0,"name":"House & Home Queen Quilt Cover Set - Chambray - Light Blue - Queen","id":"659713","position":23,"list":"Product Category - Level 2","category":"Home/Bedding/Quilt Covers","brand":"House & Home"},{"price":49.0,"name":"House & Home Queen Quilt Cover Set - Chambray - Dusty Pink - Queen","id":"659714","position":24,"list":"Product Category - Level 2","category":"Home/Bedding/Quilt Covers","brand":"House & Home"}];
</script>'''
```


```python
product_storage_parsed = re.search('\[{.*}\]', product_storage_string_raw).group()
product_storage_json = json.loads(product_storage_parsed)
print(product_storage_json)
```

    [{'price': 19.0, 'name': 'House & Home Hooded Blanket - Charcoal', 'id': '671282', 'position': 1, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Blankets', 'brand': 'House & Home'}, {'price': 5.0, 'name': 'House & Home 225TC Pillowcase -  Dance All Night - White', 'id': '649566', 'position': 2, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Pillow Cases', 'brand': 'House & Home'}, {'price': 59.0, 'name': 'House & Home Linen Cotton Quilt Cover Set - Frayed Edge - Charcoal - Queen', 'id': '659975', 'position': 3, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Quilt Covers'}, {'price': 59.0, 'name': 'House & Home Linen Cotton Quilt Cover Set - Frayed Edge - Navy - Queen', 'id': '659976', 'position': 4, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Quilt Covers', 'brand': 'House & Home'}, {'price': 10.0, 'name': 'Tontine Winter Comfort Medium Pillow', 'id': '668702', 'position': 5, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Pillows', 'brand': 'Tontine'}, {'price': 15.0, 'name': 'House & Home Woven Cushion - Grey', 'id': '662158', 'position': 6, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Pillows', 'brand': 'House & Home'}, {'price': 25.0, 'name': 'House & Home Melange Plush Blanket - Grey Blue - Queen', 'id': '656994', 'position': 7, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Blankets', 'brand': 'House & Home'}, {'price': 24.0, 'name': 'House & Home Polar Fleece Sheet Set - Silver Grey', 'id': 'BIGW659721', 'position': 8, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Sheets', 'brand': 'House & Home'}, {'price': 39.0, 'name': 'Incredibles Quilt Cover Set - Red - Single', 'id': '675844', 'position': 9, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Kids Bedding', 'brand': 'Disney'}, {'price': 27.0, 'name': 'House & Home Plain Blush Flannelette Sheet Set', 'id': 'BIGW660776', 'position': 10, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Sheets', 'brand': 'House & Home'}, {'price': 89.0, 'name': 'House & Home Marilyne 7 Piece Comforter Set', 'id': 'BIGW659777', 'position': 11, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Comforters', 'brand': 'House & Home'}, {'price': 39.0, 'name': 'House & Home Kids Foxy 180 Thread Count Comforter Set', 'id': 'BIGW662598', 'position': 12, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Comforters', 'brand': 'House & Home Kids'}, {'price': 39.0, 'name': 'House & Home Kids Comforter Set - Dakota', 'id': 'BIGW662602', 'position': 13, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Comforters', 'brand': 'House & Home Kids'}, {'price': 39.0, 'name': 'House & Home Kids Comforter Set - Xavier', 'id': 'BIGW662604', 'position': 14, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Comforters', 'brand': 'House & Home Kids'}, {'price': 39.0, 'name': 'House & Home Kids Pia 180 Thread Count Comforter Set', 'id': 'BIGW662606', 'position': 15, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Comforters', 'brand': 'House & Home Kids'}, {'price': 35.0, 'name': 'House & Home Waffle Blanket - Taupe - Queen', 'id': '429199', 'position': 16, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Blankets', 'brand': 'House & Home'}, {'price': 59.0, 'name': 'House & Home Blue Washed Pinstripe Coverlet - Queen', 'id': '660111', 'position': 17, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Quilt Covers', 'brand': 'House & Home'}, {'price': 9.0, 'name': 'Smart Value Quilt Cover Set - Iron Gate - King', 'id': '554307', 'position': 18, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Quilt Covers'}, {'price': 9.0, 'name': 'Smart Value Quilt Cover Set - Iron Gate - Single', 'id': '554304', 'position': 19, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Quilt Covers', 'brand': 'Smart Value'}, {'price': 39.0, 'name': 'Trolls Quilt Cover Set - Pink - Single', 'id': '630753', 'position': 20, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Kids Bedding', 'brand': 'Trolls'}, {'price': 29.0, 'name': 'House & Home 225 TC Quilt Cover Set - Holly - Queen', 'id': '660472', 'position': 21, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Quilt Covers', 'brand': 'House & Home'}, {'price': 59.0, 'name': 'House & Home Faux Velvet Coverlet Set - Blush - Queen', 'id': '660200', 'position': 22, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Quilt Covers', 'brand': 'House & Home'}, {'price': 49.0, 'name': 'House & Home Queen Quilt Cover Set - Chambray - Light Blue - Queen', 'id': '659713', 'position': 23, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Quilt Covers', 'brand': 'House & Home'}, {'price': 49.0, 'name': 'House & Home Queen Quilt Cover Set - Chambray - Dusty Pink - Queen', 'id': '659714', 'position': 24, 'list': 'Product Category - Level 2', 'category': 'Home/Bedding/Quilt Covers', 'brand': 'House & Home'}]



```python

```
