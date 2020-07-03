# This is an exercise that helps a user understand syntax, logical connectives, truth values, and truth functions in propositional logic.
def logic_game():

    statement_names = [
        "1 negation",
        "2 conjunction",
        "3 disjunction",
        "4 conditional",
        "5 biconditional"
        ]

    print('''
    This exercise will help you understand some important aspects of propositional logic.
    You'll learn a little bit about propositions, syntax, logical connectives, truth values, and truth functions.
    ''')
    print('''
    Here is a list of the types of statements that you will encounter while doing logic.
    Note the numbers that each type is assigned to. You'll need to refer to that number to begin the game.
    ''')
    print(statement_names)

    response = input('''
    Select a statement's number to begin the associated exercise (for example, type 1 for negation, or 2 for conjunction, etc.): ''')

    if ((response == "1") or (response == "2") or (response == "3") or (response == "4") or (response == "5")):
        print('''
        Let's go!
        ''')
    else:
        print('''
        Invalid response. 
        The game will now restart. When prompted, you must select a number between 1 and 5 to play the game.
        ''')
        logic_game()

    if response == "1":
        print("Negation takes the form of not-p or ~p")
        print('''
        The proposition, p, can have one truth value assigned to it: either T (for true) or F (for false))
        ''')
        prop_t_value = input("Assign a truth value to p. Select either T or F: ")
        prop_t_value = prop_t_value.upper()
        if prop_t_value == "T":
            truth_value_negation = "F"
        else:
            truth_value_negation = "F"
        print('''
        Now if we negate that proposition, p, we will get not-p.
        ''')
        guess = input("Given the previous truth value you assigned to p, what is the truth value of not-p? Enter T or F: ")
        guess = guess.upper()
        if guess == truth_value_negation:
            print("Correct!")
        else:
            print("Incorrect")

    if response == "2":
        print('''
        A conjunction is a complex proposition that takes the following form: p and q.
        'p' and 'q' are variables that refer to propositions.
        The atomic proposition, p, is one conjunct, and the atomic proposition, q, is the other conjunct.
        Both conjuncts are joined by the logical connective "and" (sometimes symbolized as "&").
        ''')
        print("Both p and q have individual truth values. So p can be either T (true) or F (false), and q can be either T (true) or F (false).")
        print('''
        Let us assign truth values to p and q
        ''')
        first_conjunct = input("Assign a truth value to the first conjunct, p. Enter T or F: ")
        first_conjunct = first_conjunct.upper()
        second_conjunct = input("Now assign a truth value to the consequent, q. Enter T of F: ")
        second_conjunct = second_conjunct.upper()
        if first_conjunct == "T" and second_conjunct == "T":
            t_value_conjunction = "T"
        else:
            t_value_conjunction = "F"
        print('''
        The entire conjunction derives its truth value from the truth values of its proper parts (the individual conjuncts).
        ''')
        guess = input("What is the truth value of the conjunction, p and q? Enter either T or F: ")
        if guess == t_value_conjunction:
            print('''
            Correct!
            A conjunction is true whenever both of its conjuncts are true. 
            If either p or q is false, then the conjunction is false. And if both p and q are false, then the conjunction is also false.
            ''')
        else:
            print('''Incorrect.
            A conjunction is true whenever both of its conjuncts are true. 
            If either p or q is false, then the conjunction is false. And if both p and q are false, then the conjunction is also false.
            ''')
    
    if response == "3":
        print('''
        A disjunction is a complex proposition that takes the following form: p or q.
        'p' and 'q' are variables that refer to propositions.
        The atomic proposition, p, is one disjunct, and the atomic proposition, q, is the other disjunct.
        The atomic propositions are joined by the logical connective "or" (sometimes symbolized as "V")
        ''')
        print('''
        The individual disjuncts will be assigned a truth value.
        So, p will be either T (true) or F (false). And q will be either T (true) or F (false)
        ''')
        print('''
        Let us assign truth values to the individual disjuncts.
        ''')
        first_disjunct = input("Assign a truth value to the first disjunct, p. Enter T or F: ")
        first_disjunct = first_disjunct.upper()
        second_disjunct = input("Assign a truth value to the second disjunct, q. Enter T or F: ")
        second_disjunct = second_disjunct.upper()
        if first_disjunct == "T" and second_disjunct == "T":
            t_value_disjunction = "T"
        elif first_disjunct == "T" and second_disjunct == "F":
            t_value_disjunction = "T"
        elif first_disjunct == "F" and second_disjunct == "T":
            t_value_disjunction = "T"
        elif first_disjunct == "F" and second_disjunct == "F":
            t_value_disjunction = "F"
        else:
            print("Invalid inputs. The game will restart.")
            logic_game()
        print('''
        The truth value of a disjunction is derived from the truth values of its disjuncts.
        ''')
        guess = input("Given the truth values you assigned to the disjuncts, what is the truth value of the disjunction? Enter T or F: ")
        guess = guess.upper()
        if guess == t_value_disjunction:
            print('''
            Correct!
            A disjunction is only false when both of its disjuncts are false.
            If one of the disjuncts is true and the other is false, then the disjunction is true.
            And if both disjuncts are true, then the disjunction is true.
            ''')
        else:
            print('''
            Incorrect.
            A disjunction is only false when both of its disjuncts are false.
            If one of the disjuncts is true and the other is false, then the disjunction is true.
            And if both disjuncts are true, then the disjunction is true.
            ''')
    
    if response == "4":
        print('''
        A conditional statement is a complex proposition that takes the following form: if p then q.
        'p' and 'q' are variables that refer to propositions.
        The atomic proposition, p, is the antecedent.
        The atomic proposition, q, is the consequent.
        Sometimes a conditional is symbolized in the following way: p -> q. Here, the arrow symbol "->" is the logical connective that joins the antecedent and consequent.
        ''')
        print('''
        The antecedent and consequent will each be assigned their own truth values.
        So, the antecedent, p, will be either T (true) or F (false). And the consequent, q, will be either T (true) or F (false).
        ''')
        print('''
        Let us assign truth values to p and q.
        ''')
        t_value_antecedent = input("Assign a truth value to the antecedent, p. Enter T or F: ")
        t_value_antecedent = t_value_antecedent.upper()
        t_value_consequent = input("Now, assign a truth value to the consequent, q. Enter T of F: ")
        t_value_consequent = t_value_consequent.upper()
        if t_value_antecedent == "T" and t_value_consequent == "T":
            t_value_conditional = "T"
        elif t_value_antecedent == "T" and t_value_consequent == "F":
            t_value_conditional = "F"
        elif t_value_antecedent == "F" and t_value_consequent == "T":
            t_value_conditional = "T"
        elif t_value_antecedent == "F" and t_value_consequent == "F":
            t_value_conditional = "T"
        else:
            print("Invalid Inputs. The game will restart.")
            logic_game()
        print('''
        The truth value of the conditional statement (if p then q) depends on the truth values of its proper parts (the truth value of the antecedent, p, and the truth value of the consequent, q).
        ''')
        guess = input("Given the previous truth values you assigned to the antecedent and consequent, what is the truth value of the conditional statement? Enter T or F: ")
        guess = guess.upper()
        if guess == t_value_conditional:
            print('''
            Correct!
            A conditional statement is only false when its antecedent is true and its consequent is false.
            So, a conditional is true when both the antecedent and consequent are true.
            A conditional is also true when both the antecedent and consequent are false.
            And a conditional is true when the antecedent is false and the consequent is true.
            ''')
        else:
            print('''
            Incorrect.
            A conditional statement is only false when its antecedent is true and its consequent is false.
            So, a conditional is true when both the antecedent and consequent are true.
            A conditional is also true when both the antecedent and consequent are false.
            And a conditional is true when the antecedent is false and the consequent is true.
            ''')

    if response == "5":
        print('''
        A biconditional statement is a complex proposition that takes the following form: p if and only if q.
        'p' and 'q' refer to individual atomic propositions.
        Sometimes a biconditional is symbolized as 'p <-> q'. The symbol '<->' is a logical connective that joins the atomic propositions, p and q.
        ''')
        print('''
        The atomic propositions in the biconditional will be assigned truth values.
        So, p will be either T (true) or F (false). And q will be either T (true) or F (false).
        ''')
        print('''
        Let us assign truth values to the atomic propositions in the following biconditional: p if and only if q.
        ''')
        first_t_value = input("Assign a truth value to p. Enter T or F: ")
        first_t_value = first_t_value.upper()
        second_t_value = input("Now, assign a truth value to q. Enter T or F: ")
        second_t_value = second_t_value.upper()
        print('''
        The truth value of a biconditional can be derived from the truth values of its atomic propositions.
        ''')
        if first_t_value == "T" and second_t_value == "T":
            t_value_bi = "T"
        elif first_t_value == "T" and second_t_value == "F":
            t_value_bi = "F"
        elif first_t_value == "F" and second_t_value == "T":
            t_value_bi = "F"
        elif first_t_value == "F" and second_t_value == "F":
            t_value_bi = "T"
        else:
            print("Invalid inputs. The game will restart.")
            logic_game()
        guess = input("Given the truth values you assigned to p and q, what is the truth value of the biconditional? Enter T or F: ")
        guess = guess.upper()
        if guess == t_value_bi:
            print('''
            Correct!
            A biconditional is true whenever its atomic propositions share the same truth value.
            So, a biconditional is true when both p and q are true. And a biconditional would be true if both p and q are false.
            A biconditional is false whenever its component atomic propositions have different truth values. 
            So, if p was true and q was false, then the biconditional would be false.
            ''')
        else:
            print('''
            Incorrect.
            A biconditional is true whenever its atomic propositions share the same truth value.
            So, a biconditional is true when both p and q are true. And a biconditional would be true if both p and q are false.
            A biconditional is false whenever its component atomic propositions have different truth values. 
            So, if p was true and q was false, then the biconditional would be false.
            ''')

    replay = input("What to play again? Enter yes or no: ")
    replay = replay.lower()
    if replay == "yes":
        logic_game()
    elif replay == "no":
        print("Thanks for playing!")
        exit
    else:
        print("Invalid input. The game will end. Thanks for playing!")

logic_game()