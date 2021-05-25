
#sleep
def cronus(t,text=''):
   s = t
   while(True):
      #f = t
      m = (s // 60)
      mRest = s%60
      h = (m // 60)
      hRest = m%60
      print(f' {h} horas :{m} min :{mRest} seg',text)
      tm.sleep(1)
      s -= 1
      if(s==-1):
         break
