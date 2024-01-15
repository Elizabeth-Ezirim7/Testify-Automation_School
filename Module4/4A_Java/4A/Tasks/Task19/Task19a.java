package Tasks.Task19;
//FINAL: create 3 variables of a class A, ballSize, ballColour, ballTexture.
// and make it impossible to change the value the ballSize in any method in that class
public class Task19a {
    final int ballSize;
    final String ballColour;
    final String ballTexture;

    public Task19a(int ballSize, String ballColour, String ballTexture) {
        this.ballSize = ballSize;
        this.ballColour = ballColour;
        this.ballTexture = ballTexture;
    }


    public void updateBallSize(int newSize) {
        //ballSize = newSize;
    }


}