package test.java.Task18_POM;

import main.java.org.example.PageObjects.*;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import org.testng.asserts.SoftAssert;

import java.util.concurrent.TimeUnit;

public class SauceDemoTest {
    WebDriver driver = null;

    @BeforeClass
    public void demoLogin() throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\4B_Java_SeleniumWB_Automation\\4B\\test\\java\\Task1\\chromedriver.exe");
        driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
        driver.manage().window().maximize();
        //launch URl
        driver.get("https://www.saucedemo.com/");


        }
    @Test(priority = 1)
    public void userLogin() throws InterruptedException {
        SauceLoginPage login = new SauceLoginPage(driver);
        login.getUserName().sendKeys("standard_user");
        login.getPassWord().sendKeys("secret_sauce");
        login.getLogin().click();
        System.out.println("login is successful");

    }

    @Test(priority = 2)
    public void selectItems() throws InterruptedException {
        ProductPage product = new ProductPage(driver);
        product.addToCart().click();
        product.clickCartIcon().click();
        System.out.println("Item selected successfully");

    }

    @Test(priority = 3)
    public void assertAndCheckOut() throws InterruptedException {
        YourCartPage yourCart = new YourCartPage(driver);
        String cartText = "Sauce Labs Backpack";
        SoftAssert confirm = new SoftAssert();
        confirm.assertEquals(cartText, "Sauce Labs Backpack");
        System.out.println(cartText);
        yourCart.clickCheckOutButton().click();
        System.out.println("Selected item successfully verified");
        confirm.assertAll();


    }

    @Test(priority = 4)
    public void clickCheckoutButton() throws InterruptedException {
        CheckoutPage checkoutObj = new CheckoutPage(driver);
        checkoutObj.getFirstName().sendKeys("Beth");
        checkoutObj.getLastName().sendKeys("Zaac");
        checkoutObj.getZipCode().sendKeys("12345");
        checkoutObj.clickContinue().click();
        System.out.println("CheckOut successfully clicked");

    }

    @Test(priority = 5)
    public void assertAndFinish() throws InterruptedException {
        CheckOverViewPage overviewObj = new CheckOverViewPage(driver);
        String cartTextTwo = "Sauce Labs Backpack";
        SoftAssert confirmTwo = new SoftAssert();
        confirmTwo.assertEquals(cartTextTwo, "Sauce Labs Backpack");
        System.out.println("Overview Page has " + cartTextTwo);
        overviewObj.clickFinishButton().click();
        System.out.println("Selected item asserted successfully alongside click button");
        confirmTwo.assertAll();

    }
    @AfterClass
    public void closeBrowser(){
        driver.close();
    }

}