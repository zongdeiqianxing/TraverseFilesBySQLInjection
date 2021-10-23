# FileReader
基于sqlmap的sql注入漏洞中遍历文件是否存在的脚本/Script to traverse whether the file exists in the sql injection vulnerability based on sqlmap


## usage
需要注意，在盲注时如果开启多线程会导致不稳定  
It should be noted that if multi-threading is enabled during blind injection, it will cause instability
```
usage: test2.py [-h] [-u URL | -r HEADERS_DATA] [-w FILE] [-t THREADS]

By zongdeiqianxing; Email: jshahjk@163.com

optional arguments:
  -h, --help       show this help message and exit
  -u URL
  -r HEADERS_DATA  HTTP request header
  -w FILE          wordlist containing file path
  -t THREADS       threads count
```

## show
```
$ python3 TraverseFilesBySQLInjection.py -r 1.txt -w linux.txt 
2021-10-23 23:01:51,211 - __main__ - INFO - The program has been started, if found readable files, it will be displayed, please wait..
2021-10-23 23:02:21,234 - __main__ - INFO - /etc/hosts file exists
2021-10-23 23:02:41,058 - __main__ - INFO - /etc/hostname file exists
2021-10-23 23:03:00,863 - __main__ - INFO - /etc/passwd file exists
```
