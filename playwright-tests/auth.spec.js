const { test, expect } = require("@playwright/test")

test("register and login", async ({ page }) => {
  await page.goto("/static/register.html")
  await page.fill("#u","u1")
  await page.fill("#p","p1")
  await page.click("button")
  await page.waitForURL("**/static/login.html")
  await page.fill("#u","u1")
  await page.fill("#p","p1")
  await page.click("button")
  await expect(page).toHaveURL(/calculations/)
})
