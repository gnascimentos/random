Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> valorhora=4
>>> diasdetrabalho=30
>>> horasdetrabalho=8
>>> vencimentomensal=valorhora*horasdetrabalho*diasdetrabalho
>>> nome="tiago"
>>> print(valorhora)
4
>>> print(vencimentomensal)
960
>>> print(nome)
tiago
>>> print(nome,vencimentomensal)
tiago 960
>>> print(nome,"+",vencimentomensal)
tiago + 960
>>> print(nome,">>",vencimentomensal)
tiago >> 960
>>> float(valorhora)
4.0
>>> int(10,5)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    int(10,5)
TypeError: int() can't convert non-string with explicit base
>>> int(10.5)
10
>>> str(valorhora)
'4'
