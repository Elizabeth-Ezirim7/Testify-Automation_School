package test.java;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Task8_ElementState {
    public static void main(String[] args) throws InterruptedException {


        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\4B_Java_SeleniumWB_Automation\\4B\\test\\java\\Task1\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();
        //launch URl
        driver.get("https://idorenyinankoh.github.io/loginPage/");
        //check if Create is enabled
        boolean createState1 = driver.findElement(By.xpath("//button[@id='create']")).isEnabled();

        //Enter FirstName
        driver.findElement(By.xpath("//input[@id='firstName']")).click();
        driver.findElement(By.xpath("//input[@id='firstName']")).sendKeys("Elizabeth");

        //Enter lastName
        driver.findElement(By.xpath("//input[@id='lastName']")).click();
        driver.findElement(By.xpath("//input[@id='lastName']")).sendKeys("Ezirim");

        //Enter Email
        driver.findElement(By.xpath("//input[@id='email']")).click();
        driver.findElement(By.xpath("//input[@id='email']")).sendKeys("leezbeth@gmail.com");

        //Select Gender
        driver.findElement(By.xpath("//input[@id='female']")).click();

        //Enter Password
        driver.findElement(By.xpath("//input[@id='password']")).click();
        driver.findElement(By.xpath("//input[@id='password']")).sendKeys("Test123$");

        //Confirm Password
        driver.findElement(By.xpath("//input[@id='confirmPass']")).click();
        driver.findElement(By.xpath("//input[@id='confirmPass']")).sendKeys("Test123$");


        //Tell us about you
        driver.findElement(By.xpath("//input[@id='xpLevel']")).click();
        driver.findElement(By.xpath("//input[@id='xpLevel']")).sendKeys("I am a QA Engineer");
        //driver.findElement(By.xpath("//input[@id='xpLevel']")).click();

        Thread.sleep(5000);

        //Create
        boolean createState2 = driver.findElement(By.xpath("//button[@id='create']")).isEnabled();
        System.out.println(createState1);
        System.out.println(createState2);

        Thread.sleep(5000);

        driver.quit();
    }
}