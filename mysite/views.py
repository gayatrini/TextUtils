# I have created this page
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    # assign user input ,what user want
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    capfirst = request.POST.get('capfirst','off')
    newlineremove = request.POST.get('newlineremove','off')
    extraspaceremove = request.POST.get('extraspaceremove','off')
    charcount = request.POST.get('charcount','off')

    if removepunc == 'on':
        punctuations = '''.,?:;"'-_/\[]~`!@#$%^&*(<>)|'''
        analysed = ''
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char

        params = {'purpose':'Removed Punctuation','analysed_text':analysed}
        djtext = analysed
    
    if newlineremove == 'on':
        analysed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analysed = analysed + char

        params = {'purpose':'New line Remove','analysed_text':analysed}
        djtext = analysed
    
    if capfirst == 'on':
        analysed = ''
        for char in djtext:
            analysed = analysed + char.upper()

        params = {'purpose':'UPPERCASE TEXT','analysed_text':analysed}
        djtext = analysed
    
    if extraspaceremove == 'on':
        analysed = ''
        for index,char in enumerate(djtext):
            if (djtext[index]!=' ' and djtext[index+1]!=' '):
                analysed = analysed + char.upper()

        params = {'purpose':'Extra Space Remove','analysed_text':analysed}
        djtext = analysed
    
    if charcount == 'on':
        analysed = len(djtext)
        params = {'purpose':'Character Count','analysed_text':analysed}

    if removepunc !='on' and newlineremove !='on' and charcount !='on' and capfirst != 'on' and extraspaceremove != 'on' :
        return HttpResponse('Error,please enter some operation,and then try again.')
    
    return render(request,'analyze.html',params)  
