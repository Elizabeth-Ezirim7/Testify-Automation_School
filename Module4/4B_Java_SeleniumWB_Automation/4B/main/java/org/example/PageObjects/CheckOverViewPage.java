package main.java.org.example.PageObjects;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class CheckOverViewPage {
    WebDriver Ddriver = null;

    public CheckOverViewPage(WebDriver driver){
        Ddriver = driver;

        PageFactory.initElements(Ddriver, this);
    }

    @FindBy(css=".btn_action")
    WebElement finishButton;
    public WebElement clickFinishButton() {
        return finishButton;
    }
}
