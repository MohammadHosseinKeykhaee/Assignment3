#second to hour converter
converter_op =str(input(' sh = second to hour ,  hs= hour to second :'))
if converter_op =="sh":
  sec=int(input('please Enter seconds:'))
  second=(sec%3600)%60
  minute=(sec%3600)//60
  hour=sec//3600
  print('%.2d :%.2d :%.2d'%(hour,minute,second))
elif converter_op=="hs":
  hour=int(input('please enter hour :'))
  minute=int(input('please enter minute:'))
  second=int(input('please enter second:'))
  print('%.2d :%.2d :%.2d'%(hour,minute,second))
  ms=minute*60     #minute to second
  hs=hour*3600   # hour to second
  total = ms + hs
  print('seconds:',total)