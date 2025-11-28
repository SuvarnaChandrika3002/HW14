import { test, expect } from '@playwright/test';

test('User can register and login', async ({ page }) => {

  // OPEN REGISTER PAGE
  await page.goto('http://127.0.0.1:8001/forntend/register.html');

  await page.fill('#email', 'test@example.com');
  await page.fill('#password', '123456');
  await page.click('button[type="submit"]');

  await page.waitForTimeout(800);

  // OPEN LOGIN PAGE
  await page.goto('http://127.0.0.1:8001/forntend/login.html');

  await page.fill('#email', 'test@example.com');
  await page.fill('#password', '123456');
  await page.click('button[type="submit"]');

  await page.waitForURL('**/forntend/calculations.html', { timeout: 8000 });
});
