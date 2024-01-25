package test.java.Task19_MVNCommandLine.Task17_TestSuite;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import org.testng.asserts.SoftAssert;

public class ClassC_SeleniumTrainingMainPage {
    WebDriver driver =null;
    @BeforeClass
    public void launchDemoUrl(){
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\4B_Java_SeleniumWB_Automation\\4B\\test\\java\\Task1\\chromedriver.exe");
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("https://demoqa.com");

    }


    @Test
    public void seleniumTrainingPage() throws InterruptedException {
        //click on Interactions
        WebElement clickSelenium = driver.findElement(By.xpath("//body/div[@id='app']/div[1]/div[1]/div[1]/a[1]/img[1]"));
        clickSelenium.click();
        Thread.sleep(3000);
        String expectedTitle = "Tools QA - Selenium Training";
        String actualTitle = driver.getTitle();
        SoftAssert assertSelPage = new SoftAssert();
        assertSelPage.assertEquals(actualTitle,expectedTitle);
        System.out.println(actualTitle);
        //assertSelPage.assertAll();
    }



    @AfterClass
    public void closeBrowser(){
        driver.quit();
    }
}
