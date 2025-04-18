from Python_Functions import CalBMI, CalBFP


# Python - Body Fat Calculator # 

#----------------------------------------------------------------------------------------#

# 3rd iteration - Create Functions to store different logics and call them. 

Age = 30;
Height = 178;
Weight = 80 ;
Gender = 1  # 1 = Male, 0 = Female


# Call function for getting BMI

BMI = CalBMI(Weight,Height)


# Print the results 

print("Your BMI is:"); 
print(round(BMI,1));


# Call function for getting body fat percentage 

BodyFatPercent = CalBFP(Weight,Height,Age,Gender)

# Print the results 

print("Your Body Fat Percentage is: ");
print(round(BodyFatPercent,1));
