import os
import os.path
import sys

BASE_DIR = "xxxxx"
COMPONENTS_DIR = os.path.join(BASE_DIR, components)
INCLUDEMARKER = "INCLUDE:"
COMPONENTMARKER = "component_"

def get_available_components():
    components = []
    for path, subdir, files in os.walk(COMPONENTS_DIR):
        for file in files:
            if file.startswith(COMPONENTMARKER):
                component = file.lstrip(COMPONENTMARKER)
                component = component.split('.')[0]
                components.append(component)
    return components

def form_include_marker(marker):
    return '<!-- ' + INCLUDEMARKER + marker + ' -->'

class component:
    def __init__(self, name):
        self.name = name
        self.filename = COMPONENTMARKER + name + '.html'
        self.fullpath = os.path.join(COMPONENTS_DIR, self.filename)
        
        f = open(self.fullpath, 'rb')
        self.content = f.read()
        f.close()
        
    def decode_content(self):
        return str(self.content.decode(sys.stdout.encoding))
    
class file:
    def __init__(self, dir, name):
        self.dir = dir
        self.name = name
        self.fullpath = os.path.join(dir, name)
        
        # condition: if it exists, read it
        f = open(self.fullpath, 'rb')
        self.content = f.read()
        f.close()
        
        self.find_component_includes()
        
    def find_component_includes(self):
        available_components = get_available_components()
        self.components = {}
        
        f = open(self.fullpath, 'rb')
        for line in f:
            line_str_list = []
            line_str = str(line.decode(sys.stdout.encoding))
            if "<!--" in line_str and INCLUDEMARKER in line_str:
                line_str_list = line_str.split('<!--')
                del line_str_list[0]
                line_str_list = [item.split('-->')[0] for item in line_str_list]
                line_str_list = [item.strip() for item in line_str_list]
                line_str_list = [item for item in line_str_list if INCLUDEMARKER in item]
                line_str_list = [item.lstrip(INCLUDEMARKER).strip().lower() for item in line_str_list]
            
            for item in line_str_list:
                if item in available_components:
                    if item not in self.components:
                        self.components[item] = []
                    self.components[item].append(f.tell())
        f.close()
        self.remaining_components = self.components


# Open index.html
index = file(COMPONENTS_DIR, "index.html")
#print(index.components)

components = {}
for c in index.components:
    if c not in components:
        components[c] = component(c)
    #print(c)
    #print(components[c].decode_content())
    
result = file(BASE_DIR, "index2.html")

replace_byte_locations = []
for component in index.components:
    for b in index.components[component]:
        replace_byte_locations.append(b)
replace_byte_locations.sort()
print(replace_byte_locations)
        
f = open(index.fullpath, 'rb')
# replace components from end to beginning
text = f.read()
for b in reversed(replace_byte_locations):
    # Find the component content associated w/ this b
    this_content = ""
    for component in index.components:
        for c in index.components[component]:
            if c == b:
                this_content = components[component].content
                #print(this_content)
                break
    
    print(b)
    f.seek(b)
    #print(text[b:])
    print(text)
    text = text[:b] + this_content + text[b:]

f.close()

f = open(result.fullpath, 'wb')
f.write(text)
f.close()
