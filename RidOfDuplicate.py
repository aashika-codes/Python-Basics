student_data={'id1':
              {'name':['Jess'],
                  'class':['VI'],
                  'subject':['english,maths,science']
              },
'id2':
{'name':['Glynn'],
'class':['VI'],
'subject':['english,maths,science']
},
'id3':
{'name':['Jess'],
'class':['VI'],
'subject':['english,maths,science']
},
'id4':
{'name':['Avika'],
'class':['VI'],
'subject':['english,maths,science']
}}
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)