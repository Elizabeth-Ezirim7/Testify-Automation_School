package Tasks.Task19.Task19c;

public class SecondName extends FirstName{

    public static void main(String[] args) {
        String name = "Anderson";
      SecondName myName = new SecondName(name);
      myName.firstName();
      myName.secondName();

    }
    public SecondName(String name) {
        super(name);
    }

    public void secondName(){
        System.out.println(name + " is my name");

    }


}
