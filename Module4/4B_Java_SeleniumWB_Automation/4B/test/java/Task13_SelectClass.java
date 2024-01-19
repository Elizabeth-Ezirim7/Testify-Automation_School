package test.java;

import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

public class Task13_SelectClass {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\4B_Java_SeleniumWB_Automation\\4B\\test\\java\\Task1\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();
        //launch URl
        driver.get("https://selenium08.blogspot.com/");
        Thread.sleep(5000);
        //select Element
        WebElement searchField = driver.findElement(By.xpath("//div[contains(text(),'Search')]"));
        searchField.click();
        //WebElement searchParameter = driver.findElement(By.xpath("//input[@name='q']"));
        //searchParameter.sendKeys("Demo dropdown");
        driver.findElement(By.xpath("//input[@name='q']")).sendKeys("Demo dropdown" + Keys.ENTER);
        //Thread.sleep(3000);

        driver.findElement(By.xpath("//a[contains(text(),'Read more')]")).click();
        Thread.sleep(5000);
        JavascriptExecutor js = (JavascriptExecutor) driver;
        js.executeScript("window.scrollTo(0, 200)");
        Thread.sleep(3000);
        WebElement selectElement = driver.findElement(By.xpath("//body/div[1]/div[2]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[3]/div[1]/div[1]/select[1]"));
        Select select = new Select(selectElement);
        select.selectByVisibleText("Nigeria");
        Thread.sleep(5000);
        //selectCountry Element
        WebElement monthElement = driver.findElement(By.xpath("//body/div[1]/div[2]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/select[1]"));
        Select selectMonth = new Select(monthElement);
        selectMonth.selectByIndex(1);
        Thread.sleep(3000);
        selectMonth.selectByValue("Feb");
        Thread.sleep(3000);
        selectMonth.selectByIndex(3);

        System.out.println("Country and months selected successfully");

        driver.quit();



    }
}
