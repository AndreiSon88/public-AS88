import json
with open('to_json_example.json',encoding='utf8') as f:
    templates = json.load(f)

def CheckInt(item):
    return isinstance(item,int)
def CheckStr(item):
    return isinstance(item,str)
def CheckBool(item):
    return isinstance(item,bool)
def CheckUrl(item):
    if isinstance(item,str):
        return item.startswith('http://') or item.startswith('http://')
    else:
        return False
def CheckStrValue(item,val):
    if isinstance(item, str):
        return item in val
    else:
        return False
def ErrorLog(item, value, string):
    Error.append({item: f'{value},{string}'})
listOfItems ={'timestamp' : 'int','item_price' : 'int', 'referer' : 'url', 'location' : 'url', 'item_url' : 'url',
              'remouteHost':'str','partyId':'str','sessionId':'str','pageViewId':'str','item_id':'str',
              'basket_price':'str','userAgentName':'str','eventType':'val','detectedDuplicate':'bool',
              'detectedCorruption':'bool','fistInSession':'bool'}
Error = []
for items in templates:
    for item in items:
        if item in listOfItems:
            if listOfItems[item] == 'int':
                if not CheckInt(items[item]):
                    ErrorLog(item,items[item],f'ожидали тип {listOfItems[item]}')
            elif listOfItems[item] =='str':
                if not CheckStr(item[item]):
                    ErrorLog(item, items[item],f'ожидали тип {listOfItems[item]}')
            elif listOfItems[item] == 'bool':
                if not CheckBool(items[item]):
                    ErrorLog(item,items[item],f'ожидали тип {listOfItems[item]}')
            elif listOfItems[item] == 'url':
                if not CheckUrl(items[item]):
                    ErrorLog(item,items[item], f'ожидали тип {listOfItems [item]}')
            elif listOfItems[item] == 'val':
                if not CheckStrValue(items[item] , ['itemBuyEvent','itemVievEvent']):
                    ErrorLog(item, items[item], 'ожидали значение itemBuyEvent или itemVievEvent')
            else:
                ErrorLog(item,items[item],'неожиданное значение')
        else:
            ErrorLog(item, items[item], 'неизвестная переменная')
if Error == []:
    print('Pass')
else:
    print('Fail')
    print(Error)
