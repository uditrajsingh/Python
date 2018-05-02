from lib import *

class task:

    dir_desktop = 'c:/users/danish/desktop'
    dir_downloads = 'c:/users/danish/downloads'
    dir_e = 'E:/'
    dir_c = 'C:/'


    valid_commands = ['.cd', '.file', '.folder','.help', '.cwd', '.quit', '.new', '.archive', '.del']

    def __init__(self, validated_executable_statement):
        self.exe = validated_executable_statement

    def perform(self, exe):
        if(exe not in task.valid_commands):
            raise WindowsError
        elif(exe == '.cd'):
            task.cd(self.exe)
        elif(exe == '.file'):
            task.file()
        elif(exe == '.folder'):
            task.folder()
        elif(exe == '.cwd'):
            task.cwd()
        elif(exe == '.quit'):
            quit()
        elif(exe == '.new'):
            task.new(self.exe)
        elif(exe == '.archive'):
            task.archive(self.exe)
        elif(exe == '.del'):
            task._del(self.exe)
        else:
            pass

    @staticmethod
    def _del(s):
        ex = ((s.split(' '))[1])
        try:
            os.remove(ex)
            print 'deleted succesfully ',ex
        except Exception:
            print 'Error: permission denied'

    @staticmethod
    def archive(s):
        ex = ((s.split(' '))[1]).split('--')
        try:
            print shutil.make_archive(ex[0], ex[1], base_dir=ex[2])
        except Exception:
            print 'Illegal argument'




        


    @staticmethod
    def new(s):
        try:
            os.mkdir((s.split(' '))[1])
        except WindowsError:
            pass


    @staticmethod
    def cwd():
        print os.getcwd()

    @staticmethod
    def cd(s):
        ex = ((s.split(' '))[1]).lower().capitalize()
        if(ex == 'Desktop'):
            try:
                os.chdir(task.dir_desktop)
            except WindowsError:
                print 'unknown directory'
        elif(ex == 'Downloads'):
            try:
                os.chdir(task.dir_downloads)
            except WindowsError:
                print 'unknown directory'
        elif(ex == 'C'):
            try:
                os.chdir(task.dir_c)
            except WindowsError:
                print 'unknown directory'
        elif(ex == 'E'):
            try:
                os.chdir(task.dir_e)
            except WindowsError:
                print 'unknown directory'
        else:
            try:
                os.chdir(ex)
            except WindowsError:
                print 'unknown directory'

    @staticmethod
    def file():
        files = [i for i in os.listdir(os.getcwd()) if os.path.isfile(i)]
        for i in files: 
            print '\t'*10,i 
        print 

    @staticmethod
    def folder():
        folder =  [i for i in os.listdir(os.getcwd()) if not os.path.isfile(i)]
        for i in folder:
            print '\t'*10,i
        print 

