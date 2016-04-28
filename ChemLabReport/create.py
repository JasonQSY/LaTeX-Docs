#!/usr/local/bin/python3
import sys
import os
shell = os.system;

# Check the command
errorStr = "Please input the correct argument"
if len(sys.argv) != 2:
    print(errorStr)
    exit()

if not sys.argv[1].isdigit():
    print(errorStr)
    exit()

# Start mkdir
print('Make direction...')

dir = '~/Current/Experiment_' + sys.argv[1]
mkdir = 'mkdir ' + dir
if shell(mkdir) == 0:
    subdir = dir + '/images'
    mksubdir = 'mkdir ' + subdir
    shell(mksubdir);
    print('Success!')
else:
    print('Error in mkdir!')
    exit()

list = ['./report.tex', './std-head.tex', './toc.tex', './background.tex',
       './handwrite.tex', './alr.tex', './appendix.tex', './report.tex.latexmain']
dir = dir + '/'

print('Copy tex file...')

for dirin in list:
    cp = 'cp ' + dirin + ' ' + dir
    shell(cp)

shell('cp ./input/mytitlepage.tex ' + dir + 'titlepage.tex')

print('Success!')
print('Your LaTeX project is ready at ' + dir)
