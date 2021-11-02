# 上传文件
******
## 请求(POST)
请求链接：file/upload_file

file_path(文件路径)
folder_id（文件夹id）
文件
## 返回值(http状态码+(列表))
200：成功

400:请求不合法

# 下载文件
******
## 请求(POST)
请求链接：file/download_file

file_path(文件路径)
## 返回值(文件)
200:返回文件

400:请求不合法

# 删除文件
******
## 请求(POST)
请求链接：file/delete_file

file_path(文件路径)
file_id(文件id)
## 返回值(http状态码+列表)
200:创建成功

421:此文件不存在

400:请求不合法

