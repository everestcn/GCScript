#!/bin/python3
#Build in Ubuntu 20.04
#This is a little Demo
import zipfile
import os
import math
import time
import sys
import random
def readfile(file):
    try:    
        
        files = open(file)               
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
VER = "0.0.3"
KEYWORDS = ["when", "if", "outprint", "SaveAndQuit", "using", "setv", "/", "help", "get_input", "pause", "+", "-", "*", "/", "**", "if", "c_value"]
Ifwords = ["then"]
VLAUETYPES = ["string", "int", "float", "boolen", "bin"]
math_types = ["/", "*", "-", "+", "**"]
value_branches = {0:"string", 1:"int", 2:"float", 3:"boolen", 4:"bin"}
helps = None
users_value = {}
#settings
global contion
def if_branch(condition):

    global contion
    n1, n2 = '', ''
    contion = None
    ctn = condition.split("==")
    if ctn[0] in users_value.keys():
        n1 = users_value[ctn[0]]
                
    if ctn[1] in users_value.keys():
        n2 = users_value[ctn[1]]
                
                
    if n1 == '':
        try:
            n1 = int(ctn[0])
        except ValueError:
            print("can't find value!")
    if n2 == '':
        try:
            n2 = int(ctn[1])
        except ValueError:
            print("can't find value!")
    if n1 == n2:
        contion = True
        return None
    if n1 != n2:
        contion = False
        return None
    else:
        print("faild:")
        return None
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
    global contion
    global ids
    if script == None:return None
    else:
        global read_sct
        read_sct = script
        if script == "c_d":
            print(users_value)
        for keywords in KEYWORDS:
            if keywords in script:
                if keywords == "c_value":
                    branch("[", "]")
                    if ids == 2:
                        if script[8:len(script)-1] in users_value:
                            get_change = input("input for change value "+script[8:len(script)-1]+".type '' to quit:")
                            if get_change != '':
                            
                                users_value[script[7:len(script)-1]] = get_change
                            else:
                                return None
                        
                if keywords == "if":
                    branch("(", ")")
                    if ids == 2:
                        if_branch(script[script.index('(')+1:script.index(')')])
                        if script[len(script)-1:] == "{":
                            if_under_cmd = []
                            while 1:
                                
                                cmd = input("[in if("+script[script.index('(')+1:script.index(')')]+")]>>>")
                                if cmd == "}":
                                    if contion != True:
                                        return None
                                    else:
                                        for run_times in if_under_cmd:
                                            scripts(run_times)
                                        return None
                                else:
                                    if_under_cmd.append(cmd)
                                
                                
                                    
                if keywords == "pause":
                    branch("(", ")")
                    if ids == 2:
                        pause_time = int(script[6:len(script)-1])
                        time.sleep(pause_time)
                    else:print("faild:missing ( or )")
                if keywords == "+" or keywords == "-" or keywords == "*" or keywords == "/" or keywords == "**":
                    try:
                        print(str(eval(script)))
                        return 0
                    except TypeError:
                        print("faild:you must type the number, not string.")
                        print("\033[0;31;40m\tFAILD\033[0m")
                        return 0
                if keywords == "get_input":
                    branch('"', '"')
                    if ids == 2:
                        ipt = input(script[11:len(script)-1])
                    else:
                        print('faild:missing "')
                        print("\033[0;31;40m\tFAILD\033[0m")
                if keywords == "using":
                    branch("(", ")")
                    if ids == 2:readfile(script[6:len(script)-1])
                    else:
                        print("faild:missing ( or )")
                        print("\033[0;31;40m\tFAILD\033[0m")
                if keywords == "help":
                    branch('(', ')')
                    if ids == 2:help_system()
                    else:
                        print("faild:missing ( or )")
                        print("\033[0;31;40m\tFAILD\033[0m")
                    
                if keywords == "outprint":
                    branch('"')
                    if ids == 2:                    
                        if DEBUG == True:print("DEBUG:"+script[9:len(script)])
                        else:print("OUTPUT:"+script[9:len(script)])
              
                    else:
                        print('faild:missing " ')
                        print("\033[0;31;40m\tFAILD\033[0m")
                if keywords == "SaveAndQuit":
                    branch('(', ')')
                    if ids == 2:
                        print("exit with code 0")
                        sys.exit()
                    else:
                        print("faild:missing ( or )")
                        print("\033[0;31;40m\tFAILD\033[0m")
                if keywords == "setv":
                    branch('[', ']')
                    if ids == 2:
                        value_branch = 0
                        if " " in script[5:len(script)-1]:  
                            print("faild:you can't type ' ' in value name")
                            print("\033[0;31;40m\tFAILD\033[0m")
                            return None
                        
                        else:
                            if script[5:len(script)-1] in users_value:
                                print(users_value[script[5:len(script)-1]])
                                return None
                            value = input("input for your value:")
                            users_value[script[5:len(script)-1]] = value
                            return None
                                
                                    

                             
                    
                    else:
                        print("faild:missing [ or ]")
                        print("\033[0;31;40m\tFAILD\033[0m")
        for u_values in users_value:
            if script == u_values:
                print(users_value[script])
                break
            else:pass
                
def control_on_terminal():    
    print("GCScript v0.01\nusing help() to get more imformation")                 
    while True:
        sys_exit_code(mode=True)
        ream = input(">>>")
        scripts(ream)   


                        
if __name__ == "GCScript":pass
if __name__ == "__main__":control_on_terminal()
             
                    
                





x
