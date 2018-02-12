from django.shortcuts import render
from django.http.response import JsonResponse
from .form import imageFORM,FileFieldForm
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .files import final
import http.client, urllib.request, urllib.parse, urllib.error, base64 , json , io
from django.views.generic.edit import FormView
def image(path):
    headers = {
    # Request headers
    'Content-Type': 'multipart / form-data',
    'Prediction-key': 'a23f7bca840c40cc9a051970f4bb386e',
    }
    params = urllib.parse.urlencode({
    # Request parameters
    'iterationId': '{4c8c1b0c-a721-4361-b4dc-77d7dad66419}',
    })
    F  =  open( path ,  "rb" ,  buffering = 0 )
    try:
        conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/customvision/v1.1/Prediction/3349d321-6d09-465a-80b4-c3e9797a0e6c/image?%s" % params, F.readall(), headers)
        response = conn.getresponse()
        data = response.read()
        #print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    parsed = json.loads(data.decode("utf-8"))
    parsed = json.dumps(parsed, sort_keys=True, indent=4)
    d = json.loads(parsed)
    predict = d["Predictions"]
    ll = []
    for i in range(len(predict)):
        ll.append({'prob': predict[i]["Probability"], 'tag': predict[i]['Tag']})
    return (ll)

# def index(request):
#     if request.method == 'POST':
#         form = imageFORM(request.POST, request.FILES)
#         if 'submit' in request.POST:
#             if form.is_valid():
#                 form.save()
#             else:
#                 return HttpResponseRedirect('/beard/')
#
#     else:
#         form = imageFORM()
#     return render(request,'index.html',{'form':form})

def index(request):
    if request.method == 'POST' and request.FILES:
        myfile = request.FILES.getlist('myfiles')
        l=list()
        for i in myfile:
            fs = FileSystemStorage()
            filename = fs.save(i.name, i)
            uploaded_file_url = fs.path(filename)
            l.append([final.predict(uploaded_file_url),'/media/'+str(i.name)])
        # if tt[0]['prob'] >= 0.75:
        #     tmp.append(tt[0]['tag'])
        return render(request, 'index.html', {'l':l})
    return render(request, 'index.html')

# class index(FormView):
#     form_class = FileFieldForm
#     template_name = 'index1.html'  # Replace with your template.
#     success_url = '/beard/'  # Replace with your URL or reverse().
#
#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')
#         if form.is_valid():
#             for f in files:
#                 ...  # Do something with each file.
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)


def index1(request):
    return JsonResponse({'int':'iint'})
