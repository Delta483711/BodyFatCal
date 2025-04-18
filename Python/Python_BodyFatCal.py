
# Python - Body Fat Calculator # 

#----------------------------------------------------------------------------------------#

# Create whole program 1st iteration - hard coded

#Declare Variables 

Age = 30;
Age = 0;
Height = 178;
Weight = 80 ;
Gender = 1  # 1 = Male, 0 = Female


# Logic for BMI 

BMI = Weight / (Height/100 * Height/100);

# Print the results 

print("Your BMI is:"); 
print(round(BMI,1));


# Logic for BMI 

BMI = Weight / (Height/100 * Height/100);
print("Your BMI is:"); 
print(round(BMI,1));

# Logic for Body fat %

BFP = (1.20 * BMI) + (0.23 * Age) - (10.8 * Gender) - 5.4;

# Print the results 

print("Your Body Fat Percentage is: ");
print(round(BFP,1)); 




#----------------------------------------------------------------------------------------#
# Create whole program 2nd iteration - User input 

















#----------------------------------------------------------------------------------------#
# 3rd iteration - Create Functions to store different logics and call them. 




