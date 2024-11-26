
from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse("hello World!")
    
def listComprehension():
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    clist=[x for x in fruits if 'a' in x]
    print(clist)

def asynchronous():
    for i in range(5):
        print(i)     
# asynchronous()
# listComprehension()
def members(request):
    mydic = {
        "COOKIES": request.COOKIES,
        "FILES": request.FILES,
        "GET": request.GET,
        "META": request.META,
        "POST": request.POST,
        "__class__": request.__class__,
        "__delattr__": request.__delattr__,
        "__dict__": request.__dict__,
        "__dir__": request.__dir__,
        "__doc__": request.__doc__,
        "__eq__": request.__eq__,
        "__firstlineno__": request.__firstlineno__,
        "__format__": request.__format__,
        "__ge__": request.__ge__,
        "__getattribute__": request.__getattribute__,
        "__getstate__": request.__getstate__,
        "__gt__": request.__gt__,
        "__hash__": request.__hash__,
        "__init__": request.__init__,
        "__init_subclass__": request.__init_subclass__,
        "__iter__": request.__iter__,
        "__le__": request.__le__,
        "__lt__": request.__lt__,
        "__module__": request.__module__,
        "__ne__": request.__ne__,
        # "__new__": request.__new__,
        "__reduce__": request.__reduce__,
        "__reduce_ex__": request.__reduce_ex__,
        "__repr__": request.__repr__,
        "__setattr__": request.__setattr__,
        "__sizeof__": request.__sizeof__,
        "__static_attributes__": request.__static_attributes__,
        "__str__": request.__str__,
        "__subclasshook__": request.__subclasshook__,
        "__weakref__": request.__weakref__,
        "_current_scheme_host": request._current_scheme_host,
        "_encoding": request._encoding,
        "_get_full_path": request._get_full_path,
        "_get_post": request._get_post,
        "_get_raw_host": request._get_raw_host,
        "_get_scheme": request._get_scheme,
        "_initialize_handlers": request._initialize_handlers,
        "_load_post_and_files": request._load_post_and_files,
        "_mark_post_parse_error": request._mark_post_parse_error,
        "_messages": request._messages,
        "_read_started": request._read_started,
        "_set_content_type_params": request._set_content_type_params,
        "_set_post": request._set_post,
        "_stream": request._stream,
        "_upload_handlers": request._upload_handlers,
        "accepted_types": request.accepted_types,
        "accepts": request.accepts,
        "auser": request.auser,
        "body": request.body,
        "build_absolute_uri": request.build_absolute_uri,
        "close": request.close,
        "content_params": request.content_params,
        "content_type": request.content_type,
        "csrf_processing_done": request.csrf_processing_done,
        "encoding": request.encoding,
        "environ": request.environ,
        "get_full_path": request.get_full_path,
        "get_full_path_info": request.get_full_path_info,
        "get_host": request.get_host,
        "get_port": request.get_port,
        "get_signed_cookie": request.get_signed_cookie,
        "headers": request.headers,
        "is_secure": request.is_secure,
        "method": request.method,
        "parse_file_upload": request.parse_file_upload,
        "path": request.path,
        "path_info": request.path_info,
        "read": request.read,
        "readline": request.readline,
        "readlines": request.readlines,
        "resolver_match": request.resolver_match,
        "scheme": request.scheme,
        "session": request.session,
        "upload_handlers": request.upload_handlers,
        "user": request.user,
    }
    return mydic


def test(mydic):
    for i in mydic.values():
        print(i)


def printListToFile(data):
    with open(r'output2.txt', 'w') as write:
        try:
            iter(data)
        except TypeError:
            write.write(str(data))
        else:
            for x in data:
                write.write(x)


def openTxtFile(path):
    import subprocess
    command = "\"C:/Program Files/Notepad++/notepad++.exe\""+" "+path
    subprocess.Popen(command)
    print('writting done!')
def getFileLines(path):
    with open(path,'r') as read:
        lines=read.readlines()
        return lines
def compareTwoFiles(file1,file2):
    differs=[]
    if len(file1)>len(file2):
        bigf=file1
        smlf=file2
    else:
        bigf=file2
        smlf=file1
 
    for l in bigf:
        if smlf.count(l)<1:
            differs.append(l)
    return differs
# h ='A'
# file1=r'third-party modules.txt'
# file2=r'built-in python modules (no_).txt'
# file1=getFileLines(file1)
# file2=getFileLines(file2)

# differ=compareTwoFiles(file1,file2)
# print(len(differ))
# printListToFile(differ)
# openTxtFile('output2.txt')
# from django.apps import apps
# aps=apps.all_models()
# print(type(aps))