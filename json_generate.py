main_loop = True
loop = True
properties = []

print "Type in the keys you want in your JSON object. Type STOP to move on."

while loop:
    element = raw_input("Key Name: ")
    if element == "stop":
        loop = False
    else:
        properties.append(element)
        #print properties
print "\n"
generate = raw_input("How many entries would you like? ")

jsonData = "{\n\t\"data\":[\n\t\t{\n"
id_num = 0
for i in range(int(generate)):
    id_num += 1
    jsonData += "\t\t\t\"id\": " + str(id_num) + ",\n"

    element_num = 0
    for i in properties:
        element_num += 1
        if element_num != len(properties):
            jsonData += "\t\t\t\""+i+"\":\"\",\n"
        else:
            jsonData += "\t\t\t\""+i+"\":\"\"\n"
    if id_num != int(generate):
        jsonData += "\n\t\t}\n\n\t\t{\n"

jsonData += "\n\t\t}\n\t]\n}"

print jsonData

data = open("data.txt", 'w')
data.write(jsonData)
data.close()

