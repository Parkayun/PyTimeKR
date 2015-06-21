PyTimeKR
========

PyTimeKR은 `PyTime <https://github.com/shnode/PyTime>`__ 의 포크로 대한민국의 공휴일 등 을 추가하였습니다.

설치
-------

.. code:: python

    pip install pytimekr


간단 사용법
------------

.. code:: python

    >>>from pytimekr import pytimekr
    >>>
    >>>chuseok = pytimekr.chuseok()           # 추석
    >>>print chuseok
    datetime.date(2015, 9, 27)
    >>>
    >>>pytimekr.red_days(chuseok)             # 추석 연휴
    [datetime.date(2015, 9, 26),
     datetime.date(2015, 9, 27),
     datetime.date(2015, 9, 28),
     datetime.date(2015, 9, 29)]
    >>>
    >>>ly = pytimekr.lunar_newyear(1995)      # 1995년도 설날
    >>>print ly
    datetime.date(1995, 1, 31)

다른 공휴일

.. code:: python

    >>>pytimekr.hangul()                      # 한글날
    datetime.date(2015, 10, 9)
    >>>
    >>>pytimekr.children()                    # 어린이날
    datetime.date(2015, 5, 5)
    >>>
    >>>pytimekr.independence()                # 광복절
    datetime.date(2015, 8, 15)
    >>>
    >>>pytimekr.memorial()                    # 현충일
    datetime.date(2015, 6, 6)
    >>>
    >>>pytimekr.buddha()                      # 석가탄신일
    datetime.date(2015, 5, 25)
    >>>
    >>>pytimekr.samiljeol()                   # 삼일절
    datetime.date(2015, 3, 1)
    >>>
    >>>pytimekr.constitution()                # 제헌절
    datetime.datetime(2015, 7, 17)
    >>>
    >>>pytimekr.constitution()                # 제헌절
    datetime.datetime(2015, 7, 17)


License
-------

MIT
