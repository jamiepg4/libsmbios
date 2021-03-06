#!/usr/bin/python
# vim: et:ai:sw=4:ts=4:filetype=python:nocindent:

import sys


def writeStdHeaders( out ):
    out.write ("""
#ifndef __STD_SMBIOS_XML_H
#define __STD_SMBIOS_XML_H

//
// This is an *AUTOMATICALLY* *GENERATED* file. Do not edit this file
// as your changes will be lost the next time the file is generated
//

""")

def writeStdFooters( out ):
    out.write ("""

#endif /* __STD_SMBIOS_XML_H */

""")

def processFile( input, output ):
    charsPerLine = 16
    output.write( """
const char stdXml[] = { """)
    
    charsWrittenThisLine = charsPerLine
    while 1:
        c = input.read(1)
        if c == "":   # end of file
            break 
        if charsWrittenThisLine == charsPerLine/2:
            output.write("  ")
        if charsWrittenThisLine >= charsPerLine:
            output.write( "\n" )
            output.write( "\t" )
            charsWrittenThisLine = 1
        output.write( "0x%02x, " % ord(c) )
        charsWrittenThisLine = charsWrittenThisLine + 1
        
    output.write( """0x00
};
""")

def main():
    inputXml = None
    outputHeader = None
    inputXml = sys.argv[1]
    if len(sys.argv) > 2:
        outputHeader = sys.argv[2]

    inputFh = open( inputXml, "r" )
    if outputHeader is not None:
        outputFh = open( outputHeader, "w+" )
    else:
        outputFh = sys.stdout

    writeStdHeaders( outputFh )
    processFile( inputFh, outputFh )
    writeStdFooters( outputFh )


if __name__ == "__main__":
    main()
