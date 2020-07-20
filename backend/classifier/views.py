from django.shortcuts import render
from django.http import JsonResponse
import json
from backend import database
from django.views.decorators.csrf import csrf_exempt


def index(request):
    conn = database.connectDatabase()
    result = dict()
    if conn == None:
        
        result['status'] = 'Connection Error'
    else:
        result['status'] = 'Connection Successful'
    return JsonResponse({'message':result})

def firstfewfecords(request):
    conn = database.connectDatabase()

    cursor = conn.cursor()

    query = '''select UNSPSC_Code, Commodity_Title, sum(AUD_Invoice_Line_Amount_ex_Tax) as Spend from marsh_main
        group by UNSPSC_Code, Commodity_Title  limit 100 '''

    cursor.execute(query)

    records = dict()
    counter = 1

    for UNSPSC_Code, Commodity_Title, Spend in cursor.fetchall():
        records[counter] = {'code':UNSPSC_Code, 'title':Commodity_Title, 'spend': Spend}
        counter = counter + 1
    
    return JsonResponse({'data':records}, json_dumps_params = {'indent':2})
@csrf_exempt
def insertData(request):
    print("Angular Request = ", request.body)
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    username = body['username']  
    print(username)
    password = body['password'] 
    print(password)
    conn = database.connectDatabase()
    cursor = conn.cursor()
    query = f"select user_id, first_name, last_name, email, password from users where email = '{username}' and password = '{password}'"
    
    

    cursor.execute(query)
    

    loginResponse = []
    for user_id, firstname, lastname, email, password in cursor.fetchall():
        loginResponse.append({'user_id': user_id,'email':email, 'password':password, 'firstname':firstname, 'lastname':lastname})
    print(loginResponse)
    return JsonResponse({'data':loginResponse}, json_dumps_params = {'indent':2})

    





