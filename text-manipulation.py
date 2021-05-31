#!/usr/bin/env python
# Solution taken from stackoverflow thread and modified to print entire hostname as opposed to just "docker":
# https://stackoverflow.com/questions/51567427/find-specific-words-in-text-file-and-print-the-line-using-python/51567512 

def my_function():


    with open("/etc/hosts",'r') as f: # Removed unnecessary output file
      text = f.read()
      result_string = ''

      words = ["docker"]
      text2 = text.split() # - Changed from (".") to ()
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
# Removed unnecessary secondary result output
my_function()