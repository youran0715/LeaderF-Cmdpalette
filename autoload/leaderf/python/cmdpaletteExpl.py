#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import vim
import os
import os.path
from leaderf.utils import *
from leaderf.explorer import *
from leaderf.manager import *


#*****************************************************
# CmdpaletteExplorer
#*****************************************************
class CmdpaletteExplorer(Explorer):
    def __init__(self):
        pass

    def getContent(self, *args, **kwargs):
        tmp = lfEval("@x")
        lfCmd("redir @x")

        lfCmd("silent command")
        result = lfEval("@x")
        lfCmd("let @x = '%s'" % escQuote(tmp))
        lfCmd("redir END")

        # return lfEval("split(system('gopkgs'), '\n')")
        result_list = result.splitlines()[2:]
        result_list = [x[4:].split()[0]+'\t'
                for x in result_list
                if x.strip()]
        return result_list

    def getStlCategory(self):
        return "Cmdpalette"

    def getStlCurDir(self):
        return escQuote(lfEncode(os.getcwd()))

    def isFilePath(self):
        return False


#*****************************************************
# CmdpaletteExplManager
#*****************************************************
class CmdpaletteExplManager(Manager):
    def __init__(self):
        super(CmdpaletteExplManager, self).__init__()
        self._match_ids = []

    def _getExplClass(self):
        return CmdpaletteExplorer

    def _defineMaps(self):
        lfCmd("call leaderf#Cmdpalette#Maps()")

    def _setImportAs(self, import_as):
        self.flag_import_as = import_as

    # def _cmdExtension(self, cmd):
    #     if equal(cmd, '<C-D>'):
    #         self.flag_import_as = 1
    #         self.accept()
    #     return True

    def _acceptSelection(self, *args, **kwargs):
        if len(args) == 0:
            return
        line = args[0]

        # lfCmd(": " + line)
        # lfCmd("call leaderf#Cmdpalette#Exec(\"" + line + "\")")
        # lfCmd("let tempfile = '__temp'")
        lfCmd("call writefile([input(':', '" + line[:-1] + "', 'command')], '__temp')")
        lfCmd("source __temp")
        lfCmd("call delete('__temp')")
        # lfCmd("source ")
        # if self.flag_import_as == 1:
            # local_name = lfEval("input('Enter local name: ')")
            # lfCmd("cmdpaletteAs " + local_name + " " + line)
        # else:
            # lfCmd("cmdpalette " + line)


    def _getDigest(self, line, mode):
        """
        specify what part in the line to be processed and highlighted
        Args:
            mode: 0, 1, 2, return the whole line
        """
        return line
        # return line[4:].split("[\t ]", 1)[0]
        # return line.split("\t")[:2]
        # return line.rsplit("\t")[2]

    def _getDigestStartPos(self, line, mode):
        """
        return the start position of the digest returned by _getDigest()
        Args:
            mode: 0, 1, 2, return 1
        """
        return 0

    def _createHelp(self):
        help = []
        help.append('" i : switch to input mode')
        help.append('" q : quit')
        help.append('" <F1> : toggle this help')
        help.append('" ---------------------------------------------------------')
        return help


#*****************************************************
# cmdpaletteExplManager is a singleton
#*****************************************************
cmdpaletteExplManager = CmdpaletteExplManager()

__all__ = ['cmdpaletteExplManager']
