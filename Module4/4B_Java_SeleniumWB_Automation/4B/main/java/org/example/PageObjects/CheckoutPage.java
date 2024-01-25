package main.java.org.example.PageObjects;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class CheckoutPage {
    WebDriver Cdriver = null;

    public CheckoutPage(WebDriver driver){
        Cdriver = driver;

        PageFactory.initElements(Cdriver, this);

    }

    @FindBy(xpath="//input[@id='first-name']")
    WebElement firstname;
    public WebElement getFirstName() {
        return firstname;
    }

    @FindBy(xpath="//input[@id='last-name']")
    WebElement lastname;
    public WebElement getLastName() {
        return lastname;
    }

    @FindBy(xpath="//input[@id='postal-code']")
    WebElement zipcode;
    public WebElement getZipCode() {
        return zipcode;
    }

    @FindBy(xpath="//input[@id='continue']")
    WebElement cont;
    public WebElement clickContinue() {
        return cont;
    }





}
