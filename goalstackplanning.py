"""
This module is the main program
"""
from block import block
import re
from block_mover import block_mover

PREDICATES = ['ON', 'ONTABLE', 'HOLDING', 'CLEAR', 'ARMEMPTY']

def check_p(to_check, claw, current_state=[]):
    """
        check if the predicate to be evaluated is fulfilled
    """

    to_check = to_check[to_check.index('(')+1:to_check.index(')')]
    block_names = re.split(',', to_check)
    iterar = True
    cont = 1
    if to_check.startswith('ONTABLE'):
        pass
    elif to_check.startswith('ON'):
        cont = 2
    elif to_check.startswith('CLEAR'):
        cont = 3
    elif to_check.startswith('HOLDING'):
        iterar = False
        cont = 4
    elif to_check.startswith('ARMEMPTY'):
        iterar = False
        cont = 5

    if iterar:
        #check onTable
        if cont == 1:
            for tower in current_state:
                if tower[0] == block_names[0]:
                    return True

        #check ON
        elif cont == 2:
            for tower in current_state:
                if block_names[0] in tower:
                    ind = tower.index(block_names[0])
                    if ind > 0:
                        under = tower[ind-1]
                        if block_names[1] == under:
                            return True

        #check clear
        elif cont == 3:
            for tower in current_state:
                if block_names[0] in tower:
                    ind = tower.index(block_names[0])
                    if ind == (len(tower)-1):
                        return True
        return False
    else:
        if cont == 4:
            if claw.is_empty() == False:
                if claw.holding == block_names[0]:
                    return True
        elif cont == 5:
            return claw.is_empty()
        return False

def get_relevant_actions(to_check, current_state, claw):
    """
    this method returns the relevant actions so that the predicate is fulfilled
    that is being evaluated as well as its preconditions
    """

    tst = to_check[to_check.index('(')+1:to_check.index(')')]
    block_names = re.split(',', tst)
    to_execute = []
    b1_name = block_names[0]
    if to_check.startswith('ONTABLE'):
        to_execute.append('PUTDOWN({})'.format(b1_name))
        to_execute.append('HOLDING({})'.format(b1_name))
        for torre in current_state:
            if b1_name in torre:
                ind = torre.index(b1_name)
                to_execute.append('UNSTACK({},{})'.format(b1_name, torre[ind-1]))
                to_execute.append('ARMEMPTY(@)')
                to_execute.append('CLEAR({})'.format(b1_name))
                to_execute.append('ON({},{})'.format(b1_name, torre[ind-1]))

    elif to_check.startswith('ON'):
        to_execute.append('STACK({},{})'.format(b1_name, block_names[1]))
        to_execute.append('HOLDING({})'.format(b1_name))
        to_execute.append('CLEAR({})'.format(block_names[1]))

    elif to_check.startswith('CLEAR'):
        for torre in current_state:
            if b1_name in torre:
                ind = torre.index(b1_name)
                to_execute.append('UNSTACK({},{})'.format(torre[ind+1], b1_name))
                to_execute.append('ARMEMPTY(@)')
                to_execute.append('CLEAR({})'.format(torre[ind+1]))
                to_execute.append('ON({},{})'.format(torre[ind+1], b1_name))

    elif to_check.startswith('HOLDING'):
        to_execute.append('PICKUP({})'.format(b1_name))
        to_execute.append('ARMEMPTY(@)')
        to_execute.append('ONTABLE({})'.format(b1_name))
        to_execute.append('CLEAR({})'.format(b1_name))

    elif to_check.startswith('ARMEMPTY'):
        to_execute.append('PUTDOWN({})'.format(claw.holding))
        to_execute.append('HOLDING({})'.format(claw.holding))
    return to_execute

def apply_action(to_apply, current_state, claw):
    """
    makes changes to the current state based on the action
    received as param
    """
    tst = to_apply[to_apply.index('(')+1:to_apply.index(')')]
    block_names = re.split(',', tst)
    b1_name = block_names[0]
    if to_apply.startswith('STACK'):
        for tower in current_state:
            if b1_name in tower:
                tower.remove(b1_name)
            if block_names[1] in tower:
                tower.append(b1_name)
        claw.put_down(claw.holding)

    elif to_apply.startswith('UNSTACK'):
        for tower in current_state:
            if b1_name in tower:
                tower.remove(b1_name)
        #nt = [b1_name]
        claw.pickup(b1_name)
        #current_state.append(nt)

    elif to_apply.startswith('PICKUP'):
        claw.pickup(b1_name)
        for tower in current_state:
            if b1_name in tower:
                tower.remove(b1_name)


    elif to_apply.startswith('PUTDOWN'):
        claw.put_down(b1_name)
        nt = [b1_name]
        current_state.append(nt)

    return current_state


INPUT = open('initial.txt', 'r')
STATE1 = []
for linear in INPUT:
    tmp_list = re.split(r'\W+', linear)
    if '' in tmp_list:
        tmp_list.remove("")
    STATE1.append(tmp_list)
INPUT.close()

INPUT2 = open('final.txt', 'r')
STATE2 = []
for linear in INPUT2:
    tmp_list = re.split(r'\W+', linear)
    if '' in tmp_list:
        tmp_list.remove("")
    STATE2.append(tmp_list)
INPUT2.close()


def solve():
    """
    This method is responsible for solving a problem using
    goal stack planning
    """
    my_stack = []
    plan = []
    current_state = STATE1
    blocks = []
    for line in STATE1:
        mi_len = len(line)
        for i in range(mi_len):
            on_table = False
            clear = True
            ntmp = line[i]
            if i+1 < mi_len:
                clear = False

            if i < 1:
                on_table = True
            else:
                pass
            props = {'name': ntmp, 'onTable': on_table, 'clear':clear}
            btmp = block(ntmp, props)
            blocks.append(btmp)


    #now it's time to put the final state together and put it on the stack
    complex_goal = ''
    for line in STATE2:
        mi_len = len(line)
        state = ''
        for i in range(mi_len):
            ntmp = line[i]
            #print i
            if i-1 >= 0:
                state += 'ON({},{})^'.format(ntmp, line[i-1])
            if i < 1:
                state += 'ONTABLE({})^'.format(ntmp)
        complex_goal += state
    complex_goal = complex_goal[:-1]
    sub_goals = re.split(r'\^', complex_goal)
    my_stack.append(complex_goal)

    #add subgoals to the stack
    for goal in sub_goals:
        my_stack.append(goal)


    #here the problem is solved
    my_claw = block_mover()
    while my_stack:
        for torre in current_state:
            if len(torre) < 1:
                current_state.remove(torre)
        accion_actual = my_stack.pop()
        ind = accion_actual.index('(')
        pred = '@'
        if ind > 0:
            pred = accion_actual[:ind]
        print(accion_actual)
        if pred in PREDICATES:
            if '^' in accion_actual:
                tmp_gls = re.split(r'\^', accion_actual)
                compliment = True
                for meta in tmp_gls:
                    compliment = compliment and check_p(meta, my_claw, current_state)


            else:
                compliment = check_p(accion_actual, my_claw, current_state)
                if compliment == False:
                    rest = get_relevant_actions(accion_actual, current_state, my_claw)
                    my_stack.extend(rest)

        #entering this else implies that it is an action and
        # therefore must be added to the plan VERIFY THIS PART

        else:
            current_state = apply_action(accion_actual, current_state, my_claw)
            plan.append(accion_actual)
    print("**********************")
    print(plan)
solve()
