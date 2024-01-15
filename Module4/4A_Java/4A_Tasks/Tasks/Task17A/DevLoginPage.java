package Tasks.Task17A;

public class DevLoginPage extends LoginPage{

    public DevLoginPage(String userName, String passWord) {
        super(userName, passWord);
    }

    @Override
    public void clickRememberMe() {
        System.out.println("Click Remember me check box");

    }

    @Override
    public void clickContinueToHomePage() {
        System.out.println("click on continue to home page");

    }

    @Override
    public void clickOAuthButton() {
        System.out.println("click on the OAuth button");

    }
}
