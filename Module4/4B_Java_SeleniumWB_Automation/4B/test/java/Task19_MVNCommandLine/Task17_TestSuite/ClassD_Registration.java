package test.java.Task19_MVNCommandLine.Task17_TestSuite;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class ClassD_Registration {

    WebDriver driver =null;
    @BeforeClass
    public void launchDemoUrl() throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\4B_Java_SeleniumWB_Automation\\4B\\test\\java\\Task1\\chromedriver.exe");
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("https://demoqa.com");
        Thread.sleep(3000);

    }


    @Test(priority = 1)
    public void seleniumTrainingPage() throws InterruptedException {

        //click on Selenium
        WebElement clickSelenium = driver.findElement(By.xpath("//body/div[@id='app']/div[1]/div[1]/div[1]/a[1]/img[1]"));
        clickSelenium.click();
        Thread.sleep(3000);
        driver.navigate().to("https://www.toolsqa.com/selenium-training/");


    }

    @Test(priority = 2)
    public void registration() throws InterruptedException {
        //Go to registration button
        Thread.sleep(3000);
        WebElement clickReg = driver.findElement(By.xpath("//a[contains(text(),'Go To Registration')]"));
        clickReg.click();
        System.out.println("Registration Button clicked on successfully");
    }

    @AfterClass
    public void closeBrowser(){
        driver.quit();
    }
}
