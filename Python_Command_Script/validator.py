from lib import *
class validator:

    all_alphabets = string.ascii_lowercase + string.ascii_uppercase


    def __init__(self, string_to_be_validated):
        self.root = string_to_be_validated

    def validate__del(self):
        if(self.root.rfind('.del') == -1 or self.root.rfind('.del') > 1):
            return False
        if(self.root.rfind(' ') != 4):
            return False
        return True

    def validate__archive(self):
        if(self.root.rfind('.archive') == -1 or self.root.rfind('.archive') > 1):
            return False
        if(self.root.rfind(' ') != 8):
            return False
        ex = ((self.root.split(' '))[1]).split('--')
        if(len(ex) != 3):
            print 'Illegeal statement'
            return False
        return True 

    def validate__new(self):
        if(self.root.rfind('.new') == -1 or self.root.rfind('.new') > 1):
            return False
        if(self.root.rfind(' ') != 4):
            return False
        return True   

    def validate__help(self):
        if(self.root.rfind('.help') == -1 or self.root.rfind('.help') > 1):
            return False
        return True
        
    def validate__quit(self):
        if(self.root.rfind('.quit') == -1 or self.root.rfind('.quit') > 1):
            return False
        return True

    def validate__cwd(self):
        if(self.root.rfind('.cwd') == -1 or self.root.rfind('.cwd') > 1):
            return False
        return True

    def validate__file(self):
        if(self.root.rfind('.file') == -1 or self.root.rfind('.file') > 1):
            return False
        return True

    def validate__folder(self):
        if(self.root.rfind('.folder') == -1 or self.root.rfind('.folder') > 1):
            return False
        return True


    def validate__cd(self):
        if(self.root.rfind('.cd') == -1 or self.root.rfind('.cd') > 1):
            return False
        if(self.root.rfind(' ') != 3):
            return False
        return True
