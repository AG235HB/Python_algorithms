def show_help():
    print "Usage:"
    print "\tmain.py [-h] [-st <type of sort> <sequence>] [-sh]"
    print "Parameters:"
    print "\t-h\t\tShow help."
    print "\t-st\t\tSorting of sequence of numbers. It is necessary"
    print "\t\t\tto specify sorting type."
    print "\t\t\tSequence numbers(figures) can be partitioned by\n\t\t\tspaces or ',';"
    print "\t\t\tif the sequence is not specified, 10 random numbers"
    print "\t\t\twill be generated."
    print "\t\t-b\tBubble sort."
    print "\t\t-i\tInsertion sort."
    print "\t\t-m\tMerge sort."
    print "\t\t-q\tQuick sort."
    print "\t\t-s\tSelection sort."

def mode_selector():
    if len(sys.argv) >= 2:
        if sys.argv[1] == '-h':
            print("Help:")
        elif sys.argv[1] == '-st':
            if len(sys.argv) >= 3:
                if sys.argv[2] == '-b':
                    from sort import bubble
                    if len(sys.argv) == 3:
                        from auxiliary import randomizer
                        collection = list(randomizer.create_collection(10, 0, 25))
                        print "initial collection:\t" + str(collection)
                        print "result collection:\t" + str(bubble.sort(collection))
                    elif len(sys.argv) == 4 and len(sys.argv[3]) > 3:
                        from auxiliary import text_formater
                        st = str(sys.argv[3])
                        collection = [int(item) for item in st.split(text_formater.find_separator(st))]
                        print "initial collection:\t"+ str(collection)
                        print "result collection:\t" + str(bubble.sort(collection))
                    else:
                        st = [int(item) for item in sys.argv[3:]]
                        print "initial collection:\t"+ str(st)
                        print "result collection:\t"+str(bubble.sort(sys.argv[3:]))
                elif sys.argv[2] == '-i':
                    from sort import insertion
                    if len(sys.argv) == 3:
                        from auxiliary import randomizer
                        collection = list(randomizer.create_collection(10, 0, 25))
                        print "initial collection:\t" + str(collection)
                        print "result collection:\t" + str(insertion.sort(collection))
                    elif len(sys.argv) == 4 and len(sys.argv[3]) > 3:
                        from auxiliary import text_formater
                        st = str(sys.argv[3])
                        collection = [int(item) for item in st.split(text_formater.find_separator(st))]
                        print "initial collection:\t" + str(collection)
                        print "result collection:\t" + str(insertion.sort(collection))
                    else:
                        st = [int(item) for item in sys.argv[3:]]
                        print "initial collection:\t" + str(st)
                        print "result collection:\t" + str(insertion.sort(sys.argv[3:]))
                elif sys.argv[2] == '-m':
                    from sort import merge
                    if len(sys.argv) == 3:
                        from auxiliary import randomizer
                        collection = list(randomizer.create_collection(10, 0, 25))
                        print "initial collection:\t"+ str(collection)
                        print "result collection:\t" + str(merge.sort(collection))
                    elif len(sys.argv) == 4 and len(sys.argv[3]) > 3:
                        from auxiliary import text_formater
                        st = str(sys.argv[3])
                        collection = [int(item) for item in st.split(text_formater.find_separator(st))]
                        print "initial collection:\t"+ str(collection)
                        print "result collection:\t" + str(merge.sort(collection))
                    else:
                        st = [int(item) for item in sys.argv[3:]]
                        print "initial collection:\t"+ str(st)
                        print "result collection:\t"+str(merge.sort(sys.argv[3:]))
                elif sys.argv[2] == '-q':
                    from sort import quick
                    if len(sys.argv) == 3:
                        from auxiliary import randomizer
                        collection = list(randomizer.create_collection(10, 0, 25))
                        print "initial collection:\t"+ str(collection)
                        print "result collection:\t" + str(quick.sort(collection))
                    elif len(sys.argv) == 4 and len(sys.argv[3]) > 3:
                        from auxiliary import text_formater
                        st = str(sys.argv[3])
                        collection = [int(item) for item in st.split(text_formater.find_separator(st))]
                        print "initial collection:\t"+ str(collection)
                        print "result collection:\t" + str(quick.sort(collection))
                    else:
                        st = [int(item) for item in sys.argv[3:]]
                        print "initial collection:\t"+ str(st)
                        print "result collection:\t"+str(quick.sort(sys.argv[3:]))
                elif sys.argv[2] == '-s':
                    from sort import selection
                    if len(sys.argv) == 3:
                        from auxiliary import randomizer
                        collection = list(randomizer.create_collection(10, 0, 25))
                        print "initial collection:\t"+ str(collection)
                        print "result collection:\t" + str(selection.sort(collection))
                    elif len(sys.argv) == 4 and len(sys.argv[3]) > 3:
                        from auxiliary import text_formater
                        st = str(sys.argv[3])
                        collection = [int(item) for item in st.split(text_formater.find_separator(st))]
                        print "initial collection:\t"+ str(collection)
                        print "result collection:\t" + str(selection.sort(collection))
                    else:
                        st = [int(item) for item in sys.argv[3:]]
                        print "initial collection:\t"+ str(st)
                        print "result collection:\t"+str(selection.sort(sys.argv[3:]))
                else:
                    show_help()
            else:
                    show_help()
        elif sys.argv[1] == '-sh':
            if len(sys.argv) >= 3:
                if sys.argv[2] == '-bst':
                    print "bst"
                    print sys.argv[3]
                    if sys.argv[3] == "-o":
                        print "o"
                        
                        if len(sys.argv) is 5:
                            print "random"
                            #RANDOM
                            from auxiliary import randomizer
                            collection = list(randomizer.create_collection(10, 0, 25))
                            
                            from search import binary_tree
                            bst = binary_tree.BinaryTree()
                            for i in range(0, 10, 1):
                                bst.add(collection[i])
                            print "initial collection:\t"+ str(collection)
                            string = bst.search(int(sys.argv[4]))
                            print "searchable object:\t" + str(sys.argv[4])
                            print string
                        else:
                            #MANUAL
                            print "manual"
            else:
                    show_help()
            
        elif sys.argv[1] == '-joke':
            import os
            try:
                os.system('cls')
            except:
                os.system('clear')
            print "The classic mistake inventors absolutely reliable systems - this underestimation of the ingenuity of clinical idiots.\n\nDouglas Adams."
        else:
            show_help()
        
    else:
        show_help()

def find_separator(collection):
    for index, item in enumerate(collection):
        if item == ',':
            return ','
        if item == ' ':
            return ' '
    return None

if __name__ == '__main__':
    import sys
    if sys.version_info.major < 3:
        input_func = raw_input
    else:
        input_func = input

    mode_selector()