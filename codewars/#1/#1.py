def human_years_cat_years_dog_years(human_years):
    cat = 0 
    dog = 0
    years = 3
    for i in human_years:
        if years == 1: 
            dog += 15
            cat += 15
            years += 1
        elif years == 2:
            dog += 9
            cat += 9
            years += 1
            
    return [human_years,cat,dog]