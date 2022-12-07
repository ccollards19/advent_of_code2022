from anytree import Node, RenderTree

def get_size(root, size):
    for node in root.children:
        if (node.size == "dir"):
            size = size + get_size(node, 0)
        else:
            size = size + (int)(node.size) 
    return size
        

def get_score(root):
    size = 0;
    for node in root.descendants:
        if (node.size == "dir"):
            dir_size = get_size(node, 0)
            if dir_size > 532950:
                if size == 0 or dir_size < size:
                    size = dir_size
    return size

root = Node(name='root', parent=None, children=None)
current_parent = root
with open('input') as file:
    for line in file :
        line = line.strip('\n')
        line = line.split(' ')
        if line[0] == "$" and line[1] == "cd":
            if line[2] == "..":
                current_parent = current_parent.parent
            else:
                for i in current_parent.children:
                    if i.name == line[2]:
                        current_parent = i
                        break
        elif (line[0] == "$" and line[1] == "ls") or (line[0] == "$" and line[1] == "cd" and line[2] == "/"):
            continue
        else:
            node = Node(name=line[1], parent=current_parent, children=None, size=line[0])
    score = get_score(root)
    size = get_size(root, 0)
    size = 30000000 - (70000000 - size)
    print (size)
    print (score)
    
