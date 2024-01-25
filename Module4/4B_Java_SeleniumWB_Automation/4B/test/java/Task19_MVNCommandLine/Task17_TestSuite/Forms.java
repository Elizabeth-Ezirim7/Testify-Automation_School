package test.java.Task19_MVNCommandLine.Task17_TestSuite;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import org.testng.asserts.SoftAssert;

public class Forms {
    WebDriver driver =null;
    @BeforeClass
    public void launchDemoUrl() throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\4B_Java_SeleniumWB_Automation\\4B\\test\\java\\Task1\\chromedriver.exe");
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("https://demoqa.com");
        Thread.sleep(3000);

    }


    @Test
    public void assertFormsPage(){
        //click on Forms
        WebElement clickForm =driver.findElement(By.xpath("//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/*[1]"));
        clickForm.click();
        String forms = driver.findElement(By.className("main-header")).getText();
        //Assert.assertEquals(forms, "Forms");
        SoftAssert assertForms = new SoftAssert();
        assertForms.assertEquals(forms, "Forms");
        System.out.println("This is forms page");
        assertForms.assertAll();
    }

    @AfterClass
    public void closeBrowser(){
        driver.quit();
    }
}
