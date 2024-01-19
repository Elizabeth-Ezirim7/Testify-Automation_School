package Tasks.Task17B;

public class TestersTest implements LoginTest {
    @Override
    public void testUsername(String username) {
        System.out.println("Verify that  " + username + "is correct");

    }

    @Override
    public void testPassword(String password) {
        System.out.println("Verify that  " + password + "is correct");

    }

    @Override
    public void testSuccessfulLogin(String username, String password) {
        System.out.println("Verify that login with  " + username + "&" + password + "is successful");

    }
}
