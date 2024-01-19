package test.java;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import java.util.concurrent.TimeUnit;

public class Task14_Synchronization {
    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\4B_Java_SeleniumWB_Automation\\4B\\test\\java\\Task1\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
        driver.manage().window().maximize();
        //launch URl
        driver.get("http://www.toolsqa.com/");
        //Pop up is not visible
        System.out.println("Pop up is not visible");
        //Click on the tutorial icon
        driver.findElement(By.linkText("TUTORIALS")).click();

        System.out.println("Successfully clicked on the tutorial icon");

        driver.quit();
    }
}
