package test.java.Task17_TestSuite;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import org.testng.asserts.SoftAssert;

public class Elements {
    WebDriver driver =null;
    @BeforeClass
    public void launchDemoUrl() throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\4B_Java_SeleniumWB_Automation\\4B\\test\\java\\Task1\\chromedriver.exe");
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("https://demoqa.com");
        Thread.sleep(5000);

    }


    @Test
    public void assertElementsPage(){
        WebElement findEle = driver.findElement(By.xpath("//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/*[1]"));
        findEle.click();
        String elements = driver.findElement(By.xpath("//div[@class='pattern-backgound playgound-header']")).getText();
        //Assert.assertEquals(elements, "Elements");
        SoftAssert assertElements = new SoftAssert();
        assertElements.assertEquals(elements, "Elements");
        System.out.println("This is Elements Page");
        //assertElements.assertAll();
    }

    @AfterClass
    public void closeBrowser(){
        driver.quit();
    }


}
