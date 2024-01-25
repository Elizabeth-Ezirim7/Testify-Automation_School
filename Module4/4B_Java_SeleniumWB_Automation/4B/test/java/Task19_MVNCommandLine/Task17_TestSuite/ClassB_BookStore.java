package test.java.Task19_MVNCommandLine.Task17_TestSuite;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import org.testng.asserts.SoftAssert;

public class ClassB_BookStore {


    WebDriver driver =null;
    @BeforeClass
    public void launchDemoUrl(){
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\4B_Java_SeleniumWB_Automation\\4B\\test\\java\\Task1\\chromedriver.exe");
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("https://demoqa.com");

    }


    @Test
    public void assertBookStorePage(){
        JavascriptExecutor js = (JavascriptExecutor) driver;
        js.executeScript("window.scrollBy(0, 500)");

        //click on Interactions
        WebElement clickBook = driver.findElement(By.xpath("//h5[contains(text(),'Book Store Application')]"));
        clickBook.click();
        String bookStore = driver.findElement(By.className("main-header")).getText();
        //Assert.assertEquals(interactions, "Interactions");
        SoftAssert assertBookStore = new SoftAssert();
        assertBookStore.assertEquals(bookStore, "Book Store");
        System.out.println("This is Book Store page");
        assertBookStore.assertAll();
    }

    @AfterClass
    public void closeBrowser(){
        driver.quit();
    }
}
