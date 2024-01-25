package test.java;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class Task15_TestNG {
    WebDriver driver =null;
    @BeforeMethod
    public void googleNav() throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\4B_Java_SeleniumWB_Automation\\4B\\test\\java\\Task1\\chromedriver.exe");
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("https://www.google.com/");
        driver.findElement(By.xpath("//textarea[@id='APjFqb']")).sendKeys("Testify" + Keys.ENTER);
        Thread.sleep(5000);

    }
    @Test
    public void macDonalds(){
        //https://www.mcdonalds.com/us/en-us.html
        driver.get("https://www.mcdonalds.com/us/en-us.html");
        //find order now button color code
        //System.out.println("Order Now Button Color is : " + orderButtonColor);
        //System.out.println("Order Now Button Color is: ");
        System.out.println("Order Now Button Color is: " + driver.findElement(By.xpath("//a[@id='button-ordernow']")).getCssValue("background-color"));

    }

    @AfterMethod
    public void closeBrowser(){
        driver.quit();

    }


}
