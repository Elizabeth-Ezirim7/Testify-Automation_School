package Tasks.Task14;

public class SquareValues {

    public static void main(String[] args) {

        SquareShape objAttributes = new SquareShape();
        objAttributes.setShapeLength(10);
        int length = objAttributes.getShapeLength();

        //Breadth
        objAttributes.setShapeBreadth(20);
        int breadth = objAttributes.getShapeBreadth();

        int area = length * breadth;


        //System.out.println(area);
        System.out.println("The area of a square of length: " + length +
                " and breadth: " + breadth +
                " is " + area);
    }
}
