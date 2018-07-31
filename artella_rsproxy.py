# in Maya users, please goto the bottom of the script
# for further instructions
# questions to Benjamin Slack, iam@nimajneb.com or via #slack

from __future__ import print_function
import re
import sys
import os

artella_top_folder = '_art'
insert_var = '%ART_LOCAL_ROOT%'
rs_nodes = {
    "RedshiftBokeh": ".dofBokehImage",
    "RedshiftLensDistortion": ".LDimage",
    "RedshiftLightGobo": ".tex0",
    "RedshiftCameraMap": ".tex0",
    "RedshiftNormalMap": ".tex0",
    "RedshiftProxyMesh": ".fn",
    "RedshiftDomeLight": ".tex0",
    "RedshiftVolumeShape": ".fn"
}


def parse_line(line):
    break_pat = '(.*)(' + artella_top_folder + '.*)'
    break_exp = re.compile(break_pat)
    front, back = break_exp.match(line).groups()
    # print("front", front)
    # print("back", back)
    front, ditch = str(front).rsplit('"', 1)
    # print("front", front)
    # print("ditch", ditch)
    sep_pat = '(.*)([\\/]+)'
    sep_exp = re.compile(sep_pat)
    ditch, sep = sep_exp.match(ditch).groups()
    # print("ditch", ditch)
    # print("sep", sep)
    newline = front + '"{0}{1}'.format(insert_var, sep) + back
    # print(newline)
    return newline


def main(infile):
    buf = ''
    with open(infile, 'r') as f:
        lines = f.readlines()
    attr = None
    for line in lines:
        for this_key in rs_nodes.keys():
            if "createNode {}".format(this_key) in line:
                print("Found {}...".format(this_key))
                attr = rs_nodes[this_key]
        if attr is not None and attr in line:
            print("old line - ", line)
            newline = parse_line(line)
            print("new line - ", newline)
            line = newline
            attr = None
        buf += line
    with open(infile.rstrip('.ma') + '_py_processed.ma', 'w') as f:
        f.write(buf)


if __name__ == '__main__':
    # users, this line here
    # if you want to run this from inside Maya, replace the path below
    # with the path to the file you wish to process
    infile = ''
    try:
        infile = os.path.abspath(os.path.expanduser(sys.argv[1]))
    except:
        # this path here
        infile = r"./test2.ma"
        infile = os.path.abspath(os.path.expanduser(infile))
    main(infile)
