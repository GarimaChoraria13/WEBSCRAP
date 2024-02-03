import string

file_path="C:\\Nexthike\\Web Scrapping\\python_article.txt"
with open(file_path,'r')as file:
    file_content=file.read()
    print(file_content)


if file_content:
      translator=str.maketrans(" "," ",string.punctuation)
      clean_text=file_content.translate(translator).lower()
      words=clean_text.split()
      word_frequency={}
      for word in words:
            word_frequency[word]=word_frequency.get(word,0)+1
      print('word frequency:')  
      for word,count in word_frequency.items():
            print(word,count)
else:
      print('fail to read file')    

     
