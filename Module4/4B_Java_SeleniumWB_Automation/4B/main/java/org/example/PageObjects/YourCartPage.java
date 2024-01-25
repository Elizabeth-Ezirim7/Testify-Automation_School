package main.java.org.example.PageObjects;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class YourCartPage {
    WebDriver Ydriver = null;
    public YourCartPage(WebDriver driver){
        Ydriver = driver;
        PageFactory.initElements(Ydriver, this);
    }


    @FindBy(xpath="//button[@id='checkout']")
    WebElement checkoutButton;

    public WebElement clickCheckOutButton() {
        return checkoutButton;
    }

}
