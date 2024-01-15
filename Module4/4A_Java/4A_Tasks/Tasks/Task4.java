package Tasks;

//find the area of a circle with radius on12.7m. Print out your result with the unit of measurement which is metres

public class Task4 {
    public static void main(String[] args) {
        // Define the radius of the circle
        double radius = 12.7; // in meters

        // Calculate the area of the circle
        double area = Math.PI * Math.pow(radius, 2);

        // Print out your result with the unit of measurement which is metres
        System.out.println("The area of the circle with radius " + radius + " meters is: " + area + " square meters");


    }
}
