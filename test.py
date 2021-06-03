from dadata import Dadata

token = "c617ffb867af8b7d0d8f1579d1d11a2fdc5ad4c0"
dadata = Dadata(token)
result = dadata.find_by_id("party", "2345001369")
print(result[0]['data']['name']['full_with_opf'])
print(result[0]['data']['type'])
print('Руководитель:'+result[0]['data']['management']['name'] +' Пост: '+ result[0]['data']['management']['post'])
print(result)
