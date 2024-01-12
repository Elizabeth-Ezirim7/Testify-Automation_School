package Tasks;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
//import org.openqa.selenium.Alert;
//import org.openqa.selenium.support.ui.ExpectedConditions;
//import org.openqa.selenium.support.ui.WebDriverWait;
//import java.time.Duration;
//import java.time.LocalDate;

public class Task4 {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4\\Module4B\\src\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();
        //launch URl
        driver.get("http://demo.guru99.com/");
        //Click on the security Project menu.
        driver.findElement(By.xpath("//a[contains(text(),'Security Project')]")).click();
        driver.switchTo().frame("image-with-cta-on-larger-screen");
        ////*[@id="dismiss-button"]/div/span

        Thread.sleep(3000);
        driver.findElement(By.xpath("//*[@id=\"dismiss-button\"]/div/span")).click();;

        Thread.sleep(3000);
        //Enter UserId
        driver.findElement(By.xpath("//tbody/tr[1]/td[2]/input[1]")).click();

        driver.findElement(By.xpath("//tbody/tr[1]/td[2]/input[1]")).sendKeys("Elizabeth7");
        //Enter Password
        driver.findElement(By.xpath("//tbody/tr[2]/td[2]/input[1]")).click();
        driver.findElement(By.xpath("//tbody/tr[2]/td[2]/input[1]")).sendKeys("Test123$");

        driver.close();

    }
}
