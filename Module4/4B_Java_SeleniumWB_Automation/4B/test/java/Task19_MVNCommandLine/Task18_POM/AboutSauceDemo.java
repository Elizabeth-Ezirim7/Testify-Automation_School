package test.java.Task19_MVNCommandLine.Task18_POM;

import main.java.org.example.PageObjects.SauceLoginPage;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.util.concurrent.TimeUnit;

public class AboutSauceDemo {
    WebDriver driver;

    @BeforeClass
    public  void loginSauce() throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\4B_Java_SeleniumWB_Automation\\4B\\test\\java\\Task1\\chromedriver.exe");
        driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
        driver.manage().window().maximize();
        //launch URl
        driver.get("https://www.saucedemo.com/");
        SauceLoginPage login = new SauceLoginPage(driver);
        login.getUserName().sendKeys("standard_user");
        login.getPassWord().sendKeys("secret_sauce");
        login.getLogin().click();
        Thread.sleep(3000);
    }

    @Test
    public void clickHamburger(){
        //Click on Hamburger icon
        driver.findElement(By.xpath("//button[@id='react-burger-menu-btn']")).click();
        //Click on About://a[@id='about_sidebar_link']
        driver.findElement(By.xpath("//a[@id='about_sidebar_link']")).click();
        driver.navigate().to("https://saucelabs.com/");
        System.out.println("This is the About page of Sauce website...Thank you for visiting our site");

    }

    @AfterClass
    public void closeBrowser(){
        driver.quit();
    }

}
