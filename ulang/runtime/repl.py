# decompyle3 version 3.3.2
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.1 (default, Jan  3 2020, 22:44:00) 
# [GCC 8.3.0]
# Embedded file name: ulang\runtime\repl.py
# Size of source mod 2**32: 82682 bytes
import sys, cmd
from ulang.parser.core import Parser
from ulang.parser.lexer import lexer
from ulang.runtime.env import create_globals
from ulang.runtime.功用 import 反馈信息

def is_close(源码):
    """
    Check if the given 源码 is closed,
    which means each '{' has a matched '}' 
    """
    关键词 = {
     'FUNC', 'OPERATOR', 'ATTR', 'TYPE',
     'FOR', 'LOOP', 'WHILE',
     'IF', 'ELIF', 'ELSE',
     'TRY', 'CATCH', 'FINALLY'}
    未配对之和 = 0
    unclosed_sum = 0
    if len(源码) > 1:
        if 源码[-2] == '\\':
            return False
        else:
            tokens = lexer.lex(源码)
            unclosed = []
            未配对 = [
            0, 0, 0]
            last = 2 * ['']
            for tok in tokens:
                c = tok.gettokentype()
                last[0], last[1] = last[1], c
                if c in 关键词:
                    unclosed.append(c)
                if c == 'LBRACE':
                    未配对[0] += 1
                elif c == 'RBRACE':
                    未配对[0] -= 1
                    if len(unclosed):
                        unclosed.pop(-1)
                elif c == '(':
                    未配对[1] += 1
                elif c == ')':
                    未配对[1] -= 1
                elif c == '[':
                    未配对[2] += 1
                elif c == ']':
                    未配对[2] -= 1
            未配对之和 = sum(未配对)
            unclosed_sum = len(unclosed)
            if unclosed_sum > 0:
                if 未配对之和 == 0:
                    if last[1] == 'NEWLINE':
                        if (last[0] == 'NEWLINE' or last[0]) == ';':
                            pass
                        return True
    return unclosed_sum == 0 and 未配对之和 == 0


def input_swallowing_interrupt(_input):

    def _input_swallowing_interrupt(*args):
        try:
            return _input(*args)
        except KeyboardInterrupt:
            print('^C')
            return '\n'

    return _input_swallowing_interrupt


class Repl(cmd.Cmd):
    """
    A simple wrapper for REPL using the python cmd module.
    """

    def __init__(self, ps1='> ', ps2='>> ', globals=None, locals=None):
        super().__init__()
        self.ps1 = ps1
        self.ps2 = ps2
        self.globals = globals
        self.locals = locals
        self.parser = Parser()
        self.prompt = ps1
        self.stmt = ''

    def do_help(self, arg):
        self.default('help(%s)' % arg)

    def do_quit(self, arg):
        self.default('quit(%s)' % arg)

    def do_EOF(self, arg):
        self.default('quit()')

    def onecmd(self, line):
        if line == 'EOF':
            return self.do_EOF(line)
        self.default(line)
        self.prompt = self.ps1 if len(self.stmt) == 0 else self.ps2

    def default(self, line):
        if line is not None:
            self.stmt += '%s\n' % line
            if not self.is_close():
                return
            try:
                try:
                    node = self.parser.parse('___=(%s);__print__(___)' % self.stmt, '<STDIN>')
                except Exception:
                    node = self.parser.parse(self.stmt, '<STDIN>')

                code = compile(node, '<STDIN>', 'exec')
                exec(code, self.globals, self.locals)
            except SystemExit:
                sys.exit()
            except BaseException as e:
                try:
                    sys.stderr.write('%s\n' % 反馈信息(e))
                finally:
                    e = None
                    del e

            finally:
                self.stmt = ''

    def is_close(self):
        return is_close(self.stmt)

    def cmdloop(self, *args, **kwargs):
        orig_input_func = cmd.__builtins__['input']
        cmd.__builtins__['input'] = input_swallowing_interrupt(orig_input_func)
        try:
            (super().cmdloop)(*args, **kwargs)
        finally:
            cmd.__builtins__['input'] = orig_input_func


def repl(ps1='> ', ps2='>> ', globals=None):
    """
    A simple read-eval-print-loop for the µLang program
    """
    info = [
     '\t详情: 列出内置功能',
     '\t再会: 结束对话',
     '\t你好: 显示这段']
    if not globals:
        globals = create_globals(fname='<STDIN>')
    globals['详情'] = lambda : print('\n'.join([' %s (%s)' % (k, v.__class__.__name__) for k, v in globals.items() if k != '__builtins__' if k != '___']))
    globals['你好'] = lambda *args: print('\n'.join(info)) if not args else print()
    Repl(ps1, ps2, globals).cmdloop("木兰向您问好\n更多信息请说'你好'")
    sys.exit(0)