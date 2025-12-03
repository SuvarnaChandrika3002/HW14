module.exports = {
  async login(page, u, p) {
    await page.waitForURL("**/static/login.html")
    await page.fill("#u", u)
    await page.fill("#p", p)
    await page.click("button")
    await page.waitForURL("**/static/calculations.html")
  }
}
