import http.client, urllib.request, urllib.parse, urllib.error, base64 , json , io

def full_half(path):
    headers = {'Content-Type': 'multipart / form-data','Prediction-key': 'a23f7bca840c40cc9a051970f4bb386e',}
    params = urllib.parse.urlencode({'iterationId': '{9d5a9a69-bf5e-4895-8503-1b272eebdd48}',})
    F  =  open( path ,  "rb" ,  buffering = 0 )
    try:
        conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/customvision/v1.1/Prediction/06551202-b00b-4245-b24e-cbff5f1b4a15/image?%s" % params, F.readall(), headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return(summar(data))

def plain_strip(path):
    headers = {'Content-Type': 'multipart / form-data','Prediction-key': 'a23f7bca840c40cc9a051970f4bb386e',}
    params = urllib.parse.urlencode({'iterationId': '{29e7f8b1-3d73-42fe-b5a5-16b1bd92388b}',})
    F  =  open( path ,  "rb" ,  buffering = 0 )
    try:
        conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/customvision/v1.1/Prediction/797a5f91-1775-40f7-9e00-235e20e643dc/image?%s" % params, F.readall(), headers)
        response = conn.getresponse()
        data = response.read()
        #print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return(summar(data))

def tie_or_not(path):
    headers = {'Content-Type': 'multipart / form-data','Prediction-key': 'a23f7bca840c40cc9a051970f4bb386e',}
    params = urllib.parse.urlencode({'iterationId': '{e2438c60-2950-4f73-be63-daab1e8c0c7c}',})
    F  =  open( path ,  "rb" ,  buffering = 0 )
    try:
        conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/customvision/v1.1/Prediction/c991f808-8769-4787-b5d4-373b08fbed6b/image?%s" % params, F.readall(), headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return(summar(data))

def formal_casual(path):
    headers = {'Content-Type': 'multipart / form-data','Prediction-key': 'a23f7bca840c40cc9a051970f4bb386e',}
    params = urllib.parse.urlencode({'iterationId': '{41163edf-5f3c-4355-8c20-88205ebf890a}',})
    F  =  open( path ,  "rb" ,  buffering = 0 )
    try:
        conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/customvision/v1.1/Prediction/13159405-ad57-4eaa-9043-1df31a0e3f9a/image?%s" % params, F.readall(), headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return(summar(data))

def beard(path):
    headers = {'Content-Type': 'multipart / form-data','Prediction-key': 'a23f7bca840c40cc9a051970f4bb386e',}
    params = urllib.parse.urlencode({'iterationId': '{5fd5aaf1-f0a7-4121-a3c4-06fd1c950be1}',})
    F  =  open( path ,  "rb" ,  buffering = 0 )
    try:
        conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/customvision/v1.1/Prediction/3349d321-6d09-465a-80b4-c3e9797a0e6c/image?%s" % params, F.readall(), headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return(summar(data))

def shades(path):
    headers = {'Content-Type': 'multipart / form-data','Prediction-key': 'a23f7bca840c40cc9a051970f4bb386e',}
    params = urllib.parse.urlencode({'iterationId': '{d5c2f488-f8e4-400d-b95e-31d5af635cd6}',})
    F  =  open( path ,  "rb" ,  buffering = 0 )
    try:
        conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/customvision/v1.1/Prediction/4de07b05-71f6-4ba6-a95a-b98c337a705f/image?%s" % params, F.readall(), headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return(summar(data))

def summar(data):
    parsed = json.loads(data.decode("utf-8"))
    parsed=json.dumps(parsed, sort_keys=True, indent=4)
    d=json.loads(parsed)
    ll = []
    if 'Predictions' not in d:
        return(ll)
    else:
        predict=d["Predictions"]
        for i in range(len(predict)):
            ll.append({'prob' : predict[i]["Probability"], 'tag':predict[i]['Tag']})
        return(ll)