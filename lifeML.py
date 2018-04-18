from persistence import get_bmi_list

def get_life_expectancy():
    bmis = get_bmi_list()
    return 100 - sum(bmis)/len(bmis)
