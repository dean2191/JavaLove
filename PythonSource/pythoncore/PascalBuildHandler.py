#!/usr/bin/python
# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import errno
import os


class PascalBuildHandler(object):

    _CUSTOM__PATH = False
    _BUILD_EXTENSION = '.lua'
    _LAST_FILE = None
    _LAST_DIRECTORY = None
    _OUTPUT_LANGUAGE = 1
    # constructor

    def __init__(self):  # this method creates the class object.
        self._CUSTOM__PATH = False
        self._BUILD_EXTENSION = '.lua'
        self._LAST_FILE = None
        self._Last_DIRECTORY = None
        self._OUTPUT_LANGUAGE = 1
        pass

    # creates an empty output file

    def _create_file(self, name):
        if self._LAST_DIRECTORY is None:
            self._LAST_FILE = open(name + self._BUILD_EXTENSION, 'w')
            self._LAST_FILE.write('--Generated by PUA : https://github.com/dean2191/PascalLove2D '
                                  )
        else:

            # fix the use of slash for directory later.

            self._LAST_FILE = open(self._LAST_DIRECTORY + '/' + name
                                   + self._BUILD_EXTENSION, 'w')
            self._LAST_FILE.write('--Generated by PUA : https://github.com/dean2191/PascalLove2D '
                                  )

        pass

    # Writes a function header to the file
    def _write_function(self, name):  # _PARAMETERS):
        self._LAST_FILE.write('\nfunction ' + name + " ")
        pass

    #simply output a standard piece of text
    def _write_(self, text):
        self._LAST_FILE.write(text+" ")
        pass

    #writes a new variable to file, either local or global
    def _write_variable_declaration(self, isLocal):
        if isLocal:
            self._LAST_FILE.write('\n ' + 'local ')
        else:
        #self._LAST_FILE.write('\n')
            pass

    def _write_constant(self, ctx):
        self._LAST_FILE.write('\nlocal ' + ctx.getChild(0).getText() + ' ' + ctx.getChild(1).getText() + ' ')
        pass

    def _write_constant_exit(self):
        self._LAST_FILE.write('\n')
        pass

    def _write_forLoop(self):
        self._LAST_FILE.write('\nfor ')
        pass

    def _write_int(self,number):
        self._LAST_FILE.write(' '+number+" ")
        pass

    def _write_compoundStatement(self):
        self._LAST_FILE.write('\nblock ')
        pass

    def _write_variable(self):
        self._LAST_FILE.write('\nvar ')
        pass

    def _write_function_expression(self,expression):
        #  self._LAST_FILE.write(expression)
        pass

    def _write_function_end(self):
        self._LAST_FILE.write('\nend\n')
        pass
    # close the last opened file

    def _build_file(self):
        #  self._write_function_end()
        self._LAST_FILE.close()

    # create a directory

    def _create_output_dir(self, name):
        try:
            self._LAST_DIRECTORY = name
            os.makedirs(name)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
        pass
