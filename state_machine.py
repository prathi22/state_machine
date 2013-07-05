STATE_MACHINE={'s':{'final':False,'transition':(None,'int',None)},
 'int':{'final':True,'transition':(None,'int','s1')},
 's1':{'final':False,'transition':(None,'s2',None)},
 's2':{'final':True,'transition':(None,'s2',None)}
 }

def regular_exp(a):
    cur_state=STATE_MACHINE['s']
    count=1
    for c in a:
        if c.isalpha():
            try:
                cur_state=STATE_MACHINE[cur_state['transition'][0]]
            except KeyError:
                print 'Invalid decimal number'
                return
        elif c.isdigit():
            cur_state=STATE_MACHINE[cur_state['transition'][1]]
        elif c=='.':
            count=count+1
            if count>1:
                try:
                    cur_state=STATE_MACHINE[cur_state['transition'][2]]
                except KeyError:
                    print 'Invalid decimal number'
                    return                                                        
        else:
            print 'Invalid state'
            break
    if cur_state['final']==True:
        print 'Valid decimal number'
    

a=raw_input('Enter a value:')
print 'Input is:',a
regular_exp(a)
