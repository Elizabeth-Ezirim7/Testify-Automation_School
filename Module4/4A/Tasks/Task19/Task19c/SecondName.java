package Tasks.Task19.Task19c;

//Task 19
public class SecondName extends FirstName {

    public SecondName(String name) {
        super(name);
    }

    public static void main(String[] args) {
        String name1 = "Anderson";
        SecondName myName = new SecondName(name1);
        //myName.firstName();
        myName.secondName();

        //Accessing the variable 'name' from class A using super
        System.out.println("Value from Class FirstName: " + myName.name);

        //Accessing the variable 'name' from class B
        System.out.println("Value from Class SecondName: " + myName.name);


    }

    private void secondName() {
    }

}