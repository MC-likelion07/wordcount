from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')  # render - 세 개의 인자를 받을 수 있음.
    #render() 함수는 request 객체를 첫번째 인수로 받고, 
    #template 이름을 두번째 인수로 받으며, context 사전형 객체를 세전째 선택적(optional) 인수로 받는다

def about(request):
    return render(request, 'about.html')

def result(request):
    email = request.GET['email_address']
    text = request.GET['fulltext'] # 12번째 줄의 코드가 home의 textarea코드와 짝을 이룬다. 
    #textarea에 입력된 값 전체를 의미한다.
    words = text.split() # home.html의 textarea에 입력된 값 전체를 띄어쓰기 단위로 나누어 리스트에 저장한 값
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            # add to dictionary
            word_dictionary[word] = 1

    return render(request, 'result.html', {'e_mail':email, 'full':text ,'total' : len(words), 'dictionary':word_dictionary.items()})
    #.items는 딕셔너리 자료형에 저장된 쌍들을 보내주는 또다른 파이썬 상의 문법. 