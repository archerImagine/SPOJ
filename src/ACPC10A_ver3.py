while True:
 try :
  test=raw_input()
  test=test.split()
  x=[int(i) for i in test]
  if x[0]==0 and x[1]==0 and x[2]==0:
    break
  d1=x[1]-x[0]
  d2=x[2]-x[1]
  if (x[2] - x[1]) == (x[1] - x[0]):
    print "AP",
    print x[2] + (x[2] - x[1])
  else:
    print "GP",
    print x[2]*x[2]/x[1]
 except:
  break


