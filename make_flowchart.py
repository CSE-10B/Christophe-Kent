#!/usr/bin/env python3
"""Generate a simple flowchart from a short instruction sentence.

Creates:
 - flowchart_mermaid.md  (Mermaid text you can paste into Markdown)
 - flowchart.dot         (Graphviz DOT file)
 - flowchart.png         (rendered PNG if `dot` is available)

Usage: python3 make_flowchart.py "Take twenty paces, then turn and shoot."
If no argument is given, the script uses the default example.
"""
import sys
import shutil
import subprocess
from pathlib import Path

default = "Take twenty paces, then turn and shoot."
text = sys.argv[1] if len(sys.argv) > 1 else default

# Very small heuristic parser: split on ' then ' and commas
parts = []
for seg in text.split(' then '):
    for p in seg.split(','):
        p = p.strip()
        if p:
            parts.append(p)

nodes = ['Start'] + parts + ['End']

def mermaid_node(i, label):
    lbl = label.replace('"', '\\"')
    if label.lower() == 'start' or label.lower() == 'end':
        return f"N{i}([{lbl}])"
    return f"N{i}[{lbl}]"

# Build Mermaid
mermaid = "```mermaid\nflowchart TD\n"
for i in range(len(nodes) - 1):
    mermaid += f"  {mermaid_node(i, nodes[i])} --> {mermaid_node(i+1, nodes[i+1])}\n"
mermaid += "```\n"

Path('flowchart_mermaid.md').write_text(mermaid, encoding='utf-8')

# Build DOT
dot = 'digraph G {\n'
dot += '  rankdir=TB;\n'
for i, label in enumerate(nodes):
    shape = 'oval' if label.lower() in ('start', 'end') else 'box'
    dot += f'  N{i} [label="{label}" shape={shape}];\n'
for i in range(len(nodes) - 1):
    dot += f'  N{i} -> N{i+1};\n'
dot += '}\n'

Path('flowchart.dot').write_text(dot, encoding='utf-8')

dot_exec = shutil.which('dot')
if dot_exec:
    out = 'flowchart.png'
    try:
        subprocess.run([dot_exec, '-Tpng', 'flowchart.dot', '-o', out], check=True)
        print(f'Wrote {out} (rendered with {dot_exec})')
    except subprocess.CalledProcessError:
        print('Graphviz was found but rendering failed. DOT saved as flowchart.dot')
else:
    print('Graphviz `dot` not found. Wrote flowchart.dot and flowchart_mermaid.md')

print('Mermaid saved to flowchart_mermaid.md')
