from thingking import loadtxt
import sdf
import numpy as np

prefix = "../project/data/ds14_scivis_0128/"
filename = prefix + "rockstar/trees/tree_0_0_0.dat"

trees = {}
particle = []
lines = []

with open(filename, 'r') as f:
    for line in f:
        lines.append(line)

for index, line in enumerate(lines):
    if line[:5]=="#tree":
        treeId = line
        next_line_index = index + 1
        while next_line_index < len(lines):
            next_line = lines[next_line_index]
            if next_line[:5] == "#tree":
                break
            else:
                p = next_line.split(" ")
                particle.append(p)
            next_line_index += 1
        trees[treeId] = particle
        particle = []  # 重新创建空列表