package main.java.org.example.PageObjects;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class ProductPage {
    WebDriver Pdriver = null;
    public ProductPage(WebDriver driver){
        Pdriver = driver;
        PageFactory.initElements(Pdriver, this);
    }

    @FindBy(xpath="//button[@id='add-to-cart-sauce-labs-backpack']")
    WebElement items;
    public WebElement addToCart() {
        return items;
    }

    @FindBy(xpath="//body/div[@id='root']/div[@id='page_wrapper']/div[@id='contents_wrapper']/div[@id='header_container']/div[1]/div[3]/a[1]")
    WebElement cartIcon;

    public WebElement clickCartIcon() {

        return cartIcon;
    }






}
