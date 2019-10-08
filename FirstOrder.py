import requests
response = requests.get(
    "https://zvlhch4ygd.execute-api.eu-west-1.amazonaws.com/production/challenge")
SplittedResponse = response.text.split('-->')
exec("liste = " + SplittedResponse[0])
#print(liste)

numericalOrder = []
alphapeticalOrder = []
for i in liste:
    if i.isnumeric():
        numericalOrder.append(int(i))
    else:
        alphapeticalOrder.append(i)
numericalOrder = sorted(numericalOrder)
alphapeticalOrder = sorted(alphapeticalOrder)
FinalSortedList = ""
if SplittedResponse[1].split(' ')[0] == 'Words':
    FinalSortedList = alphapeticalOrder + numericalOrder
else:
    FinalSortedList = numericalOrder + alphapeticalOrder
print(FinalSortedList)

response = requests.post("https://zvlhch4ygd.execute-api.eu-west-1.amazonaws.com/production/challenge",
                         json={'answer': str(FinalSortedList)})
print(response.text)
