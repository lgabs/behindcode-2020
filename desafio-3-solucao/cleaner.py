import re
import os
import json


r1 = re.compile(r"([0-9]+:[0-9]+)")
r2 = re.compile(r'"')
r3 = re.compile(r"\n")
r4 = re.compile(r"\n$")



bodies = os.listdir("docs/plain_text/")
processed = os.listdir("docs/processed/")
docs_json = os.listdir("docs/")
docs_json = [d for d in docs_json if re.search(r"json", d)]

# print(docs_json)
# print(bodies)

rjson = re.compile('"body": "')

def write_on_json(file_name, body):
    with open("docs/" + file_name, "r") as f:
        text = f.read()

        # print(rjson.sub('"body": "' + body, text))
        # new = rjson.sub(r'"body": "asasa\\n\\n asad"', text)
        # new = rjson.sub(r'"body": "asasa\\n\\n asad"', text)
        # print('"body": "' + body)
        # print(new)

        # print(body)
        # with open("docs/" + file_name, "w") as f2:
        #     # json.dump(new, f2)
        #     f2.write(new)


for file in bodies:
    if file not in processed:
        print("processing: ", file)
        with open("docs/plain_text/" + file, "r") as f:
            text = f.read()
            proc_text = r1.sub(" ", text)
            proc_text = r2.sub(r"\"", proc_text)
            proc_text = r3.sub(r"\\n ", proc_text)
            proc_text = r4.sub(" ", proc_text)

            with open("docs/processed/" + file, "w") as g:
                g.write(proc_text)

            # write_on_json(file_name=re.sub(".txt", ".json", file), body=proc_text)
