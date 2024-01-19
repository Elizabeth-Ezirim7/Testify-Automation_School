package test.java;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Task9_BrowserNavigations {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\4B_Java_SeleniumWB_Automation\\4B\\test\\java\\Task1\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();
        //launch URl
        driver.get("https://www.saucedemo.com/");
        //Enter UserName
        driver.findElement(By.xpath("//input[@id='user-name']")).click();
        driver.findElement(By.xpath("//input[@id='user-name']")).sendKeys("standard_user");

        //Enter Password
        driver.findElement(By.xpath("//input[@id='password']")).click();
        driver.findElement(By.xpath("//input[@id='password']")).sendKeys("secret_sauce");

        driver.findElement(By.xpath("//input[@id='login-button']")).click();
        Thread.sleep(5000);
        driver.navigate().back();

        //String loginValue = driver.findElement(By.cssSelector("#login-button")).getAttribute("submit-button");
        String loginValue = driver.findElement(By.cssSelector("#login-button")).getAttribute("value");
        System.out.println(loginValue);


        Thread.sleep(5000);
        driver.navigate().forward();

        Thread.sleep(5000);
        String homePageValue  = driver.findElement(By.cssSelector("div.page_wrapper div.inventory_container div.inventory_list div.inventory_item:nth-child(1) div.inventory_item_description div.inventory_item_label a:nth-child(1) > div.inventory_item_name")).getText();

        System.out.println(homePageValue);

        driver.quit();



    }
}
