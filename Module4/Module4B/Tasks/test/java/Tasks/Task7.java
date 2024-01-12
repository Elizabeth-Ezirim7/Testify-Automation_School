package Tasks;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.Keys;
//import org.openqa.selenium.support.ui.ExpectedConditions;
//import org.openqa.selenium.support.ui.WebDriverWait;
//import java.time.Duration;
//import java.time.LocalDate;
//import org.openqa.selenium.By;
//import org.openqa.selenium.Keys;
//import org.openqa.selenium.WebDriver;
//import org.openqa.selenium.WebElement;
//import org.openqa.selenium.chrome.ChromeDriver;
//import org.openqa.selenium.support.ui.ExpectedConditions;
//import org.openqa.selenium.support.ui.WebDriverWait;
//import java.time.Instant;



public class Task7 {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\Module4B\\src\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();
        //launch URl
        driver.get("https://worldweather.wmo.int/en/home.html");
        Thread.sleep(10000);
        //String autoCom = driver.findElement(By.cssSelector(".top_searchbox")).getAttribute("autocomplete");
        //System.out.println(autoCom);

        driver.findElement(By.xpath("//input[@type='text']")).click();
        //driver.findElement(By.cssSelector(".top_searchbox")).sendKeys("Lagos" + Keys.ENTER);
        driver.findElement(By.xpath("//input[@type='text']")).sendKeys("Lagos");
        //form[@id='searchForm']/input[3]
        driver.findElement(By.xpath("//input[@name='submit']")).click();
        //Thread.sleep(10000);
        //driver.findElement(By.name("submit")).click();
        //driver.findElement(By.cssSelector(".top_searchbox_submit")).click();

        //Thread.sleep(1000);
        ///html/body/div[1]/div[6]/div[5]/div[2]
        String weatherRep;
        weatherRep = By.xpath("/html/body/div[1]/div[6]/div[5]/div[2]").findElement(driver).getText();
        Thread.sleep(1000);
        System.out.println(weatherRep);

        driver.quit();

    }
}
