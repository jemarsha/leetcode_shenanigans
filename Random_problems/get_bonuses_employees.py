#You are the manager of a number of employees who all sit in a row.
# The CEO would like to give bonuses to all of your employees,
# but since the company did not perform so well this year the CEO would like to keep the bonuses to a minimum.

#The rules of giving bonuses is that:
#- Each employee begins with a bonus factor of 1x.
#- For each employee, if they perform better than the person sitting next to them, the employee is given +1 higher bonus
# (and up to +2 if they perform better than both people to their sides).

#Given a list of employee's performance, find the bonuses each employee should get.


#Example:
#Input: [1, 2, 3, 2, 3, 5, 1]
#Output: [1, 2, 3, 1, 2, 3, 1]


def get_bonuses(performance):  #O(n) time. just have a separate array of O(n) space to store the bonuses. You can also alternatively use the same array and just modify
    #values so you won't use any extra space by other means.

    """

    Args: array with current performance values

    Output: array of bonuses based on performance against others

    @type performance: object
    """

    bonuses = [1] * len(performance)

    if len(performance) <=1:
        return bonuses

    if performance[0] > performance[1]:
        bonuses[0] = performance[0] +1

    if performance[len(performance)-1] > performance[len(performance)-2]:
        bonuses[len(performance)-1] = bonuses[len(performance)-1] +1

    for i in range(1,len(performance)-1):

        if performance[i] > performance[i-1] and performance[i] > performance[i+1]:
            bonuses[i] +=2

        elif performance[i] > performance[i-1] or performance[i] > performance[i+1]:
            bonuses[i] +=1

    return bonuses

if __name__ =='__main__':

    test1 =  [1,2]

    test2 = [1, 2, 3, 2, 3, 5, 1]

    test3 = []

    test4 = [0, 0, 0, 0, 0, 1, 0]

    print(get_bonuses(test4))