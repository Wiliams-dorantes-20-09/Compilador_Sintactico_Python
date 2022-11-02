from src.SCM import SCMCompiler

def test():
    from src.test import TEST_FILES_NAMES, TEST_FILES_DIRS
    print "Elija un archivo de prueba para compilar:\n"
    for i,t in enumerate(TEST_FILES_NAMES, start=1):
        print "\t{}. {}".format(i, t)
    print
    test_file = raw_input("Tu opcion [default 1]: ")
    option = test_file if test_file != "" else 1
    if int(option) < len(TEST_FILES_DIRS) + 1:
        main(TEST_FILES_DIRS[int(option)-1], print_tokens=True)
    else:
        print "Opcion incorrecta"

def main(code_file_dir=None, print_tokens=False):
    if code_file_dir:
        print "\nCompilado: ", code_file_dir
        obj = SCMCompiler(src=code_file_dir, print_tokens=print_tokens)
        obj.compile()


if __name__ == '__main__':
    import sys, os, getopt
    if len(sys.argv) > 1:
        print_tokens = False
        opts = []
        try:
            opts, args = getopt.getopt(sys.argv[1:],"hp",["imprimir", "ayuda"])
        except getopt.GetoptError, e:
            print str(e)
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                print 'use:\n\tpython compile.py -p <archivo de codigo>'
                print '\tpython compile.py --print <archivo de codigo>'
                sys.exit()
            elif opt in ("-p", "--print"):
                print_tokens = True
        try:
            code_file_dir = args[0]
        except:
            code_file_dir = ""
        if os.path.isfile(code_file_dir):
            main(code_file_dir, print_tokens=print_tokens)
        else:
            print '[ERROR] Ruta de archivo invalida'
    else:
        test()