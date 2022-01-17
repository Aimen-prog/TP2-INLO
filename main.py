#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This main calls for adn.py functions to verify the if an input is dna
"""

__author__ = 'Aimen CHERIF'

from adn import *

if __name__ == "__main__":  
    
    check_fasta(get_fasta("exemple.fasta"))
    #get_valid_adn()
