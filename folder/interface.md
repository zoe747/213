# 请求根目录id与名称
******
## 请求(POST)
请求链接：folder/get_first_folder

无参数
## 返回值(http状态码+(列表))
200+列表:成功+根目录名称与id列表

400:请求不合法

# 请求根目录下所有文件
******
## 请求(POST)
请求链接：folder/folder_list

folder_id(群号)
## 返回值(http状态码+(列表))
200:返回目录下所有文件与id

400:请求不合法

# 请求新建文件夹
******
## 请求(POST)
请求链接：folder/add_folder/

father_folder_id(父节点id)
folder_name(节点名称)
## 返回值(http状态码+列表)
200:创建成功

422:此文件夹不存在

400:请求不合法

# 删除文件夹
******
## 请求(POST)
请求链接:folder/delete_folder

folder_id(文件夹id)
## 返回值(http状态码)
200:成功

400:请求不合法

421:无此文件夹


