import json
import argparse

#below command for conversion 
# -> python -u "/home/demonhunter/projects/device_detector/converter_update.py" 'tips.ipynb' 

parser = argparse.ArgumentParser(description='Convert .ipynb file to .py file')
parser.add_argument('input_file', help='Path to the input .ipynb file')
args = parser.parse_args()
file = args.input_file

code = json.load(open(file))
filename = file.split(".")[0]
py_file = open(f"{filename}.py", "w+")

for cell in code['cells']:
    if cell['cell_type'] == 'code':
        if cell['source'] and (("#| export" in cell['source'][0]) or("#|export" in cell['source'][0]) ):
            py_file.write("# %%\n")       #you can comment out this line
            for line in cell['source'][1:]:
                py_file.write(line)
        py_file.write("\n")
    elif cell['cell_type'] == 'markdown':
        py_file.write("\n")
        py_file.write("# %%\n")         #you can comment out this line
        for line in cell['source']:
            if line and line[0] == "#":
                py_file.write(line)
            else:
                py_file.write("#* " + line)
        py_file.write("\n")

py_file.close()
