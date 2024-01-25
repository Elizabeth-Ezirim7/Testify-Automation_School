package test.java.Task19_MVNCommandLine.Task18_POM;

import main.java.org.example.PageObjects.SauceLoginPage;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.util.concurrent.TimeUnit;

public class FilterOption {
    WebDriver driver;
    @BeforeClass
    public  void loginSauce() {
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
    }

    @Test
    public void filterOption() throws InterruptedException {
        WebElement filterBox = driver.findElement(By.xpath("//body/div[@id='root']/div[@id='page_wrapper']/div[@id='contents_wrapper']/div[@id='header_container']/div[2]/div[1]/span[1]/select[1]"));
        Select filterSel = new Select(filterBox);
        filterSel.selectByVisibleText("Price (low to high)");
        Thread.sleep(5000);
        System.out.println("Price (low to high) are nice to have");

    }

    @AfterClass
    public void closeBrowser(){
        driver.quit();
    }
}
