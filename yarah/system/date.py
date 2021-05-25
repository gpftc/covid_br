
#data
def date():
  from datetime import datetime as dt
  dt = dt.now()
  return dt.strftime('%d/%m/%Y %H:%M:%S')
