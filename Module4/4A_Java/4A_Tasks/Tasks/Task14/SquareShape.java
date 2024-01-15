package Tasks.Task14;

public class SquareShape {

    public static void main(String[] args) {
        SquareShape objShape = new SquareShape();
        objShape.getShapeSides();
        int correctShape = objShape.getShapeSides();
        System.out.println(correctShape);
    }
    private int shapeSides = 4;
    private int shapeLength;
    private int shapeBreadth;


    public int getShapeSides() {
        return shapeSides;
    }

    public int getShapeLength() {
        return shapeLength;
    }

    public void setShapeLength(int shapeLength) {
        this.shapeLength = shapeLength;
    }

    public int getShapeBreadth() {
        return shapeBreadth;
    }

    public void setShapeBreadth(int shapeBreadth) {
        this.shapeBreadth = shapeBreadth;
    }


}
