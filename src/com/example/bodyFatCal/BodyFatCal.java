package com.example.bodyFatCal;

//Import
import java.util.Scanner;

public class BodyFatCal {


    public static void main(String[] args) {

        Scanner Sc = new Scanner(System.in);

        System.out.println("This is the First Iteration of the App " +
                "that will Calculate Body Fat Percentage. Type Yes to continue or No to Leave");
        String  input = Sc.nextLine();

        if(input.equals("Yes")){
            System.out.println("Enter your Height (Cm)");
            float Height = Sc.nextFloat();

            System.out.println("Enter your Weight(Kg)");
            float Weight = Sc.nextFloat();
        }
        else if(input.equals("No")){
            System.out.println("Thank you.");
            Sc.nextLine();
            Sc.close();
        }
    }
}
