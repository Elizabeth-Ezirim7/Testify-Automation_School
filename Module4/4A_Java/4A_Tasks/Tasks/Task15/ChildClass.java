package Tasks.Task15;

public class ChildClass extends ParentClass{
    public static void main(String[] args) {
        ChildClass myClass = new ChildClass();
        ParentClass myChild = new ParentClass();
        myChild.cook();
        myChild.sing();
        myChild.teach();
        myClass.run();
        myClass.dance();
    }

    public void run(){
        System.out.println("Usain Bolt runs very fast");
    }

    public void dance(){
        System.out.println("Dance and win a prize");

    }

}
