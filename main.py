#!/usr/bin/env python3

import getopt
import sys
import os
import functions


def main(argv):
    csvfile = ''
    outputfile = ''

    if len(argv) < 1:
        print('must use at least "./import.py -h"')
        exit(0)
    try:
        opts, args = getopt.getopt(argv, "hc:o:", ["cfile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -c <csvfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('import.py -c <csvfile> -o <outputfile>')
            exit(0)
        elif opt in ("-c", "--cfile"):
            csvfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    print("CSV file is:", csvfile)
    print("Output file is: ", outputfile)
    if outputfile == '':
        outputfile = 'a.csv'

    new_cfile = 'randFileGen3235435345234132543.csv'
    cmd = 'touch ' + outputfile
    os.system(cmd)
<<<<<<< HEAD

    new_cfile = newCFile()

    # functions OK
    functions.writeNewHeaders(new_cfile, outputfile)

    new_i = cFileFromOutput()

    # functions OK
    functions.sortVariants(new_i, outputfile)

    # functions
    functions.parseFile(new_i, outputfile, prefix, suffix)

    new_i = cFileFromOutput()

    # functions
    functions.parseVariants(new_i, outputfile)

    deleteFiles()


def newCFile():
    global csvfile
    global outputfile
    rand_num = randint(100000,9999999)
    new_cfile = 'randFileGen' + str(rand_num) + '.csv'
    cmd = 'pwd'
    print(os.system(cmd))
    cmd = 'touch ' + new_cfile
    os.system(cmd)
=======
>>>>>>> e6b697cba67ec48779e0f2b66864c7645be66cc3
    cmd = 'cp ' + csvfile + ' ' + new_cfile
    os.system(cmd)

    new_f = functions.sortVariants(new_cfile, outputfile)

    # CHANGE THIS TO NEW_F ONCE SORTVARIANTS FINISHED
    functions.parseFile(new_f, outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])
