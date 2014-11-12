from vyapp.tools.misc import get_opened_files, find_on_all
from time import time


class WordComplete(object):
    """

    """
    def __init__(self, area):
        """
        """

        self.area  = area
        INSTALL    = [(0, '<Control-q>', lambda event: self.complete())]
        self.seq   = iter(())
        self.snd   = time()
        self.MAX   = 2
        self.index = None

        area.install(*INSTALL)

    def complete(self):
        """
        """

        if time() - self.snd > self.MAX: 
            self.reset()

        try:
            data = self.seq.next()
        except StopIteration:    
            self.reset()        
        else:
            self.area.delete(self.index, 'insert')
            self.area.insert(self.index, data)
        self.snd = time()


    def reset(self):
        """
        """

        if self.area.compare('insert', '==', 'insert linestart'):
            return

        self.index = self.area.search(' ', 'insert', 
                                      stopindex='insert linestart',regexp=True, 
                                      backwards=True)

        if not self.index: self.index = 'insert linestart'
        else: self.index = '%s +1c' % self.index
        if self.area.compare(self.index, '==', 'insert'): return

        data     = self.area.get(self.index, 'insert')
        self.seq = find_on_all('%s[^ ]+' % data)

install = WordComplete









