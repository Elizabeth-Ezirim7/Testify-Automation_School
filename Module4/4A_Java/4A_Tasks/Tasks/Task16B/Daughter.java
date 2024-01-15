package Tasks.Task16B;

public class Daughter extends Father {
    public static void main(String[] args) {


        Daughter lizzy = new Daughter();
        lizzy.learnAutomation("Java");
        lizzy.learnSofWareTesting("Automation");

    }


    public void learnAutomation(String type){
        System.out.println("Elizabeth is a Java Programmer");
    }

    public void learnSofWareTesting(String type){
        System.out.println("ELizabeth is an automation Engineer");
    }


}


