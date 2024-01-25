package test.java.Task17_TestSuite;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import org.testng.asserts.SoftAssert;

public class Interactions {

    WebDriver driver =null;
    @BeforeClass
    public void launchDemoUrl(){
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\4B_Java_SeleniumWB_Automation\\4B\\test\\java\\Task1\\chromedriver.exe");
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("https://demoqa.com");

    }


    @Test
    public void assertInteractionsPage(){
        //click on Interactions
        WebElement clickInt = driver.findElement(By.xpath("//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]/div[2]/*[1]"));
        clickInt.click();
        String interactions = driver.findElement(By.className("main-header")).getText();
        //Assert.assertEquals(interactions, "Interactions");
        SoftAssert assertInteractions = new SoftAssert();
        assertInteractions.assertEquals(interactions, "Interactions");
        System.out.println("This is interactions page");
        assertInteractions.assertAll();
    }

    @AfterClass
    public void closeBrowser(){
        driver.quit();
    }

}
