Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:25:23) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Hello World!
>>> ================================ RESTART ================================
>>> 
Hello World!
>>> import calendar
>>> print(calendar.month(1965,3))
     March 1965
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31

>>> print(calendar.calendar(1994,2,1,10))
                                      1994

      January                       February                       March
Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su
                1  2              1  2  3  4  5  6              1  2  3  4  5  6
 3  4  5  6  7  8  9           7  8  9 10 11 12 13           7  8  9 10 11 12 13
10 11 12 13 14 15 16          14 15 16 17 18 19 20          14 15 16 17 18 19 20
17 18 19 20 21 22 23          21 22 23 24 25 26 27          21 22 23 24 25 26 27
24 25 26 27 28 29 30          28                            28 29 30 31
31

       April                          May                           June
Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su
             1  2  3                             1                 1  2  3  4  5
 4  5  6  7  8  9 10           2  3  4  5  6  7  8           6  7  8  9 10 11 12
11 12 13 14 15 16 17           9 10 11 12 13 14 15          13 14 15 16 17 18 19
18 19 20 21 22 23 24          16 17 18 19 20 21 22          20 21 22 23 24 25 26
25 26 27 28 29 30             23 24 25 26 27 28 29          27 28 29 30
                              30 31

        July                         August                      September
Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su
             1  2  3           1  2  3  4  5  6  7                    1  2  3  4
 4  5  6  7  8  9 10           8  9 10 11 12 13 14           5  6  7  8  9 10 11
11 12 13 14 15 16 17          15 16 17 18 19 20 21          12 13 14 15 16 17 18
18 19 20 21 22 23 24          22 23 24 25 26 27 28          19 20 21 22 23 24 25
25 26 27 28 29 30 31          29 30 31                      26 27 28 29 30

      October                       November                      December
Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su
                1  2              1  2  3  4  5  6                    1  2  3  4
 3  4  5  6  7  8  9           7  8  9 10 11 12 13           5  6  7  8  9 10 11
10 11 12 13 14 15 16          14 15 16 17 18 19 20          12 13 14 15 16 17 18
17 18 19 20 21 22 23          21 22 23 24 25 26 27          19 20 21 22 23 24 25
24 25 26 27 28 29 30          28 29 30                      26 27 28 29 30 31
31

>>> calendar.isleap(2008)
True
>>> calendar.isleap(2009)
False
>>> 
