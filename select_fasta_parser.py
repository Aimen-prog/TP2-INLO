#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
from adn import get_fasta,check_fasta

__author__ = 'Aimen CHERIF'

def create_parser():
    """ Declares new parser and adds parser arguments """
    program_description=''' reading fasta file and checking sequence format '''
    parser =  argparse.ArgumentParser(add_help=True,description=program_description)
    parser.add_argument('-i','--inputfile',default=sys.stdin,
    help="required input file in fasta format",type=argparse.FileType("r"),required=True)
    return parser

def main():
    """ Main function for reading fasta file and checking sequence format """
    parser = create_parser()
    args = parser.parse_args()
    args = args.__dict__
    fasta_input = args["inputfile"].name #get input name
    check_fasta(get_fasta(fasta_input))


if __name__ == "__main__":
    main()
