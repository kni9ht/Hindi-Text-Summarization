from googletrans import Translator
from summarizer import textrank

f=open('HindiText.txt','r')
hinText=f.read()
f.close()
translator = Translator()
engText=translator.translate(hinText,src='hi',dest='en')
engSum=textrank(engText.text)

for sentence in engSum:
	hinSent=Translator().translate(sentence,src='en',dest='hi')	
	temp=hinSent.text	
	f=open('HindiSum.txt','ab')
	f.write(temp.encode('utf-8'))
	f.close()


		
