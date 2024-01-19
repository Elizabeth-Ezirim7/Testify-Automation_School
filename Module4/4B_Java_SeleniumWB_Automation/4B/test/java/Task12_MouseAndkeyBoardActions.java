package test.java;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;

public class Task12_MouseAndkeyBoardActions {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\4B_Java_SeleniumWB_Automation\\4B\\test\\java\\Task1\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();
        //launch URl
        driver.get("https://jqueryui.com/");
        Thread.sleep(5000);

        // Locate and click on the "Resizable" menu
        WebElement resizeMenu = driver.findElement(By.xpath("//a[contains(text(),'Resizable')]"));
        resizeMenu.click();

        // Switch to the iframe containing the resizable box
        driver.switchTo().frame(0);


        // Locate the resizable box
        WebElement resizeIcon = driver.findElement(By.xpath("//body/div[@id='resizable']/div[1]"));

        // Use Actions class to perform drag-and-drop to resize the box
        Actions resize = new Actions(driver);
        resize.clickAndHold(resizeIcon).moveByOffset(291, 301).build().perform();

        System.out.println("Resized successfully");
        driver.quit();

    }
}
