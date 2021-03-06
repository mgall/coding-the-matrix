from functools import reduce
voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, ... ]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    name = lambda senator: senator.split(" ")[0]
    votes = lambda senator: map(int,senator.split[3:])

    senators = open('voting_record_dump109.txt','r')
    voting = { name(s):votes(s) for s in list(senators) }
    senators.close()

    return voting

## Task 2

def policy_compare(sen_a, sen_b, voting):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    return sum((a*b for a,b in zip(voting[sen_a],voting[sen_b])))


## Task 3

def most_similar(sen, voting):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    sim = max(( (policy_compare(sen,sen_c,voting), sen_c) for sen_c in voting if sen_c != sen ))
    return sim[1]
    

## Task 4

def least_similar(sen, voting):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    sim = min(( (policy_compare(sen,sen_c,voting), sen_c) for sen_c in voting if sen_c != sen ))
    return sim[1]

## Task 5

most_like_chafee    = most_similar('Chafee',create_voting_dict())
least_like_santorum = least_similar('Santorum',create_voting_dict())



# Task 6

def find_average_similarity(sen, sen_set, voting):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    return sum((policy_compare(sen,sen_c,voting) for sen_c in sen_set)) / len(sen_set)

most_average_Democrat = 'Biden'


# Task 7

def find_average_record(sen_set, voting):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1],\ 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    sens = (voting[sen] for sen in sen_set)
    avg = reduce(lambda s1,s2: [v1+v2 for v1,v2 in zip(s1,s2)], sens)
    n = len(sen_set)
    return [v/n for v in avg]

average_Democrat_record = [-0.16279069767441862, -0.23255813953488372, 1.0,
   0.8372093023255814, 0.9767441860465116, -0.13953488372093023, -0.9534883720930233,
   0.813953488372093, 0.9767441860465116, 0.9767441860465116, 0.9069767441860465,
   0.7674418604651163, 0.6744186046511628, 0.9767441860465116, -0.5116279069767442,
   0.9302325581395349, 0.9534883720930233, 0.9767441860465116, -0.3953488372093023,
   0.9767441860465116, 1.0, 1.0, 1.0, 0.9534883720930233, -0.4883720930232558,
   1.0, -0.32558139534883723, -0.06976744186046512, 0.9767441860465116,
   0.8604651162790697, 0.9767441860465116, 0.9767441860465116, 1.0, 1.0,
   0.9767441860465116,-0.3488372093023256, 0.9767441860465116, -0.4883720930232558,
   0.23255813953488372, 0.8837209302325582, 0.4418604651162791, 0.9069767441860465,
   -0.9069767441860465, 1.0, 0.9069767441860465, -0.3023255813953488]



# Task 8

def bitter_rivals(voting):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    sens = voting.keys()
    bitter = min( ( (policy_compare(s1,s2,voting),s1,s2)  for s1 in sens for s2 in sens if s1!=s2) )
    return (bitter[1], bitter[2])

