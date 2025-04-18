
# Logic for BMI 

def CalBMI(Weight, Height):

    return Weight / (Height/100 * Height/100)


#Logic for Body Fat Percentage 

def CalBFP(Weight,Height,Age,Gender):

    BFP = (1.20 * CalBMI(Weight,Height) ) + (0.23 * Age) - (10.8 * Gender) - 5.4;
    
    return BFP