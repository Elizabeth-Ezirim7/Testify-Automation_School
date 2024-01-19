package test.java;

import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.WebElement;

public class Task11_AlertPopUp {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\4B_Java_SeleniumWB_Automation\\4B\\test\\java\\Task1\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();
        //launch URl
        driver.get(" https://www.google.com/ ");
        WebElement clickSearch = driver.findElement(By.xpath("//textarea[@id='APjFqb']"));
        clickSearch.click();
        driver.findElement(By.xpath("//textarea[@id='APjFqb']")).sendKeys("Testify Ltd" + Keys.ENTER);

        Thread.sleep(3000);

        //click on Testify link
        ////body/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[@id='center_col']/div[@id='res']/div[@id='search']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/a[1]/h3[1]
        WebElement testifyLink = driver.findElement(By.xpath
                ("//body/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[@id='center_col']/div[@id='res']/div[@id='search']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/a[1]/h3[1]"));
        testifyLink.click();
        Thread.sleep(5000);
        JavascriptExecutor  js = (JavascriptExecutor) driver;
        js.executeScript("window.scrollBy(0,document.body.scrollHeight)");
        //js.executeScript("window.scrollBy(0, 1000)");
        Thread.sleep(5000);

        //click on linked in
       driver.findElement(By.xpath("//*[@id=\"__next\"]/section/div/div[1]/div[1]/div/div/div[2]/a")).click();


        driver.switchTo().alert().dismiss();
        //close button
        //driver.findElement(By.xpath("//*[@id=\"organization_guest_contextual-sign-in\"]/div/section/button/icon/svg/path")).click();

        Thread.sleep(3000);

        // Get the description text on the user's LinkedIn page
        //.org-top-card-summary__tagline
        WebElement descriptionElement = driver.findElement(By.xpath("//body/div[5]/div[3]/div[1]/div[2]/div[1]/div[2]/main[1]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/p[1]"));
        String descriptionText = descriptionElement.getText();
        System.out.println("LinkedIn Description Text: " + descriptionText);

        driver.quit();

    }
}
