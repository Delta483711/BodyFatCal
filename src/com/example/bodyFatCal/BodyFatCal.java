package com.example.bodyFatCal;

//Import
import java.text.DecimalFormat;
import java.util.*;

public class BodyFatCal {


    public static void main(String[] args) {

        Scanner Sc = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("0.00");

        System.out.println("This is the First Iteration of the App " +
                "that will Calculate Body Fat Percentage. Type Yes to continue or No to Leave");
        String input = Sc.nextLine();

        //if Statement
        if(input.equals("Yes")){
            //Ask for Height
            System.out.println("Enter your Height (Cm)");
            double Height = Sc.nextDouble();

            //Ask for Weight
            System.out.println("Enter your Weight(Kg)");
            double Weight = Sc.nextDouble();

            //Calculation for  Getting BMI
            double BMI = Weight / (Height/100 * Height/100);

            System.out.println("your BMI is "
                    +  df.format(BMI));

            //Ask for Age
            System.out.println("Enter your Age");
            double Age = Sc.nextDouble();

            //Ask for Gender
            System.out.println("Enter your Gender 1 for Male 2 for Female");
            double Gender = Sc.nextDouble();

            double BFP = (1.20 * BMI) + (0.23 * Age) - (10.8 * Gender) - 5.4;

            System.out.println("Your Body Fat Percentage is: " + BFP);


        }
        else if(input.equals("No")){
            System.out.println("Thank you.");
            Sc.nextLine();
            Sc.close();
        }
    }
}
