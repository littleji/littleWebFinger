# littleWebFinger
based on  [TideFinger](https://github.com/TideSec/TideFinger) web app cms  fingerprint scaner.

# How to use

```
$ python littlejiFinger.py

    Usage: python littlejiFinger.py -u http://www.123.com [-p 1] [-m 50] [-t 5]

    -u: URL 
    -p: When specifying this option to 1,  proxy detection will be enabled. Please ensure that the proxy file "proxys_ips.txt", with one proxy per line, in the format: 124.225.223.101:80
    -m: thread number, default number is 50
    -t: await time for the website's response, default time is 5 seconds
```



