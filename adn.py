#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    This library checks whether a dna sequence is valid.
    If not, it purifies it or not, depending on user's choice.
    If not, it asks the user to input a sequence once again.

    It also checks if a fasta file is valid and reports first error in each
    sequence of the input file.
"""
__author__ = 'Aimen CHERIF'



"""
    Classic dna validation functions
    These functions check whether a dna sequence is valid with no purification before.
    If not, it ask the user to input a sequence once again.
"""


def is_valid(adn) :
    adn=adn.upper()  #Transforms all the sequence to uppercase
    adn=adn.replace(' ','') #removes spaces from the input
    global IMPURE, POS
    IMPURE=""  #chain that will receive the first impure base in the sequence
    POS=0       #will receive the position of the first impure base in the sequence
    valide=True
    for base in adn:
        POS+=1
        if not base in 'ATCG':
            IMPURE+=base
            return False
            valide=False
            break
    if valide is True :
        return True


def get_valid_adn(prompt='chaîne : ') :
    adn=input(prompt)
    adn=adn.replace(' ','').upper() #removing spaces/uppercase to get an appropriate result
    while purified_is_valid(adn) is False :
        adn=input("Entrez une séquence ADN valide : ")
    print ("La séquence ADN valide : " , purify(adn))

"""
    This function purifies a dna sequence before its validation
"""

def purify (adn_str):
    """purifies  dna sequence """
    if adn_str is not None :
        adn_str=adn_str.replace(" ","") #removes spaces from the input
        adn_str=adn_str.replace('\n','') #removes the newline escape sequences
        adn_str=adn_str.upper()  #Transforms all the sequence to uppercase
        for base in adn_str:
            if not base in 'ATCG':
                adn_str=adn_str.replace(base,'')  #removes non nucleotidic letters
        return adn_str
    else :
        return False

"""
    Advanced validations functions
    These functions check whether a purified dna sequence is valid 
    If not, it ask the user to input a sequence once again.
"""
def purified_is_valid(adn) :
    adn=purify(adn)
    if adn is not False and len(adn)>0:
        valide=True
        for base in adn:
            if not base in 'ATCG':
                return False
                valide=False
                break
        if valide is True :
            return True
    else :
        return False

def get_valid_purified_adn(prompt='chaîne : ') :

    adn=input(prompt)
    adn=adn.replace(' ','').upper() #removing spaces/uppercase to get an appropriate result
    while purified_is_valid(adn) is False :
        adn=input("Entrez une séquence ADN valide : ")
    print ("La séquence ADN valide : " , purify(adn))

"""
    This function reads a fasta file and puts it in a dictionary
    keys are the ids of each sequence (values)
"""

def get_fasta(fasta_file) :
    dico = {}
    with open(fasta_file,"r") as fasta:
        current = ""
        try :
            for line in fasta:   #loops through every line in the file
                line = line.strip()
                if line == "":          #if a line is empty,it ignores it.
                    continue
                if line[0] == ">":    #if a line starts with ">"
                    dico[line] = ""   #set id as key and value to empty until we find dna
                    current = line
                else :             #if line isn't empty and doesn't start with ">"
                    if dico[current] == "" : #if it's first dna line of the id add it
                        dico[current] = line
                    else:                    #same id and value not empty, add it to value
                        dico[current] +=line
        except :
            dico is False #it's not a fasta file
    return dico

"""
    This function checks the input (dict), verifies whether it's empty
    In case it's empty it prints a warning message
    If not, it prints the validity status of each sequence with its id ,length 
    plus the first wrong letter and its position in when the sequence is invalid
"""


def check_fasta(dico) :
    if not bool(dico) is False : #if a dictionary is not empty proceed to checking
        count=0
        for key in dico :
            if is_valid(dico[key]) :
                count+=1
                print ("La séquence d'identifiant :", key, "est valide")
                print( "La longueur de cette séquence est de", len(dico[key]),"\n")
            else :
                print ("La séquence d'identifiant :", key, "est invalide")
                print( "La longueur de cette séquence est de", len(dico[key]))
                print("La 1ère erreur dans la séquence est", IMPURE ,"à la position", POS,"\n")

        if count == len(dico.keys()) : #if all sequences are valid supplementary message
            print("Toutes les séquences du fichier fasta sont valides.")

    else :  #if a dictionary is empty
        print("Le fichier fasta est vide et/ou n'est pas sous forme fasta.")
