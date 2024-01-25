package test.java.Task19_MVNCommandLine.Task17_TestSuite;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;
import org.testng.asserts.SoftAssert;

public class ClassA_AFWindows {
    WebDriver driver;

    @Test(groups = {"one"})
    public void userDemoQaHomepage() throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\4B_Java_SeleniumWB_Automation\\4B\\test\\java\\Task1\\chromedriver.exe");
        //driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("https://demoqa.com");
        Thread.sleep(3000);
        //String homePage = driver.findElement(By.cssSelector(".banner-image")).getText();
        SoftAssert assertHomepage = new SoftAssert();
        String homePage = driver.findElement(By.cssSelector(".banner-image")).getText();
        //String expectedTitle = "Selenium Online Trainings";
        //assertHomepage.assertEquals(actualTitle,expectedTitle);
        assertHomepage.assertEquals(homePage, "Selenium Online Training");
        System.out.println("This is the HomePage for Demo QA");
        //assertHomepage.assertAll();


    }



    @Test(priority = 2)
    public void clickAlertsFramesWindows() throws InterruptedException {
        WebElement findAFW = driver.findElement(By.xpath("//h5[contains(text(),'Alerts, Frame & Windows')]"));
        findAFW.click();
        Thread.sleep(3000);

    }

    @Test(priority = 3)
    public void assertAFWPage(){
        //WebElement findAFW = driver.findElement(By.xpath("//h5[contains(text(),'Alerts, Frame & Windows')]"));
        //findAFW.click();
        String afw = driver.findElement(By.xpath("//*[@id=\"app\"]/div/div/div[1]")).getText();
        //Assert.assertEquals(elements, "Elements");
        SoftAssert assertAFW = new SoftAssert();
        assertAFW.assertEquals(afw, "Alerts, Frame & Windows");
        System.out.println("This is AFW Page");
        assertAFW.assertAll();
    }

    @Test(priority = 4)
    public void closeBrowser(){
        driver.quit();
    }


}
