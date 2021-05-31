#!/usr/bin/env python
def my_function():


    with open("/etc/hosts",'r') as f:
      text = f.read()
      result_string = ''

      words = ["docker"]
      text2 = text.split()
      for itemIndex in range(len(text2)):
          for word in words:
              if word in text2[itemIndex]:
                  if text2[itemIndex][0] ==' ':
                      print(text2[itemIndex][1:])
                      break
                  else:
                      print(text2[itemIndex])
                      break
      print(result_string)

my_function()