package test.java;

import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import org.testng.asserts.SoftAssert;

public class Task16_TestNGAssert {
    WebDriver driver = null;
    @BeforeClass
    public void launchTestify() throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\4B_Java_SeleniumWB_Automation\\4B\\test\\java\\Task1\\chromedriver.exe");
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get(" https://testifyltd.com/ ");
        JavascriptExecutor js = (JavascriptExecutor) driver;
        js.executeScript("window.scrollBy(0,document.body.scrollHeight)");
        Thread.sleep(5000);

    }

    @Test
    public void assertContact(){
        String email = "info@testifyltd.com"; //info@testifyltd.com
        String Location = "Nigeria";
        String phoneNumber = "(+234)905-882-0971";
        SoftAssert contact = new SoftAssert();
        contact.assertEquals(email, "info@testifyltd.co.uk");
        contact.assertEquals(Location, "Nigeria");
        contact.assertEquals(phoneNumber, "(+234)904-882-0971");
        System.out.println("Contact details asserted successfully");
        contact.assertAll();

    }


    @AfterClass
    public void closeBrowser(){

        driver.quit();
    }
}
