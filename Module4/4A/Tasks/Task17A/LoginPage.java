package Tasks.Task17A;

public abstract class LoginPage {
    private String userName;
    private String passWord;



    public LoginPage(String userName, String passWord) {
        this.userName = userName;
        this.passWord = passWord;

    }

    // Common elements for all login pages
    public void enterUsername() {
        System.out.println("Entering username: " + userName);
    }

    public void enterPassword() {
        System.out.println("Entering password: " + passWord);
    }

    public void clickForgotPassword() {
        System.out.println("Clicking Forgot Password link");
    }

    public void clickSignIn() {
        System.out.println("Clicking Sign In button");
    }

    // Abstract methods for optional elements
    public abstract void clickRememberMe();

    public abstract void clickContinueToHomePage();

    public abstract void clickOAuthButton();
}



