import os

def encrypt(file):
   st = os.stat(file)
   file_len = st.st_size
   fp = open(file)
   fp = fp.readlines()
   file_block = []
   for i in range(len(fp)):
      for j in range(len(fp[i])):
         file_block.append(fp[i][j])
   cipher = []
   for i in range(file_len%128):
      cipher[i].append(AES(file_block[i]))

   return cipher