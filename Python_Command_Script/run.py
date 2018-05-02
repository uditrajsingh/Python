from lib import *
initiate()

__cmd = {
    "newDirectory":"mkdir",
    "currentDirectory":"getcwd",
    "directoryName":"path.basename",
    'files in current directory':'.listdir',
    'check for folder and file':'path.isfile'
}

command_list = ['.move']

dir = 'root'
path = '\\'
chevron = '>>>'



while True:
    
    a = raw_input(dir + path + ' ' + chevron)
    object = validator(a)
    tasker = task(a)

    if(object.validate__cd()):
        tasker.perform('.cd')
        dir = os.getcwd()
    elif(object.validate__file()):
        tasker.perform('.file')   
    elif(object.validate__folder()):
        tasker.perform('.folder')         
    elif(object.validate__cwd()):
        tasker.perform('.cwd')
    elif(object.validate__quit()):
        tasker.perform('.quit')
    elif(object.validate__help()):
        helper().get_help()
    elif(object.validate__new()):
        tasker.perform('.new')
    elif(object.validate__archive()):
        tasker.perform('.archive')
    elif(object.validate__del()):
        tasker.perform('.del')
    else:
        pass

