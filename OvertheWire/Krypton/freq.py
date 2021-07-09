from collections import Counter
import string


def readfile():
 data = []
 try:
  #Open informatic file
  f1 = open("/home/leaundre/Projects/Github/ctf/OvertheWire/Krypton/found1", "r")
  f2 = open("found2", 'r')
  f3 = open("found3", 'r')
  f4 = open("krypton4", 'r')
  # Read contain
  data.append(f1.read())
  data.append(f2.read())
  data.append(f3.read())
  data.append(f4.read())

  # Close file
  f1.close()
  f2.close()
  f3.close()
  f4.close()
 except:
  print("Error when reading file")

 return data


def analystfre(data):
    combinedata = ''.join(data[:-2])
    counter = Counter(combinedata)
    print("===========Counter ============== \n")
    print(counter)


data = readfile()
analystfre(data)

cipher = data[3].replace(' ', '')
intab = 'JDSQNVIKWBAGXFMYUCA'
outab = 'THEARLVWDOBNFKOPSIB'
print("Original data \n %s") % cipher
tran = str.translate(intab, outab)
print("Decrypt data \n %s") % cipher.translate(tran)
