choice = input('Type a sentence😊 :   ').split()
from PIL import ImageTk,Image
sentence = choice[::-1]
sen = " ".join(sentence)
print(sen)  