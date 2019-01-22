from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']  # 입력받는 텍스트를 fulltext라고 이름 지었음
    # text에 받은 내용이 문자열로 저장됨
    words = text.split() # string=split() : 공백을 나눠 리스트에 넣어줌
    word_dictionary = {}

    for word in words: # (words:리스트 이름, word:반복문 안의 변수)
        if word in word_dictionary: # 단어가 dictionary안에 있으면,
            word_dictionary[word]+=1 # value값을 1씩 증가시켜라
        else: # 단어가 dictionary 안에 있지 않다면
            # add to dictionary
            word_dictionary[word] = 1 # value값을 1로 주어라


    return render(request, 'result.html', {'full': text, 'total' : len(words), 'dictionary' : word_dictionary.items()}) # 세번째 인자는 dictionary형, key : full이라는 이름, value : text 값 (key는 value를 대표)