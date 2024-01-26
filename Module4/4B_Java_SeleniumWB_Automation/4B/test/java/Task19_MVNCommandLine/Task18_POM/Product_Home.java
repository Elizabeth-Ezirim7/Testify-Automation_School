package test.java.Task19_MVNCommandLine.Task18_POM;

import main.java.org.example.PageObjects.SauceLoginPage;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;
import org.testng.asserts.SoftAssert;

import java.util.concurrent.TimeUnit;

public class Product_Home {
    WebDriver driver;

    @Test(groups = {"one"})
    public void verifySauceDemoHomepage(){
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\4B_Java_SeleniumWB_Automation\\4B\\test\\java\\Task1\\chromedriver.exe");
        driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
        driver.manage().window().maximize();
        SauceLoginPage login = new SauceLoginPage(driver);
        driver.get("https://www.saucedemo.com/");
        login.getUserName().sendKeys("standard_user");
        login.getPassWord().sendKeys("secret_sauce");
        login.getLogin().click();
        System.out.println("login is successful");
        //String expectedTitle = "Swag Labs";
        //String actualTitle = driver.getTitle();
        String pageText = driver.findElement(By.cssSelector(".app_logo")).getText();
        SoftAssert confirmHome = new SoftAssert();
        confirmHome.assertEquals(pageText,"Swag Labs");
        System.out.println("This is the homepage for Sauce Demo");
        confirmHome.assertAll();

    }


    @Test
    public void closeBrowser(){
        driver.quit();
    }
}
