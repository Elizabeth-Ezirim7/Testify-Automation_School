package test.java.Tasks.Task2;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
//import org.openqa.selenium.opera.OperaDriver;

public class GoogleNav {
    public static void main(String[] args) {
            System.setProperty("webdriver.chrome.driver", "C:\\Users\\EEzirim\\Documents\\TESTIFY\\Testify-Automation_School\\Module4B\\Tasks\\test\\java\\Tasks\\Task1\\chromedriver.exe");
            WebDriver driver = new ChromeDriver();
            driver.manage().window().maximize();
            driver.get("https://www.google.com/");
            driver.quit();
        }
    }

