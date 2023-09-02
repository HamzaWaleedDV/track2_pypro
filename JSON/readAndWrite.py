stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

import json

#read
JDPV = json.loads(stringOfJsonData)
print(JDPV)

#write
pythonValue = {"isCat": True, "miceCaught": 0, "name": "Zophie", "felineIQ": None}

writeJson = json.dumps(pythonValue)
print(writeJson)