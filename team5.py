####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team5'
strategy_name = 'Eval betrayal hsitory'
strategy_description = '''\
Collude first round. Collude, unless betrayed; then always betray.'''
    
def move(my_history, their_history, my_score, their_score):
    '''This evaluates the history of their 10 prior moves. If within those 10 
moves, they have betrayed 3 or more times, we return betray. Otherwise, always
return collude.

    '''
    if 'b' in their_history[0:10] >=3:
        return 'b'
    else:
        return 'c'
