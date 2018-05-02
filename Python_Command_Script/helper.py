class helper:

    intro = '''This is simple python comman line which can be used for navigating through directories using simple commands.\n 
List of all commands is given as folllows feel free to call for hel using '.help' command
'''

    demo = 'Help for '
    __helper = {
        '.cd':demo+'.cd',
        '.file':demo+'.file',
        '.folder':demo+'.folder',
        '.cwd':demo+'.cwd',
        '.quit':demo+'.quit',
        '.help':demo+'.help',
        '.new':demo+'.new'
        }

    def get_help(self):
        print helper.intro
        print
        for i in helper.__helper.keys():
            print helper.__helper[i]


