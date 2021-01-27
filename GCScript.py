#!/bin/python3
#Build in Ubuntu 20.04
#This is a little Demo
import zipfile
import os
import math
import tkinter
import time
import sys
import random

def readfile(file):
    try:    
        
        files = open(file+".gc")               
        line = files.readline()               
        while line: 
            
            scripts(line)
            line = files.readline()
        files.close()   
    except:
        print("faild to open file "+file+".gc")
        files.close() 
     
def sys_init_start(DE=False, GU=False, NE=True):
    DEBUG = DE
    GUI = GU
    NEW = NE

#settings
global read_sct
global ids
DEBUG = False
VER = "0.0.1"
KEYWORDS = ["when", "if", "outprint", "SaveAndQuit", "using", "setv", "/", "help", "get_input", "pause"]
VLAUETYPES = ["string", "int", "float", "boolen", "bin"]
value_branches = {0:"string", 1:"int", 2:"float", 3:"boolen", 4:"bin"}
helps = None
users_value = {}
#settings

def help_system(help_things=None):
    try:    
        
        files = open("help.txt")               
        line = files.readline()               
        while line: 
            
            print(line)
            line = files.readline()
        files.close()   
    except:
        print("faild to open helpfile")
        files.close() 

def branch(types=None, types2=None):
    global read_sct
    global ids
    ids = 0
    if types2 == None:
        for script_text in read_sct:
            if types in script_text:ids += 1
    elif types2 != None:
        for script_text in read_sct:
            if types in script_text or types2 in script_text:ids += 1
    else:
        return None

def sys_exit_code(mode=False):
    if mode == True:
        pass
def scripts(script=None):
    global ids
    if script == None:return None
    else:
        global read_sct
        read_sct = script
        for keywords in KEYWORDS:
            if keywords in script:
                if keywords == "pause":
                    branch("(", ")")
                    if ids == 2:
                        try:
                            time.sleep(int(script[6:len(script)-1]))
                        except:
                            print("faild:None")
                    else:print("faild:missing ( or )")
                if keywords == "get_input":
                    branch('"', '"')
                    if ids == 2:
                        ipt = input(script[11:len(script)-1])
                        print("INPUT:"+str(ipt))
                    else:print('faild:missing "')
                if keywords == "using":
                    branch("(", ")")
                    if ids == 2:
                        readfile(script[6:len(script)-1])
                    else:print("faild:missing ( or )")
                if keywords == "help":
                    branch('(', ')')
                    if ids == 2:help_system()
                    else:print("faild:missing ( or )")
                    
                if keywords == "outprint":
                    branch('"')
                    if ids == 2:                    
                        if DEBUG == True:print("DEBUG:"+script[9:len(script)])
                        else:print("OUTPUT:"+script[9:len(script)])
              
                    else:
                        print('faild:missing " ')
                        print("FAILD")
                if keywords == "SaveAndQuit":
                    branch('(', ')')
                    if ids == 2:
                        print("exit with code 0")
                        sys.exit()
                    else:print("faild:missing ( or )")
                if keywords == "setv":
                    branch('[', ']')
                    if ids == 2:
                        value_branch = 0
                        for _ in range(5):
                            if script[5:len(script)-1] == value_branches[value_branch]:
                                print(value_branches[value_branch])
                                name = input("input for your value name:")
                                for u_values in users_value:
                                    if name in u_values:
                                        print(users_value[name])
                                        break
                                    else:
                                        users_value.update(name)
                                break
                            else:
                                if value_branch < 4:
                                    value_branch += 1
                                else:print("faild:can't find value type "+script[5:len(script)-1])
                    else:
                        print("faild:missing [ or ]")
                        print("FAILD")
        for u_values in users_value:
            if script == u_values:
                print(users_value[script])
                break
            else:
                pass
                
                        

print("GCScript v0.01")
print("using help() to get more imformation")                                 
while True:

    sys_exit_code(mode=True)
    ream = input(">>>")
    scripts(ream)                 
             
                    
                

