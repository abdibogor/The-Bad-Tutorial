Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:25:23) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import time
>>> time.time()
1554300089.47716
>>> time.time()
1554300133.704677
>>> time.localtime(time.time())
time.struct_time(tm_year=2019, tm_mon=4, tm_mday=3, tm_hour=17, tm_min=2, tm_sec=32, tm_wday=2, tm_yday=93, tm_isdst=0)
>>> time.asctime()
'Wed Apr  3 17:04:08 2019'
>>> mytuple=(1993,4,6,15,23,15,0,0,0)
>>> time.mktime(mytuple)
734098995.0
>>> time.localtime(time.mktime(mytuple))
time.struct_time(tm_year=1993, tm_mon=4, tm_mday=6, tm_hour=15, tm_min=23, tm_sec=15, tm_wday=1, tm_yday=96, tm_isdst=0)
>>> 
