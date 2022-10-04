import java.util.Scanner;

public class IntroJava_NoHelp_TemirlanNurmambetov {
    
    public static void main(String[] args) {
        askPerson();
    }
    
    static void askPerson(){
        
        // Variables we are going to be using
        String answer1 = "Nunavut";
        String[] answer3 = {"Alberta", "Saskatchewan", "Manitoba"};
        int answer2 = 13;
        int score = 0;
        int[] answer4 = {2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015};
        
        
        // FYI
        System.out.println("\nTo Exit Type Exit In The Name Section\n");
        
        // Gets user input by creating scanner objects
        Scanner input = new Scanner(System.in);
        System.out.println("What is your name? ");
        String name = input.nextLine();
        
        // Stops the method
        if (name.equalsIgnoreCase("exit")){
            return;
        }
    
        // Checks if the answers are correct and counts it and states if they are rightor wrong
        Scanner input1 = new Scanner(System.in);
        System.out.println("\nIqaluit is the capital of which territory?: ");
        String question1 = input1.nextLine();
        
        if (question1.equalsIgnoreCase(answer1)) {
            score++;
            System.out.println("Correct!");
        } else {
            System.out.println("...wrong");
        } 

        Scanner input2 = new Scanner(System.in);
        System.out.println("\nHow many provinces and territories are there in Canada?: ");
        int question2 = input2.nextInt();
        
        if (question2 == answer2){
            score++;
            System.out.println("Correct!");
        } else {
            System.out.println("...wrong");
        }
        
        Scanner input3 = new Scanner(System.in); // Iterates over the list to check if the answer is one of them
        System.out.println("\nName one province that is in the \'prairies\'.");
        String question3 = input3.nextLine();
        
        for (int i = 0; i < answer3.length; i++){
            if (question3.equalsIgnoreCase(answer3[i])){
                score++; 
                System.out.println("Correct!");
                break;
            } else {
                System.out.println("...wrong");
                break;
            }
        }
        
        Scanner input4 = new Scanner(System.in);
        System.out.println("\nName one year during which Stephen Harper was prime minister.");
        int question4 = input4.nextInt();
        
        for (int n = 0; n < answer4.length; n++){
            if (question4 == answer4[n]){
                score++;
                System.out.println("Correct!");
                break;
            } else {
                System.out.println("...wrong");
                break;
            }
        }
    
        // Result
        System.out.println("\n" + name + ", you received "+score+" out of 4");
        System.out.println("This test was created and marked by Temirlan Nurmambetov\n");
        
        
        // Runs Chat bot
        chatBot();
        askPerson();
        
    }
    
    static void chatBot(){
        // Variables we are going to be using
        boolean isGood = false;
        boolean isOk = false;
        boolean isFailed = false;
        
        // Asks for users response
        Scanner a = new Scanner(System.in);
        System.out.println("How did you feel about today's test?");
        String response = a.nextLine();
        
        // Iterates through the strings and the list to check if the words match
        
        if (response.toLowerCase().contains("good".toLowerCase()) || response.toLowerCase().contains("great".toLowerCase())){
            isGood = true;
        } else if (response.toLowerCase().contains("fine".toLowerCase()) || response.toLowerCase().contains("ok".toLowerCase())){
            isOk = true;
        } else if (response.toLowerCase().contains("failed".toLowerCase())){
            isFailed = true;
        }
        

    
        
        // Feedback based on their response
        
        if (isGood) {
            System.out.println("\nYou must be a genius!");
        } else if (isOk){
            System.out.println("\nI am glad you did ok. Feel free to ask for a study guide next time to help you prepare.");            
        } else if (isFailed){
            System.out.println("\nWell, then you should sign up for summer school, quickly.");
        } else {
            System.out.println("\nThank you for taking the test.");
        }
    }
    
    
}
