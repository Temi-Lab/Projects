import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

/*
 * Takes Student Emails and Stores it in a txt file
 */

class EmailTaker{

    public static void appendStrToFile(String fileName, String str){
        try {
 
            // object of BufferedWriter class
            BufferedWriter out = new BufferedWriter(
                new FileWriter("EmailList.txt", true));
 
            // Writing on output stream
            out.write(str);
            // Closing the connection
            out.close();
        }
 
        // Catch block to handle the exceptions
        catch (IOException e) {
 
            // Display message when exception occurs
            System.out.println("exception occurred" + e);
        }
    }

    public static void main(String[] args){
        // create scanner object
        Scanner input = new Scanner(System.in);
        ArrayList<String> studentEmails = new ArrayList<String>();

        while(true){
            // Takes emails
            String email = input.nextLine();

            // Checks if it needs to stop
            if (email.equals("stop")){ 
                
                System.out.println("--------------------");

                // When stops it prints all the student emails to the txt file
                for (String x : studentEmails){
                    appendStrToFile("EmailList.txt", x+"\n");
                }
                break;
            } 

            //Adds the email to the Array
            studentEmails.add(email);
        }
    }
}
