
# Python - Body Fat Calculator # 

#----------------------------------------------------------------------------------------#

# Create whole program 2nd iteration - User input 

# Store User input
Age = input("Enter Age:");
Height = input("Enter Height (cm)");
Weight = input("Enter Weight (kg)");
Gender = input("Enter Gender (M/F):");  # 1 = Male, 0 = Female


# Printing User Input 

print("You Have entered:");
print("------------------");
print("Age: " + Age);
print("Height: " + Height);
print("Weight: " + Weight);
print("Gender: " + Gender);
print("------------------");
print("Processing....");


# Logic for BMI 

#Convert to int 
Weight  = int(Weight);
Height = int(Height);

BMI = Weight / (Height/100 * Height/100);

# Print the results 

print("Your BMI is:");
print(round(BMI,1));


print("------------------");
print("Processing....");


# Change user input to numbers 
Gender = 1 if Gender == "M" else 0;

 #Convert to int 
Age = int(Age);
Gender = int(Gender);

 # Logic for Body fat %

BFP = (1.20 * BMI) + (0.23 * Age) - (10.8 * Gender) - 5.4;


# Print the results 

print("Your Body Fat Percentage is: ");
print(round(BFP,1));  

print("------------------");
print("Processing....");
print("Thank You !!");
print("------------------");