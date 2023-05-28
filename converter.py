import json

file = 'tips.ipynb'

code = json.load(open(file))
filename = file.split(".")[0]
py_file = open(f"{filename}.py", "w+")

for cell in code['cells']:
    if cell['cell_type'] == 'code':
        if "#| export" in cell['source'][0]:
            for line in cell['source'][1:]:
                py_file.write(line)
                
        py_file.write("\n")
    elif cell['cell_type'] == 'markdown':
        py_file.write("\n")
        for line in cell['source']:
            if line and line[0] == "#":
                py_file.write(line)
            else:
                py_file.write("#* " + line)
        py_file.write("\n")

py_file.close()