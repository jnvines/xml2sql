#!/Library/Frameworks/Python.framework/Versions/3.3/bin/python3
import argparse

parser = argparse.ArgumentParser(description="Build a tree of a DTD File")
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("input_file", help="DTD File to readin")
parser.add_argument("-o", "--output_file", help="Optionally output tree to a file")
args = parser.parse_args()


if args.verbose:
    print("Parsing " + args.input_file, end = '')
    if args.output_file:
    	print(" and writing to " + args.output_file + "...")
    else:
    	print("...")
    	

    
    