from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

def form_link(title,questions):
    
    SCOPES = "https://www.googleapis.com/auth/drive"
    DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

    store = file.Storage('token.json')
    creds = None
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
        creds = tools.run_flow(flow, store)

    form_service = discovery.build('forms', 'v1', http=creds.authorize(
        Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

    form = {
        "info": {
            "title": title,
        },
    }
    result = form_service.forms().create(body=form).execute()
    i=0
    j=-1
    while(i<len(questions)):
        if(questions[i][0]=='#'):
            j+=1
            update = {    
                 "requests":[
                     {
                         "createItem":{
                             "item": {
                                 "itemId":str(j),
                                 "title":questions[i][1:],
                                 "questionItem": {
                                     "question":{
                                         "questionId":str(j),
                                         "required": True,
                                         "choiceQuestion":{
                                            "type": "RADIO",
                                            "options": [
                                                {"value":"a"},
                                                {"value":"b"}
                                            ]
                                         }
                                     }
                                 }
                             },
                             "location":{
                                 "index": j
                             }
                         }
                     }
                 ]
            }
            question_setting = form_service.forms().batchUpdate(formId=result["formId"], body=update).execute()
            i+=1
        
        else:
            temp=[]
            while(i < len(questions) and questions[i][0]!='#'):
                  temp.append({"value": questions[i]})
                  i+=1
            
            update = {    
                 "requests":[
                     {
                         "updateItem":{
                             "item": {
                                 "itemId":str(j),
                                 "questionItem": {
                                     "question":{
                                         "questionId":str(j),
                                         "choiceQuestion": {
                                            "type": "RADIO",
                                            "options": temp
                                        }
                                     }
                                 }
                             },
                             "updateMask":"questionItem",
                             "location":{
                                 "index": j
                             }
                         }
                     }
                 ]
            }
            question_setting = form_service.forms().batchUpdate(formId=result["formId"], body=update).execute()

    return(result["responderUri"])