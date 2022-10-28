
filename1 = open ('/Users/maruthu/Desktop/BUG/Tools/tempomail/mails/65348018','r')
import re
strValue= filename1.read()
start = 'activation/'
end = '?'
# patern = ".*" + ch
before,sep,after = strValue.partition(start)
# start word
if len (after) > 0:
    strValue = after
    strValue = strValue
    if len (after) > 0:
#end word
        before,sep,after = strValue.partition(end)
        strValue = before
    
print("Message:",strValue)
